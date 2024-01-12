import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import sqlite3
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Sending the question and getting response from gemini 
def get_response(question,prompt):
   response = chat.send_message([prompt,question])
   return response.text

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# To retreive query from db
def read_sql_query(sql_query,db):
   connect = sqlite3.connect(db)
   curs = connect.cursor()
   curs.execute(sql_query)
   rows = curs.fetchall()
   connect.commit()
   connect.close()
   for row in rows:
      print(row)
   return rows

# Defining the prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit
st.set_page_config(page_title='Text2SQL')
st.title('Text2SQL')
st.sidebar.title("Chat History")
st.header('Bot to Retrive SQL Data')

question = st.text_input("A",key='input_question',label_visibility='hidden')
submit = st.button('Retrieve SQL')

if submit:
   response = get_response(question,prompt[0])

   st.session_state['chat_history'].append(("You", question))

   st.subheader('Your SQL Query is ...')
   print(response)
   st.write(response)

   db_records = read_sql_query(response, "student.db")
   print(db_records)

   st.session_state['chat_history'].append(("Bot", db_records))

   st.subheader('The Records are ...')
   for row in db_records:
      print(row)
      st.write(row)

for role, text in st.session_state['chat_history']:
    # Limit display to a maximum of 100 words with an ellipsis for longer messages
    truncated_text = ''.join(str(item) for item in text[:30]) + ('...' if len(text) > 30 else '')
    st.sidebar.text(f"{role}: {truncated_text}")


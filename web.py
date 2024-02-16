import streamlit as st
import function

# Read the text file to todos
todos = function.read_todo()

# Streamlit text messages
st.title("Welcome to Nathaniel Todo App")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity')

# A for loop to read the text messages to checkbox
for todo in todos:
    st.checkbox(todo)

# Receive input from users
st.text_input(label=" ", placeholder="Add new todo...")


st.checkbox("Buy grocery")
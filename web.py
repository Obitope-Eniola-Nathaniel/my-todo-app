import streamlit as st

import function

# Read the text file to todos
todos = function.read_todo()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todo(todos)


# Streamlit text messages
st.title("Welcome to Nathaniel Todo App")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity')

# A for loop to read the text messages to checkbox and also remove checkbox when click
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Receive input from users
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state

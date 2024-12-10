import streamlit as st
from streamlit import session_state

import functions

todos=functions.read_todos()
def addtodo():

    todo=session_state['todo']+'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("todo's")
st.subheader("find the checkboxes below")
todos=functions.read_todos()

for index,todo in enumerate(todos) :
     checkbox=st.checkbox(todo,key=todo)
     if checkbox:
            todos.pop(index)
            functions.write_todos(todos)

st.text_input(label="b",placeholder="Enter a new todo....",on_change=addtodo,key='todo')
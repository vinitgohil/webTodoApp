import streamlit as st
from modules import utils
import time

taskList = utils.read_taskfile()

def addTask():
    task = st.session_state['newTask'] + "\n"
    taskList.append(task.capitalize())
    utils.write_taskfile(taskList)
    st.session_state["newTask"] = ""


st.title("My Todo App")
st.subheader("Web Application to add tasks to your to-do list")
st.write("This is to manage your tasks and your <b>productivity</b>.",
        unsafe_allow_html=True)


st.text_input(label="Enter a Task to do:", placeholder="Add task...",
              on_change=addTask, key='newTask')

for index, task in enumerate(taskList):
    checkboxTask = st.checkbox(task, key=task)
    if checkboxTask:
        taskList.pop(index)
        utils.write_taskfile(taskList)
        del st.session_state[task]
        st._rerun()



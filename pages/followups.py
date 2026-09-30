import streamlit as st
from database.database import execute
from utils.helpers import page_header,to_dataframe

page_header("Follow-ups & Tasks","Manage reminders and customer actions")

with st.form("task"):
    title=st.text_input("Task")
    related=st.text_input("Related lead/customer/order")
    due=st.date_input("Due date")
    assigned=st.text_input("Assigned to")
    if st.form_submit_button("Add Task") and title:
        execute("INSERT INTO followups(company_id,title,related_to,due_date,assigned_to) VALUES(1,?,?,?,?)",
                (title,related,str(due),assigned))
        st.success("Task added.")

rows=execute("SELECT * FROM followups ORDER BY due_date",fetch=True)
st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)

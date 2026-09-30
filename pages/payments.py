import streamlit as st
from database.database import execute
from utils.helpers import page_header,to_dataframe

page_header("Payments & Receivables","Track advances, balances and overdue payments")

with st.form("payment"):
    order=st.number_input("Order ID",min_value=0,step=1)
    amount=st.number_input("Amount",min_value=0.0)
    currency=st.selectbox("Currency",["USD","EUR","GBP","AED","PKR"])
    due=st.date_input("Due date")
    status=st.selectbox("Status",["Pending","Partial","Paid","Overdue"])
    if st.form_submit_button("Add Payment") and amount>0:
        execute("INSERT INTO payments(company_id,order_id,amount,currency,due_date,status) VALUES(1,?,?,?,?,?)",
                (order,amount,currency,str(due),status))
        st.success("Payment saved.")

rows=execute("SELECT * FROM payments ORDER BY due_date",fetch=True)
st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)

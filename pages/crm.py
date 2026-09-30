import streamlit as st
from database.database import execute
from utils.helpers import page_header, to_dataframe

page_header("CRM", "Manage buyers, customers, contacts and business relationships")

tabs = st.tabs(["Customers", "Add Customer", "Pipeline"])

with tabs[0]:
    rows = execute("SELECT * FROM customers ORDER BY id DESC", fetch=True)
    st.dataframe(to_dataframe(rows), use_container_width=True, hide_index=True)

with tabs[1]:
    with st.form("customer"):
        name=st.text_input("Contact name")
        company=st.text_input("Company")
        email=st.text_input("Email")
        country=st.text_input("Country")
        notes=st.text_area("Notes")
        if st.form_submit_button("Save Customer") and name:
            execute("INSERT INTO customers(company_id,name,company_name,email,country,notes) VALUES(1,?,?,?,?,?)",
                    (name,company,email,country,notes))
            st.success("Customer saved.")

with tabs[2]:
    st.info("Pipeline: New → Contacted → Replied → Interested → Meeting → Customer → Not Interested")

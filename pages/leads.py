import streamlit as st
import pandas as pd
from database.database import execute
from utils.helpers import page_header, to_dataframe

page_header("Leads", "Import, add and manage business leads")

with st.expander("Add Lead"):
    with st.form("lead_form"):
        name=st.text_input("Contact name")
        company=st.text_input("Company")
        email=st.text_input("Business email")
        country=st.text_input("Country")
        product=st.text_input("Product interest")
        source=st.text_input("Source")
        status=st.selectbox("Status", ["New","Contacted","Replied","Interested","Meeting","Customer","Not Interested"])
        notes=st.text_area("Notes")
        if st.form_submit_button("Save Lead") and name:
            execute("""INSERT INTO leads(company_id,name,company_name,email,country,product_interest,source,status,notes)
                       VALUES(1,?,?,?,?,?,?,?,?)""",
                    (name,company,email,country,product,source,status,notes))
            st.success("Lead saved.")

st.subheader("Import CSV")
upload=st.file_uploader("CSV file", type=["csv"])
if upload:
    df=pd.read_csv(upload)
    st.dataframe(df.head(), use_container_width=True)
    if st.button("Import rows"):
        for _,r in df.fillna("").iterrows():
            execute("""INSERT INTO leads(company_id,name,company_name,email,country,product_interest,source)
                       VALUES(1,?,?,?,?,?,?,?)""",
                    (str(r.get("name","")),str(r.get("company_name","")),str(r.get("email","")),
                     str(r.get("country","")),str(r.get("product_interest","")),str(r.get("source",""))))
        st.success(f"Imported {len(df)} leads.")

rows=execute("SELECT * FROM leads ORDER BY id DESC",fetch=True)
st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)

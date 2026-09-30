import streamlit as st
import pandas as pd
from database.database import execute
from utils.helpers import page_header

page_header("Analytics & Reports","CRM, sales, export, inventory and payment intelligence")

orders=execute("SELECT country, SUM(value) total FROM export_orders GROUP BY country",fetch=True)
if orders:
    df=pd.DataFrame([dict(r) for r in orders])
    st.subheader("Sales by Country")
    st.bar_chart(df.set_index("country")["total"])
else:
    st.info("Add export orders to populate analytics.")

payments=execute("SELECT status, SUM(amount) total FROM payments GROUP BY status",fetch=True)
if payments:
    df=pd.DataFrame([dict(r) for r in payments])
    st.subheader("Payments by Status")
    st.bar_chart(df.set_index("status")["total"])

st.subheader("Business Insights")
st.write("Future AI analysis can summarize trends, risks, receivables, product performance and operational bottlenecks.")

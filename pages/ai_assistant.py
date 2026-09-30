import streamlit as st
from ai.business_analysis import analyze_business
from database.database import scalar
from utils.helpers import page_header

page_header("Universal AI Business Assistant","Ask questions about authorized company data")

q=st.text_area("Ask your business assistant",
    placeholder="Show my pending payments, summarize my leads, or suggest follow-ups...")
if st.button("Ask AI"):
    summary=f"""
    Leads: {scalar("SELECT COUNT(*) FROM leads")}
    Customers: {scalar("SELECT COUNT(*) FROM customers")}
    Orders: {scalar("SELECT COUNT(*) FROM export_orders")}
    Products: {scalar("SELECT COUNT(*) FROM products")}
    Pending payments: {scalar("SELECT COALESCE(SUM(amount),0) FROM payments WHERE status != 'Paid'")}
    User request: {q}
    """
    st.write(analyze_business(summary))

st.caption("AI actions that modify or send business data should require explicit user confirmation.")

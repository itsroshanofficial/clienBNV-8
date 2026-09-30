import streamlit as st
from database.database import scalar, execute
from utils.helpers import page_header, kpi

page_header("Dashboard", "Your complete business and export overview")

leads = scalar("SELECT COUNT(*) FROM leads")
customers = scalar("SELECT COUNT(*) FROM customers")
orders = scalar("SELECT COUNT(*) FROM export_orders")
products = scalar("SELECT COUNT(*) FROM products")
pending = scalar("SELECT COALESCE(SUM(amount),0) FROM payments WHERE status != 'Paid'")

c1,c2,c3,c4,c5 = st.columns(5)
with c1: kpi("Leads", leads)
with c2: kpi("Customers", customers)
with c3: kpi("Orders", orders)
with c4: kpi("Products", products)
with c5: kpi("Receivables", f"${pending:,.0f}")

st.divider()
st.subheader("Business Workflow")
st.info("Lead → Outreach → Reply → Follow-up → Buyer → Quotation → Order → Inventory → Documents → Shipment → Payment → Analytics")

st.subheader("Quick Actions")
a,b,c,d = st.columns(4)
with a:
    if st.button("➕ Add Lead", use_container_width=True):
        st.switch_page("pages/leads.py")
with b:
    if st.button("✉️ Write AI Email", use_container_width=True):
        st.switch_page("pages/campaigns.py")
with c:
    if st.button("📦 Add Product", use_container_width=True):
        st.switch_page("pages/inventory.py")
with d:
    if st.button("🚢 New Export Order", use_container_width=True):
        st.switch_page("pages/export_orders.py")

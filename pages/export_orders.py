import streamlit as st
from database.database import execute
from utils.helpers import page_header,to_dataframe

page_header("Export Orders","Command center for buyer, order, payment, shipment and documents")

with st.form("order"):
    buyer=st.text_input("Buyer")
    country=st.text_input("Country")
    value=st.number_input("Order value",min_value=0.0)
    currency=st.selectbox("Currency",["USD","EUR","GBP","AED","PKR"])
    incoterm=st.selectbox("Incoterm",["EXW","FCA","FOB","CFR","CIF","DAP","DDP"])
    expected=st.date_input("Expected shipment date")
    if st.form_submit_button("Create Export Order") and buyer:
        execute("""INSERT INTO export_orders(company_id,buyer_name,country,value,currency,incoterm,expected_ship_date)
                   VALUES(1,?,?,?,?,?,?)""",
                (buyer,country,value,currency,incoterm,str(expected)))
        st.success("Export order created.")

rows=execute("SELECT * FROM export_orders ORDER BY id DESC",fetch=True)
st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)

st.info("Recommended lifecycle: Confirmed → Production → Ready to Ship → Booked → Shipped → In Transit → Delivered")

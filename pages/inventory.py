import streamlit as st
from database.database import execute
from utils.helpers import page_header,to_dataframe

page_header("Inventory & Product Catalog","Products, stock and low-stock intelligence")

with st.form("product"):
    name=st.text_input("Product name")
    sku=st.text_input("SKU")
    price=st.number_input("Price",min_value=0.0)
    stock=st.number_input("Opening stock",min_value=0,step=1)
    moq=st.number_input("MOQ",min_value=1,step=1,value=1)
    hs=st.text_input("Candidate HS Code")
    if st.form_submit_button("Add Product") and name:
        execute("""INSERT INTO products(company_id,name,sku,price,stock,moq,hs_code)
                   VALUES(1,?,?,?,?,?,?)""",(name,sku,price,stock,moq,hs))
        st.success("Product added.")

rows=execute("SELECT id,name,sku,price,currency,moq,stock,hs_code FROM products ORDER BY id DESC",fetch=True)
st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)
st.caption("HS Code suggestions are assistance only; verify official customs classification.")

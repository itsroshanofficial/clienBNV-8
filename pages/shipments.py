import streamlit as st
from utils.calculators import cbm
from utils.helpers import page_header

page_header("Shipments & CBM Planner","Shipment tracking and free local packing calculations")

c1,c2,c3,c4=st.columns(4)
with c1: l=st.number_input("Length (cm)",min_value=0.0)
with c2: w=st.number_input("Width (cm)",min_value=0.0)
with c3: h=st.number_input("Height (cm)",min_value=0.0)
with c4: q=st.number_input("Quantity",min_value=1,step=1,value=1)

if st.button("Calculate CBM"):
    st.metric("Total CBM",f"{cbm(l,w,h,q):.3f} m³")

st.divider()
st.text_input("Tracking number")
st.selectbox("Shipment status",["Order Confirmed","Production","Ready to Ship","Booked","Shipped","In Transit","Delivered"])
st.caption("Connect a real carrier/forwarder API later if needed.")

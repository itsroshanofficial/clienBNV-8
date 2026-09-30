import streamlit as st
from database.database import execute
from utils.helpers import page_header,to_dataframe

page_header("Activity & Audit Log","Security and accountability history")

rows=execute("SELECT * FROM audit_logs ORDER BY id DESC LIMIT 200",fetch=True)
if rows:
    st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)
else:
    st.info("No audit events yet.")

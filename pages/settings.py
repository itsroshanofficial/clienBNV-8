import streamlit as st
from database.database import execute
from utils.helpers import page_header

page_header("Settings & Company","Company profile, team, integrations and subscription")

st.subheader("Company")
company=execute("SELECT * FROM companies WHERE id=1",fetch=True)
if company:
    c=dict(company[0])
    st.text_input("Company name",c["name"])
    st.text_input("Country",c["country"] or "")
    st.text_input("Company email",c["email"] or "")

st.subheader("Subscription")
st.info("Planned tiers: Free • Pro • Business")
st.caption("Production subscription enforcement must happen server-side, not only by hiding frontend controls.")

st.subheader("Integrations")
st.checkbox("Local/Open-source AI")
st.checkbox("Email provider")
st.checkbox("OIDC authentication")
st.checkbox("Hosted PostgreSQL")
st.warning("Never place API keys, passwords or OAuth secrets directly in source code.")

import streamlit as st
from ai.email_writer import write_email
from database.database import execute
from utils.helpers import page_header

page_header("Campaigns & AI Email Writer", "Create professional outreach without requiring a paid AI API")

left,right=st.columns([1,1])
with left:
    context=st.text_area("What do you want to communicate?", height=180,
        placeholder="Introduce our products to a new international buyer...")
    tone=st.selectbox("Tone",["Professional","Friendly","Short","Follow-up","Sales Introduction","Formal"])
    language=st.selectbox("Language",["English","Urdu","Arabic","Spanish","German","French"])
    if st.button("✨ Generate AI Email",use_container_width=True):
        st.session_state["generated_email"]=write_email(context,tone,language)

with right:
    st.subheader("Generated Draft")
    st.text_area("Subject & Body",st.session_state.get("generated_email",""),height=300)

st.divider()
st.subheader("Campaigns")
with st.form("campaign"):
    name=st.text_input("Campaign name")
    subject=st.text_input("Campaign subject")
    if st.form_submit_button("Create Campaign") and name:
        execute("INSERT INTO campaigns(company_id,name,subject) VALUES(1,?,?)",(name,subject))
        st.success("Campaign created.")

import streamlit as st
from ai.reply_assistant import classify_reply, draft_reply
from utils.helpers import page_header

page_header("Inbox & Reply Intelligence", "Analyze business replies and prepare responses")

thread=st.text_area("Paste or connect an email conversation",height=230,
    placeholder="Paste the conversation here for the local demo...")
if st.button("Analyze Reply"):
    if thread:
        st.session_state["reply_category"]=classify_reply(thread)
        st.session_state["reply_draft"]=draft_reply(thread)

if "reply_category" in st.session_state:
    st.success("Classification: " + st.session_state["reply_category"])
    st.text_area("AI Suggested Reply",st.session_state["reply_draft"],height=220)
    st.caption("Review and edit AI-generated messages before sending.")

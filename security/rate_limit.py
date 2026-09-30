import time
import streamlit as st

def allow(key, seconds=2):
    now = time.time()
    previous = st.session_state.get(f"rate_{key}", 0)
    if now - previous < seconds:
        return False
    st.session_state[f"rate_{key}"] = now
    return True

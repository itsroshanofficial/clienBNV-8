import streamlit as st
from database.database import execute, scalar

def ensure_demo_user():
    if scalar("SELECT COUNT(*) FROM companies") == 0:
        company_id = execute(
            "INSERT INTO companies(name,country,email) VALUES(?,?,?)",
            ("Demo Export Company", "Pakistan", "demo@example.com")
        )
        execute(
            "INSERT INTO users(company_id,name,email,role) VALUES(?,?,?,?)",
            (company_id, "Demo Admin", "demo@example.com", "admin")
        )

def current_user():
    return {
        "id": 1,
        "company_id": 1,
        "name": "Demo Admin",
        "email": "demo@example.com",
        "role": "admin",
    }

def login(email):
    rows = execute(
        "SELECT id,company_id,name,email,role FROM users WHERE email=?",
        (email,), fetch=True
    )
    if rows:
        user = dict(rows[0])
        st.session_state["user"] = user
        return user
    return None

def logout():
    st.session_state.pop("user", None)

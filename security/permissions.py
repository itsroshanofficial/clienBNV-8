import streamlit as st
from database.auth import current_user

def require_login():
    # Demo mode intentionally allows local development.
    # Replace this with OIDC/backend authentication before production.
    return True

def user_can(role, allowed):
    return role in allowed

def company_id():
    user = current_user()
    return user["company_id"] if user else None

import streamlit as st
from database.database import init_db, get_setting
from database.auth import ensure_demo_user, current_user
from security.permissions import require_login

st.set_page_config(
    page_title="ClientFlow AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()
ensure_demo_user()

# Modern Streamlit multipage navigation.
pages = [
    st.Page("pages/dashboard.py", title="Dashboard", icon="📊"),
    st.Page("pages/crm.py", title="CRM", icon="👥"),
    st.Page("pages/leads.py", title="Leads", icon="🎯"),
    st.Page("pages/campaigns.py", title="Campaigns", icon="📨"),
    st.Page("pages/inbox.py", title="Inbox & Reply AI", icon="💬"),
    st.Page("pages/followups.py", title="Follow-ups", icon="✅"),
    st.Page("pages/inventory.py", title="Inventory", icon="📦"),
    st.Page("pages/export_orders.py", title="Export Orders", icon="🚢"),
    st.Page("pages/shipments.py", title="Shipments", icon="🛳️"),
    st.Page("pages/payments.py", title="Payments", icon="💳"),
    st.Page("pages/documents.py", title="Documents", icon="📄"),
    st.Page("pages/image_tools.py", title="Image Studio", icon="🖼️"),
    st.Page("pages/analytics.py", title="Analytics", icon="📈"),
    st.Page("pages/ai_assistant.py", title="AI Assistant", icon="🤖"),
    st.Page("pages/activity.py", title="Activity & Audit", icon="🛡️"),
    st.Page("pages/settings.py", title="Settings", icon="⚙️"),
]

if not current_user():
    st.sidebar.info("Demo mode: local development")
else:
    st.sidebar.success(f"Signed in as {current_user()['name']}")

st.sidebar.caption("ClientFlow AI")
st.sidebar.caption("AI-powered business & export intelligence")

pg = st.navigation(pages)
pg.run()

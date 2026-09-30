import pandas as pd
import streamlit as st

def page_header(title, subtitle=""):
    st.title(title)
    if subtitle:
        st.caption(subtitle)

def kpi(label, value, help_text=None):
    st.metric(label, value, help=help_text)

def df_download(df, filename="export.csv"):
    st.download_button(
        "Download CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name=filename,
        mime="text/csv"
    )

def to_dataframe(rows):
    return pd.DataFrame([dict(r) for r in rows])

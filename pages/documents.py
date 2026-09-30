import streamlit as st
from pathlib import Path
from security.validation import safe_filename
from utils.helpers import page_header,to_dataframe
from database.database import execute

UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

page_header("Documents & Document Vault","Store business documents by type and order")

dtype=st.selectbox("Document type",["Quotation","Proforma Invoice","Commercial Invoice","Packing List","Proposal","Sales Contract","Shipment Document","Other"])
order=st.number_input("Order ID",min_value=0,step=1)
file=st.file_uploader("Upload document",type=["pdf","png","jpg","jpeg","docx","xlsx"])
if file and st.button("Save Document"):
    name=safe_filename(file.name)
    path=UPLOAD_DIR/name
    path.write_bytes(file.getbuffer())
    execute("INSERT INTO documents(company_id,name,document_type,order_id,file_path) VALUES(1,?,?,?,?)",
            (name,dtype,order,str(path)))
    st.success("Document saved.")

rows=execute("SELECT * FROM documents ORDER BY id DESC",fetch=True)
st.dataframe(to_dataframe(rows),use_container_width=True,hide_index=True)
st.warning("Compliance-sensitive documents should be reviewed before official use.")

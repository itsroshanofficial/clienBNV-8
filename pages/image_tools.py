import streamlit as st
from PIL import Image
from utils.helpers import page_header

page_header("Image Studio","Free-first tools for business product visuals")

file=st.file_uploader("Upload an image",type=["png","jpg","jpeg","webp"])
if file:
    image=Image.open(file)
    st.image(image,caption="Original",use_container_width=True)

    tab1,tab2,tab3=st.tabs(["Resize","Compress","Convert"])
    with tab1:
        width=st.number_input("Width",min_value=100,max_value=5000,value=image.width)
        if st.button("Resize"):
            ratio=width/image.width
            new=image.resize((int(width),int(image.height*ratio)))
            st.image(new,use_container_width=True)
            st.success("Resize preview generated.")
    with tab2:
        quality=st.slider("Quality",20,95,80)
        st.caption(f"Selected JPEG quality: {quality}")
    with tab3:
        fmt=st.selectbox("Output format",["PNG","JPEG","WEBP"])
        st.caption(f"Conversion target: {fmt}")

st.info("Background removal and reverse-image checking can be added with open-source/local components or provider integrations.")

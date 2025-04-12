import streamlit as st

# Set page title
st.set_page_config(page_title="Amul Distributor",page_icon="🍫", layout="wide")

# Header
st.markdown("<h1 style='text-align: center;'>Amul Products Distributor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Punam Uphar Gruha, Sangadi-Bhandara-Maharashtra</h3>", unsafe_allow_html=True)

# Columns Layout
col1, col2 = st.columns(2)

# Column 1: Contact Info
with col1:
    st.header("Contact Details")
    st.markdown("📧 Email: **yrahele@gmail.com**")
    st.markdown("📍 Location: Sangadi, Bhandara, Maharashtra")
    st.markdown("📞 Phone: +91 8329312092") 
    st.markdown("<h4 style='text-align: center;'><a href='https://maps.app.goo.gl/WoczdLAzxdD7T3Bw5?g_st=awb' target='_blank'>📍 View Location on Google Maps</a></h4>", unsafe_allow_html=True)

# Column 2: About Business
with col2:
    st.header("Our Products")
    st.markdown("✅ **Dairy Products** (Amul)")
    st.markdown("✅ **Chocolates & Confectionery** (Cadbury, Lotte, Perfetti)")
    st.markdown("✅ **Wholesale Distribution Services**")
    st.image("https://source.unsplash.com/600x300/?chocolates", caption="Quality Products")  # You can replace the image URL

# Footer
st.write("---")
st.markdown("© 2025 Punam Uphar Gruha | All Rights Reserved")


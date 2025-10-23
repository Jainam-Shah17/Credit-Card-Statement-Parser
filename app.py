import streamlit as st
import pdfplumber
import re
import json
from parser import parse_statement, BANK_PATTERNS

def extract_text_from_pdf(pdf_source):
    try:
        with pdfplumber.open(pdf_source) as pdf:
            first_page = pdf.pages[0]
            return first_page.extract_text()
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

st.set_page_config(
    layout="wide",
    page_title="Credit Card Statement Parser",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    h1, h2, h3, h4 {
        margin-bottom: 0.5rem;
    }
    .stMetric {
        background-color: #262730;
        padding: 10px 5px;
        border-radius: 8px;
    }
    .stTextInput, .stFileUploader {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("💳 Credit Card Statement Parser")

uploaded_file = st.file_uploader(
    "Upload your PDF statement",
    type=["pdf"],
    label_visibility="collapsed"
)

if uploaded_file is not None:
    full_text = extract_text_from_pdf(uploaded_file)

    if full_text:
        parsed_data = parse_statement(full_text, BANK_PATTERNS)

        st.markdown("### 📋 Extracted Details")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🏦 Bank", parsed_data.get("bank_name", "N/A"))
        col2.metric("💳 Last 4 Digits", parsed_data.get("card_last_4", "N/A"))
        col3.metric("📅 Due Date", parsed_data.get("due_date", "N/A"))

        total_due = parsed_data.get("total_due", 0.0)
        col4.metric("💰 Total Due", f"₹{total_due:,.2f}")

        st.divider()

        st.markdown(f"""
        **Statement Date:** {parsed_data.get('statement_date', 'N/A')}  
        **Statement Period:** {parsed_data.get('statement_period', 'N/A')}
        """)

        with st.expander("🧾 View Extracted Text (optional)"):
            st.text_area("Extracted PDF Text", full_text[:2000], height=150)

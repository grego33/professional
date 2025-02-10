import streamlit as st
import markdown2
from weasyprint import HTML

# Streamlit app
st.title("Markdown to PDF Converter")

# Text area for Markdown input
markdown_text = st.text_area("Enter your Markdown text here:")

# Convert Markdown to HTML
html_text = markdown2.markdown(markdown_text)

# Add CSS to ensure emojis are rendered correctly and adjust font size and line height
css = """
    <style>
    @font-face {
        font-family: 'NotoSansEmoji';
        src: url('https://fonts.gstatic.com/s/notosans/v27/o-0IIpQlx3QUlC5A4PNb4j5Ba_2c7A.woff2') format('woff2');
    }
    body {
        font-family: 'NotoSansEmoji', sans-serif;
        font-size: 14px;
        line-height: 1.5;
    }
    </style>
"""

# Combine HTML and CSS
html_with_css = f"{css}{html_text}"

# Convert HTML to PDF and trigger download
if st.button("Generate PDF"):
    pdf = HTML(string=html_with_css).write_pdf()
    st.download_button(label="Download PDF", data=pdf, file_name="output.pdf", mime="application/pdf", key="download")

import streamlit as st
import time
from scrape import (scrape_website, split_dom_content, clean_body_content, extract_body_content)
from parse import parse_with_ollama


st.title('WEB AI: Web Scraping Simplified')


url = st.text_input('Enter a Website URL: ')

if st.button("Scrape Site") and url != "":
    with st.spinner('Scrapping the Website....'):
        time.sleep(0.5)
        result = scrape_website(url)
        body_content = extract_body_content(html_content=result)
        cleaned_content = clean_body_content(body_content=body_content)
        
        st.session_state.dom_content = cleaned_content
        with st.expander("View Dom Content"):
            st.text_area("DOM Content:", cleaned_content, height=300)
        st.success("Done Scrapping..")   
            
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content. This might take a while. Please be patient.")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks=dom_chunks, parse_description=parse_description)
            st.write(result)
        

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from pexel import get_pexels_images
import re

template = """Question: {question}\n\n
            Answer: Please organize each element in briefly sentence."""
prompt = PromptTemplate.from_template(template)
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What are the three key tips for providing information?"

import streamlit as st 
st.title('Infograpic Generator')
st.text("<www.pexels.com> Photos provided by pexels")
st.divider()
query = st.text_input('Input your keyword')

# image generator
api_key = "VL0KDEqt8u4xbbD5Q6GRmg14h2vr9OxSZZvgp3d4UpqsV79VvF9DCy0j"
num_images = st.number_input("Enter the number of images", min_value=1, max_value=5, value=3)


if st.button("Generator"):
    images = get_pexels_images(api_key, query, per_page=num_images)
    result_dict = llm_chain.invoke(query)
    text = result_dict["text"]
    sentences = re.split(r'[.!?]', text)  

   
    for i, (image, sentence) in enumerate(zip(images, sentences)):
        if i < len(images):
            st.image(image, caption=sentence.strip(), width=400)  
            if i < len(images) - 1:
                st.divider()


# Text, Image 따로
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.header("Only Image")
    
    if st.button("Image"):
        images = get_pexels_images(api_key, query, per_page=num_images)
        for image in images:
            st.image(image, use_column_width=True)
    
with col2:
    st.header("Only Text")
    # Text generator

    if st.button('Text'):
        with st.spinner("waiting..."):
            text = llm_chain.invoke(query)
            st.write(text)
        
      


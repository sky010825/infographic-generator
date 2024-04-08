from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from pexel import *
import re
import io
import streamlit as st 

template = """Question: {question}\n\n
            Answer: Please organize each element in briefly sentence. """
prompt = PromptTemplate.from_template(template)
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What are the three key tips for providing information?"


st.title('Infograpic Generator')
st.text("<www.pexels.com> Background Photos provided by pexels")
st.divider()
# 키워드 입력
query = st.text_input('Input your keyword')

# image generator
api_key = "VL0KDEqt8u4xbbD5Q6GRmg14h2vr9OxSZZvgp3d4UpqsV79VvF9DCy0j"
num_images = st.number_input("Enter the number of images", min_value=1, max_value=5, value=3)

#text generator
result_dict = llm_chain.invoke(query)
text = result_dict["text"]
sentences = re.split(r'[.!?]', text)

if st.button("Generator"):
    # images = get_pexels_images(api_key, query, per_page=num_images)
    # result_dict = llm_chain.invoke(query)
    # text = result_dict["text"]
    # sentences = re.split(r'[.!?]', text)  

    # for image, sentence in zip(images, sentences):
    #     st.image(image, caption=sentence.strip(), width=400)  
    #     if num_images > 1:
    #         st.divider()
    


    images = apply_box_to_images(api_key, query, per_page=num_images)

    for i, image in enumerate(images):
        st.image(image, use_column_width=True)
        
        # 이미지를 파일로 저장하여 이진 데이터 가져옴
        image_file = io.BytesIO()
        image.save(image_file, format='JPEG')
        image_data = image_file.getvalue()  
        
        # 각 이미지에 대한 다운로드 버튼
        download_button_label = f"Download Image {i+1}"
        st.download_button(label=download_button_label, data=image_data, file_name=f"image_{i+1}.jpg")


# # Text, Image 따로
# st.divider()
# col1, col2 = st.columns(2)

# with col1:
#     st.header("Only Image")
    
#     if st.button("Image"):
#         images = get_pexels_images(api_key, query, per_page=num_images)
#         for image in images:
#             st.image(image, use_column_width=True)
    
# with col2:
#     st.header("Only Text")
#     # Text generator
#     if st.button('Text'):
#         with st.spinner("waiting..."):
#             text = llm_chain.invoke(query)
#             st.write(text)
        
      


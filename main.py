# from sysmov import path
# path.create_path()

import streamlit as st
# from create import image as img_module
# from create import text
# from create import templates as temp

# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
import io
import time
import requests
import os
from template import *
from text import *


# 로그인 상태 확인 및 초기화
if 'login_nickname' not in st.session_state:
    st.session_state['login_nickname'] = 'Unknown'

if 'login_successful' not in st.session_state:
    st.session_state['login_successful'] = False

login_nickname = st.session_state.login_nickname
login_successful = st.session_state.login_successful



def main():
    st.title('Infographic Generator :frame_with_picture:')
    # st.write('Welcome! ' + login_nickname)
    st.text("<www.pexels.com> Background Photos provided by pexels")
    st.divider()

    if 'slides' not in st.session_state:
        st.session_state['slides'] = []

    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = {}

    inputform()

    for i in range(len(st.session_state.slides)):
        slide = st.session_state.slides[i]

        #텍스트 할당
        input_text = slide['text']
        text_list = text_parser(input_text)
        st.write(text_list)
        text = {'title': ' ', 'subtext1': '', 'subtext2': '', 'subtext3': '', 'subtext4': '', 'subtext5': ''}
        keys = list(text.keys())
        for k, value in enumerate(text_list):
            if k < len(keys):
                text[keys[k]] = str(value)

        #템플릿 선정
        overlay_image = None
        if slide['text']:
            if st.session_state.num_inputs==1:
                selected_template = '1'
                st.write("템플릿 " + selected_template)
            else:
                selected_template = template_num(slide['text'])
                st.write("템플릿 " + selected_template)

                
            # 선택된 템플릿에 따라 overlay_image를 생성
            if '1' in selected_template :
                overlay_image = temp1(text['title'], text['subtext1'], text['subtext2'])
            elif '2' in selected_template :
                overlay_image = temp2(text['title'], text['subtext1'], text['subtext2'])
            elif '3' in selected_template :
                overlay_image = temp3(text['title'], text['subtext1'], text['subtext2'])
            elif '4' in selected_template :
                overlay_image = temp4(text['title'], text['subtext1'], text['subtext2'])
            
            if overlay_image: 
                image_byte_array = overlay_image.save("output.jpg")
                st.image(image_byte_array)
                st.download_button(label=f"다운로드 {i+1}", data=image_byte_array, file_name=f"image_{i+1}.jpg")

def inputform():
    add_input = st.button("추가")
    if 'num_inputs' not in st.session_state:
        st.session_state.num_inputs = 0

    if add_input:
        st.session_state.num_inputs += 1

    with st.form("form"):
        for i in range(st.session_state.num_inputs):
            slide_text = st.text_input(f"슬라이드 {i+1} 문장", key=f"text_{i}")

            if i < len(st.session_state.slides):
                st.session_state.slides[i] = {'text': slide_text}
            else:
                st.session_state.slides.append({'text': slide_text})

        submit = st.form_submit_button("생성")
        if submit:
            with st.spinner('Wait for it...'):
                time.sleep(5)

if __name__ == "__main__":
    main()

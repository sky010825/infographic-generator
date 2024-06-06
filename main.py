# from sysmov import path
# path.create_path()

import streamlit as st
# from create import image as img_module
# from create import text
import template as temp
import io
import time
import requests
import os
# from template import *
from image import *
import text as txt
import random


# 로그인 상태 확인 및 초기화
if 'login_nickname' not in st.session_state:
    st.session_state['login_nickname'] = 'Unknown'

if 'login_successful' not in st.session_state:
    st.session_state['login_successful'] = False

login_nickname = st.session_state.login_nickname
login_successful = st.session_state.login_successful

options = None

def main():
    st.title('Infographic Generator :frame_with_picture:')
    # st.write('Welcome! ' + login_nickname)
    st.text("<www.pexels.com> Background Photos provided by pexels")
    st.divider()

    if 'slides' not in st.session_state:
        st.session_state['slides'] = []

    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = {}
    
    options = st.selectbox("템플릿 컨셉",  ["따뜻하게", "시원하게", "화사하게", "단조롭게", "신비롭게", "직접 입력"])
    if options=="직접 입력":
        options = st.text_input("템플릿 컨셉 직접 입력")

    st.divider()
    inputform()

    
    #### GENERATE ####
    for i in range(len(st.session_state.slides)):
        slide = st.session_state.slides[i]

        #템플릿 선정
        overlay_image = None
        if slide['text']:

            #텍스트 할당
            input_text = slide['text']
            text_list = txt.text_parser(input_text)
            text = {'title': ' ', 
                    'subtext1': ' ', 
                    'subtext2': ' ', 
                    'subtext3': ' ', 
                    'subtext4': ' ', 
                    'subtext5': ' '}
            keys = list(text.keys())
            for k, value in enumerate(text_list):
                if k < len(keys):
                    text[keys[k]] = str(value)
            
            #Color Pallete
            colNumber = temp.colorNumber(options)
            st.write("선택된 컬러 팔레트 = ", colNumber)


            #Template Slide 
            if st.session_state.num_inputs==1:
                st.write("슬라이드가 1개이므로 content 템플릿에서 랜덤으로 결정")
            
                args = {
                    "title": text['title'],
                    "sub1": txt.sub_title(text['subtext1']),
                    "sub2": txt.sub_title(text['subtext2']),
                    "sub3": txt.sub_title(text['subtext3']),
                    "ct1": text['subtext1'],
                    "ct2": text['subtext2'],
                    "ct3": text['subtext3'],
                    "label": text['subtext4'],
                    "colorNumber": colNumber
                }
                temp_set = [temp.content1, temp.content2, temp.content3, temp.content4]
                random_index = random.randint(0,3)
                overlay_image = temp_set[random_index](**args)
                
            else:
                st.write("슬라이드가 2개 이상이므로 set에서 고르거나 cover+content조합으로")
                # temp = [[book1(), book2()], [note1(), note2(), note3()], [post_it1(), post_it2(), post_it3(), post_it4()], [cover1]]
                # random_temp = random.choice(temp)

                

            # 결과 및 다운로드
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

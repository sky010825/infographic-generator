import streamlit as st
from image import *
from text import *
import io
import time

def main():
    st.title('Infographic Generator :frame_with_picture:')
    st.text("<www.pexels.com> Background Photos provided by pexels")
    st.divider()

    if 'slides' not in st.session_state:
        st.session_state.slides = []
    
    #input form
    inputform()
    
    #슬라이드 결과 보여주기
    for i in range(len(st.session_state.slides)):
        if(st.session_state.slides[i]['query']):
            image = overlay_image(st.session_state.slides[i]['query'], st.session_state.slides[i]['text'])
            st.image(image, width=600)
            st.download_button(f"다운로드{i+1}", data=image, file_name=f"image{i+1}.jpg")




def inputform():
    add_input = st.button("추가")
    if 'num_inputs' not in st.session_state:
            st.session_state.num_inputs = 0
    if add_input:
        st.session_state.num_inputs += 1

    with st.form("form"):
        for i in range(st.session_state.num_inputs):
            query = st.text_input(f"슬라이드 {i+1} 이미지", key=f"image_keyword_{i}")
            text = st.text_input(f"슬라이드 {i+1} 문장", key=f"text_{i}")

            if i < len(st.session_state.slides):
                st.session_state.slides[i] = {'query': query, 'text': text}
            else:
                st.session_state.slides.append({'query': query, 'text': text})
                
        submit = st.form_submit_button("생성")
        if submit:
            with st.spinner('Wait for it...'):
                time.sleep(5)
                    

if __name__ == "__main__":
    main()

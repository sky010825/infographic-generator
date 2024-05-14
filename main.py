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
    
    if 'button_clicked' not in st.session_state:
            st.session_state.button_clicked = {}

    #input form
    inputform()

    #슬라이드 결과 보여주기
    for i in range(len(st.session_state.slides)):
        image = overlay_image(st.session_state.slides[i]['query'], st.session_state.slides[i]['text'])
        st.image(image)




def inputform():
    add_input = st.button("추가")
    if 'num_inputs' not in st.session_state:
            st.session_state.num_inputs = 0

    if add_input:
        st.session_state.num_inputs += 1

    with st.form("form"):
        inputs = []
        for i in range(st.session_state.num_inputs):
            query = st.text_input(f"슬라이드 {i+1} 이미지", key=f"image_keyword_{i}")
            inputs.append(query)

            text = st.text_input(f"슬라이드 {i+1} 문장", key=f"text_{i}")
            inputs.append(text)

        submit = st.form_submit_button("생성")
        if submit:
            for i in range(st.session_state.num_inputs):
                query_key = f"image_keyword_{i}"
                text_key = f"text_{i}"
                query = st.session_state[query_key]
                text = st.session_state[text_key]
                st.session_state.slides.append({'query': query, 'text': text})

            with st.spinner('Wait for it...'):
                time.sleep(5)
            


def download(image, n):
    for i, image in enumerate(image):
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format='JPEG')
        image_data = image_byte_array.getvalue()
        st.download_button(label=f"다운로드 {i+n+1}", data=image_data, file_name=f"image_{i+n+1}.jpg")

if __name__ == "__main__":
    main()

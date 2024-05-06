import streamlit as st 
from image import *
from text import *
import io

def main():
    # Streamlit Project 제목
    st.title('Infograpic Generator 	:frame_with_picture:')
    st.text("<www.pexels.com> Background Photos provided by pexels")
    st.divider() 
    
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = {}
    
    if 'slides' not in st.session_state:
        st.session_state.slides = []
    

    # 추가
    with st.form(key="form"):
        query = st.text_input('배경 키워드')
        txt = st.text_input('text text text')
        submit = st.form_submit_button(':heavy_plus_sign:')
        if submit:
            if not query:
                st.error("배경 키워드를 입력하세요.")
            else:
                st.session_state.slides.append({'query':query,'txt':txt})
    
    # 슬라이드 
    for i in range(len(st.session_state.slides)):
        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            image = make(st.session_state.slides[i]['query'], st.session_state.slides[i]['txt'])
            st.image(image)

        with col2:
            #삭제버튼
            delete_button = st.button(label="삭제", key=i)
            if delete_button:
                del st.session_state.slides[i]
                st.rerun()
            
            #다운로드 버튼
            download(image, i)  







def download(image, n):
    for i, image in enumerate(image):
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format='JPEG')
        image_data = image_byte_array.getvalue() 
        st.download_button(label=f"다운로드 {i+n+1}", data=image_data, file_name=f"image_{i+n+1}.jpg")


if __name__ == "__main__":
    main()

    

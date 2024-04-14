import streamlit as st 
from image import *
from text import *
import io

def main():
    # Streamlit Project 제목
    st.title('Infograpic Generator')
    st.text("<www.pexels.com> Background Photos provided by pexels")
    num_images = st.number_input("Enter the number of images", min_value=1, max_value=5, value=3)
    st.divider() 
    
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = {}
    
    
    for i in range(1, num_images+1):
        col1, col2 = st.columns([3,7])
        with col1:  
            query = st.text_input(f'background keyword {i}')
            txt = st.text_input(f'text keyword {i}')
            
        with col2:
            if st.button(f"Make {i}", key=f"make_button_{i}"):
                st.session_state.button_clicked[f"make_button_{i}"]=True
                make(query, txt) 
            else:
                st.session_state.button_clicked[f"make_button_{i}"]=False
        st.divider()
      


def make(query, txt):
    num_images = 1
    api_key = "VL0KDEqt8u4xbbD5Q6GRmg14h2vr9OxSZZvgp3d4UpqsV79VvF9DCy0j" ##Input your API KEY 
    images = apply_box_to_images(api_key, query, txt, per_page=num_images)
        
    for i, image in enumerate(images):
        st.image(image, width=400)   #이미지 띄우기
    
        # 다운로드 버튼
        image_file = io.BytesIO()
        image.save(image_file, format='JPEG')
        image_data = image_file.getvalue()  
        download_button_label = f"Download Image"
        st.download_button(label=download_button_label, data=image_data, file_name=f"image_{i+1}.jpg")


if __name__ == "__main__":
    main()

    

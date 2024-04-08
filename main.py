import streamlit as st 
from image import *
from text import *
import io

def main():
    # Streamlit Project 제목
    st.title('Infograpic Generator')
    st.text("<www.pexels.com> Background Photos provided by pexels")
    st.divider()
    
    api_key = "VL0KDEqt8u4xbbD5Q6GRmg14h2vr9OxSZZvgp3d4UpqsV79VvF9DCy0j"   ## "www.pexel.com" API KEY
    
    # 초기 입력
    query = st.text_input('Input your keyword')
    num_images = st.number_input("Enter the number of images", min_value=1, max_value=5, value=3)

    if st.button("Make"):
        images = apply_box_to_images(api_key, query, per_page=num_images)
          
        for i, image in enumerate(images):
            st.image(image, width=400)   #이미지 띄우기
        
            # 다운로드 버튼
            image_file = io.BytesIO()
            image.save(image_file, format='JPEG')
            image_data = image_file.getvalue()  
            download_button_label = f"Download Image {i+1}"
            st.download_button(label=download_button_label, data=image_data, file_name=f"image_{i+1}.jpg")


if __name__ == "__main__":
    main()

    

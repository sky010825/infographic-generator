import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import streamlit as st 
from text import *

def get_pexels_images(api_key, query, per_page):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
    headers = {"Authorization": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    images = [photo['src']['original'] for photo in data['photos']]
    return images

# @st.cache_data ?
def apply_box_to_images(api_key, query, per_page):
    images = get_pexels_images(api_key, query, per_page)
    modified_images = []
    
    ## 텍스트 연동
    sentence = text_generator(query)
    
    for i, image_url in enumerate(images):
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((400,400))
        width, height = image.size
        
        # 텍스트 배경 박스
        draw = ImageDraw.Draw(image)
        box_width = int(width * 0.8) 
        box_height = int(height * 0.5) 
        box_x = (width - box_width) // 2
        box_y = (height - box_height) // 2
        fill_color = (255, 255, 255, 200)  # 불투명도 적용안됨 
        draw.rectangle([box_x, box_y, box_x + box_width, box_y + box_height], fill=fill_color)  
        
        #텍스트
        if i < len(sentence):  
            text = sentence[i]
        else:
            text = "" 
        
        #텍스트 크기, 글꼴
        font_size = 20
        font = ImageFont.truetype("NanumGothic.ttf", font_size)
        # 텍스트 위치 
        text_x = box_x      
        text_y = box_y 
        
        draw.text((text_x, text_y), text, font=font, fill='black') 
        modified_images.append(image)
        
    return modified_images
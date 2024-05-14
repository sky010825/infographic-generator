import streamlit as st 
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from text import *
import random
import io

def overlay_image(query, text):
    api_key = "W6rmGVFPuxMtYvqhUUtWnNHpMV1OD9AMrpt9G9NfSZ4Ido1Nwc6AZ6RQ" ##Input your API KEY             
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={1}"
    headers = {"Authorization": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    images_url = [photo['src']['original'] for photo in data['photos']]
    
    text = text_generator(text)
    overlay_image = TextOverlayImage(io.BytesIO(requests.get(images_url[0]).content))
    overlay_image.add_text_box(text, 50, 50, (255, 0, 0), (255, 255, 255), font_size=200)
    image_byte_array = overlay_image.save("output.jpg")
    return image_byte_array

class TextOverlayImage:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)
        self.text_boxes = []

    def add_text_box(self, text, x, y, text_color, box_color, font_path="NanumGothic.ttf", font_size=20):
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getlength(text)
        _, text_height = font.getbbox(text)[2:]
        box_left = x
        box_top = y
        box_right = x + text_width
        box_bottom = y + text_height

        # 텍스트 상자 그리기
        self.draw.rectangle([(box_left, box_top), (box_right, box_bottom)], fill=box_color)

        # 텍스트 그리기
        self.draw.text((x, y), text, font=font, fill=text_color)

        # 텍스트 상자와 텍스트를 하나의 객체로 저장
        text_box = {
            "text": text,
            "box": [(box_left, box_top), (box_right, box_bottom)],
            "text_color": text_color,
            "box_color": box_color,
            "font": font,
            "font_size": font_size
        }
        self.text_boxes.append(text_box)

    # def save(self, output_path):
    #     self.image.save(output_path)
    def save(self, output_path):
        byte_io = io.BytesIO()
        self.image.save(byte_io, format='JPEG')
        byte_array = byte_io.getvalue()
        return byte_array

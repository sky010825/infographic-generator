from dotenv import load_dotenv
load_dotenv()

import image as img_module
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import re
from text import *


# Template_AI
def colorNumber(options):
    colorNumber_template = PromptTemplate.from_template(
    """
    You are the AI that chooses Color Pallette Number.
    Choose the color palette associated with the entered {text} from the color set and return the number. 
    
    ColorSet = [
        [(255, 166, 248), (196, 49, 184), (125, 0, 115)], # 완전 보라   =>   0
        [(227, 191, 255), (146, 87, 194), (59, 18, 92)], # 자색 계열     =>   1
        [(202, 214, 250), (84, 114, 209), (7, 28, 89)], # 파랑 계열       =>  2
        [(204, 237, 255), (68, 138, 166), (37, 50, 89)], # 파랑 계열    =>    3
        [(186, 235, 255), (61, 169, 212), (16, 94, 125)], # 푸른 계열   =>    4
        [(194, 255, 255), (44, 199, 199), (6, 117, 117)], # 미쿠 색감   =>    5
        [(163, 255, 203), (72, 196, 126), (9, 110, 53)], # 녹색 계열(푸른)  =>  6
        [(218, 255, 181), (129, 196, 63), (48, 97, 0)], # 녹색 계열      =>    7
        [(254, 255, 184), (217, 219, 64), (126, 128, 10)], # 확실한 노랑 =>   8
        [(242, 238, 228), (250, 213, 122), (168, 120, 0)], # 노랑 계열   =>   9
        [(255, 212, 171), (255, 153, 55), (101, 61, 22)], # 주황 계열    =>   10
        [(255, 212, 201), (222, 103, 73), (110, 29, 9)], # 주홍 계열     =>   11
        [(247, 201, 212), (201, 71, 102), (122, 17, 42)], # 체리 색감    =>   12
        [(255, 181, 181), (237, 83, 83), (156, 0, 0)], # 빨간 맛         =>   13
    ]
    
    The output must return only a number, an integer between 0 and 13.
    """,
    )
    llm = OpenAI(temperature=0)
    result = llm(colorNumber_template.format(text=options))
    number_match = re.search(r'\d+', result)
    if number_match:
        color_number = int(number_match.group())
        if 0 <= color_number <= 13:
            return color_number


## 이 밑으론 같음 
RED     =   (255, 0, 0)
GREEN   =   (0, 255, 0)
BLUE    =   (0, 0, 255)
BLACK   =   (0, 0, 0)
WHITE   =   (255, 255, 255)

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import re

# Template 
template = """당신은 카드뉴스에 들어갈 문장을 만드는 AI입니다. 다음 텍스트에서 카드뉴스의 요소 뒤 내용을 추출하여 '/' 로 구분된 형태로 반환해주세요.
요소는 제목, 일시, 신청기간, 비용, 장소, 세부사항 등이 존재합니다.

텍스트: {text}

출력 형식: {output_format}

예시:
입력 텍스트: "제목은 대동제 날짜는 5월30일 시간은 18시부터"
출력: "대동제 / 5월30일 / 18시"
"""

prompt = PromptTemplate(
    input_variables=["text", "output_format"],
    template=template,
)
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)


def text_generator(text):
    input_text = text
    output_format = "제목 / 일시 / 시간 "
    result = llm_chain.run(text=input_text, output_format=output_format)
    return result

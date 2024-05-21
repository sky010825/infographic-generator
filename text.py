from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Template 
prompt_template = PromptTemplate.from_template(
"""
당신은 문장을 추출하는 AI입니다. 다음 텍스트에서 문장의 요소를 출력해주세요.
요소는 제목, 일시, 신청기간, 비용, 장소, 세부사항 등이 존재합니다.

You are an AI assistant that extracts key information from text related to events or programs.
and Please organize the input text in the order of importance.
Only include the relevant fields based on the input text. If a field is not mentioned, leave it out.

텍스트: {text}


예시1:
Input: "제목은 대동제 날짜는 5월30일 시간은 18시부터 장소는 대운동장"
Output: 대동제, 5월30일, 18시, 대운동장

예시2:
Input: "5월 20일 오후4시에 팔정도에서 불교박람회가 개최됩니다"
Output: 불교박람회, 5월20일, 오후4시, 팔정도

"""
)


llm = OpenAI()

def text_generator(input_text):
    result = llm(prompt_template.format(text=input_text))
    return result

# def map_categories(result):
#     category_mapping = {
#         "제목": "1",
#         "장소": "2",
#         "일시": "2",
#         "기간": "2",
#         "비용": "3",
#         "세부사항": "3"
#     }
#     mapped_result = []
#     for item in result:
#         category = item[0]
#         value = item[1]
#         mapped_value = category_mapping.get(category, 3)

#         if mapped_value is not None:
#             mapped_result.append([mapped_value, value])
#     return mapped_result  

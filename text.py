from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()


output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

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

def text_output(input_text):
    output = text_generator(input_text)
    result = output_parser(output)
    return result[0]


# PEXEL_SEARCH
prompt_template_pexel = PromptTemplate.from_template(
"""
You are the AI that chooses keywords. 
Please print out the word that most closely relates to the entered sentence from below. 
You must only print out the spelling of that word.

word list: ["forest", "school", "book", "coding" , "contest" , "sea",
"school", "teacher", "student", "classroom", "homework", "lesson", 
"subject", "exam", "grade", "textbook", "notebook", "desk", "chair", 
"blackboard", "chalk", "pen", "pencil", "eraser", "ruler", "library", "laboratory",
"playground", "principal", "schedule", "recess", "uniform", "quiz", "report card", "assignment", 
"assembly", "bell", "cafeteria", "classmate", "course", "curriculum", "diploma", "education", "field trip", 
"graduation", "hallway", "holiday", "kindergarten", "lecture", "locker", "lunch", "math", "music", "notebook", "office", 
"paper", "parent-teacher meeting", "project", "quiz", "recess", "reference book", "registration", "report", "research", "school bus", 
"school trip", "science", "semester", "sports day", "staff", "study", "subject", "substitute teacher", "syllabus", "timetable", "tuition",
"vacation", "whiteboard", "worksheet", "yearbook", "assignment", "biology", "chemistry", "class president", "computer lab", "dictionary", 
"drama", "drawing", "English", "exam results", "extracurricular", "geography", "geometry", "history", "home economics", "language", "literature", 
"mathematics", "physical education", "physics", "principal's office", "quiz", "reading", "science fair", "spelling", "student council", "teacher's lounge", 
"timetable", "writing", "advisor", "alumni", "campus tour", "commencement", "course load", "coursework", "curriculum", "dean", "department chair", 
"dining hall", "dorm room", "elective", "exchange student", "extracurricular activities", "faculty meeting", "fellowship", "fraternity", "graduate student", 
"honors program", "lecture series", "lecture theatre", "major advisor", "orientation week", "peer review", "postgraduate", "prerequisite", "provost", "resident assistant", 
"scholarship application", "senior", "sophomore", "student activities", "student center", "student ID", "student organization", "study abroad", "summerschool", "syllabus week", 
"teaching assistant", "tenure", "undergraduate", "university council", "university policy", "work-study program",
]

텍스트: {text}


예시1:
Input: 불교 기념 등산 대회
Output: forest

예시2:
Input: 공과대학 코딩테스트 개최
Output: coding
"""
)
llm = OpenAI()

def pexel_search(input_text):
    result = llm(prompt_template_pexel.format(text=input_text))
    return result 

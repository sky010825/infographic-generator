from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import re

# Template 
template = """Question: {question}\n\n
            Answer: Please organize each element in briefly sentence."""
prompt = PromptTemplate.from_template(template)
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What are the three key tips for providing information?"

def text_generator(query):
    result_dict = llm_chain.invoke(query)
    text = result_dict["text"]
    sentences = re.split(r'[.!?]', text) 
    return sentences



      


      


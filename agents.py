from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser
from tools import web_searching, url_scrapping 
from dotenv import load_dotenv
load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0,
    max_retries=5
)

parser=StrOutputParser()

def search_agent():
    return create_agent(
        model = llm,
        tools = [web_searching]
    )

def reader_agent():
    return create_agent(
        model = llm,
        tools = [url_scrapping]
    )

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write a clear, organised, structured and insightful report"),
    ("human", """Write a detailed research report on the topic below.
    Topic : {topic}
    Research gathered : 
    {research}
    Structure of the report : 
    - Introduction
    - Key findings 
    - Conclusion 
    - Sourcse (list all URLs found in the research)

    Be detailed, factual and professional. """)
])

writer_chain = writer_prompt | llm | parser

critic_prompt = ChatPromptTemplate.from_messages([
    ("system","you are a sharp and constructive research critic. Be extremely honest."),
    ("human", """Review the research report given below and evaluate it strictly.messages
    Report:
    {report}
    Respond in this format : 
    Score : x/10
    Strengths: 
    - ...
    - ...
    Areas of Improvement : 
    - ...
    - ... 
    One line verdict :
    ... """)
])

critic_chain = critic_prompt | llm | parser 

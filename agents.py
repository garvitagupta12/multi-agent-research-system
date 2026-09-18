import time
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from tools import url_scrapping, web_searching

load_dotenv()

# 1. Configure LLM with retries and concurrency throttles
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0,
    max_retries=6,              # Increase backoff attempts for rate limits
    timeout=60,
    max_concurrent_requests=1    # Prevents simultaneous outbound requests
)

parser = StrOutputParser()

# 2. Agent Initialization
search_agent = create_agent(model=llm, tools=[web_searching])
reader_agent = create_agent(model=llm, tools=[url_scrapping])

# 3. Chains
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write a clear, organized, structured and insightful report."),
    ("human", """Write a detailed research report on the topic below.
    Topic : {topic}
    Research gathered : 
    {research}
    Structure of the report : 
    - Introduction
    - Key findings 
    - Conclusion 
    - Sources (list all URLs found in the research)

    Be detailed, factual and professional.""")
])
writer_chain = writer_prompt | llm | parser

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be extremely honest."),
    ("human", """Review the research report given below and evaluate it strictly.
    Report:
    {report}
    Respond in this format : 
    Score : x/10
    Strengths: 
    - ...
    Areas of Improvement : 
    - ... 
    One line verdict :
    ...""")
])
critic_chain = critic_prompt | llm | parser

# 4. Pipeline Execution Node Functions
def run_research_pipeline(topic: str) -> dict:
    print(f"Starting research for topic: {topic}")
    
    # Node 1: Search Agent
    search_response = search_agent.invoke({
        "messages": [HumanMessage(content=f"Find reliable information about: {topic}")]
    })
    time.sleep(2)  # Throttle call to prevent HTTP 429
    
    # Node 2: Reader Agent
    reader_response = reader_agent.invoke({
        "messages": [HumanMessage(content=f"Read and extract details for topic {topic} based on search results: {search_response}")]
    })
    time.sleep(2)  # Throttle call
    
    # Node 3: Writer Chain
    combined_research = f"Search Output:\n{search_response}\n\nReader Output:\n{reader_response}"
    report = writer_chain.invoke({"topic": topic, "research": combined_research})
    time.sleep(2)  # Throttle call
    
    # Node 4: Critic Chain
    criticism = critic_chain.invoke({"report": report})
    
    return {
        "report": report,
        "criticism": criticism
    }

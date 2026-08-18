from dotenv import load_dotenv
load_dotenv()
from langchain_tavily import TavilySearch
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from rich import print

tavily = TavilySearch(max_results=3)

@tool
def web_searching(query: str) -> str :
    """Search the web for reliable and recent information."""
    results = tavily.invoke({"query": query})
    output = []
    for r in results["results"]:
        output.append(
            f"Title: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"Snippet: {r['content']}"
        )
    return "\n\n".join(output)

@tool
def url_scrapping(url : str) -> str :
    """Scrape and return clean content from the provided URL."""
    try:
        response=requests.get(url, timeout=5, headers={"User-agent":"Mozilla/5.0"})
        soup = BeautifulSoup(response.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"Can not scrape : {str(e)}"


from dotenv import load_dotenv
load_dotenv()
from langchain_tavily import TavilySearch
from langchain.tools import toolfrom dotenv import load_dotenv

load_dotenv()

from langchain_tavily import TavilySearch
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup


tavily = TavilySearch(
    max_results=3
)


@tool
def web_searching(query: str) -> str:
    """Search the web for reliable and recent information."""

    try:
        results = tavily.invoke({"query": query})

        # Handle Tavily errors or unexpected responses
        if not isinstance(results, dict):
            return f"Search failed: Unexpected response from Tavily: {results}"

        if "results" not in results:
            return f"Search failed: Tavily response did not contain results. Response: {results}"

        search_results = results["results"]

        if not search_results:
            return "No search results found."

        output = []

        for r in search_results:
            output.append(
                f"Title: {r.get('title', 'No title')}\n"
                f"URL: {r.get('url', 'No URL')}\n"
                f"Snippet: {r.get('content', 'No content')}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Web search failed: {str(e)}"


@tool
def url_scrapping(url: str) -> str:
    """Scrape and return clean content from the provided URL."""

    try:
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(
            separator=" ",
            strip=True
        )[:3000]

    except Exception as e:
        return f"Cannot scrape: {str(e)}"import requests
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


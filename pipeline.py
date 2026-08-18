from langchain_core.messages import HumanMessage
from agents import search_agent, reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:
    state = {}
    
    # Step 1: Search Agent
    print("=" * 50 + "\nstep 1\n")
    search = search_agent()
    search_result = search.invoke({
        "messages": [HumanMessage(content=f"Find recent and reliable information about {topic}")]
    })
    state["search_results"] = search_result["messages"][-1].content
    print(state["search_results"])

    # Step 2: Reader Agent
    print("=" * 50 + "\nstep 2\n")
    reader = reader_agent()
    reader_result = reader.invoke({
        "messages": [
            HumanMessage(
                content=f"Based on the following search results about '{topic}', "
                        f"pick the most relevant URL and scrape it for deeper analysis content.\n"
                        f"Search results: {state['search_results'][:800]}"
            )
        ]
    })
    state["scraped_results"] = reader_result["messages"][-1].content
    print(state["scraped_results"])

    # Step 3: Writer Report
    print("=" * 50 + "\nstep 3\n")
    combined_research = (
        f"Search results: {state['search_results']}\n"
        f"Detailed scraped result: {state['scraped_results']}"
    )
    state['report'] = writer_chain.invoke({
        "topic": topic,
        "research": combined_research
    })
    print(state["report"])

    # Step 4: Critic Report
    print("=" * 50 + "\nstep 4\n")
    state['feedback'] = critic_chain.invoke({
        "report": state['report']
    })
    print(state['feedback'])

    return state

if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    run_research_pipeline(topic)
import streamlit as st
from pipeline import run_research_pipeline


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="ResearchPilot",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------
# Custom styling
# -----------------------------
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f9fc;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero {
            padding: 2rem 2.2rem;
            border-radius: 20px;
            background: linear-gradient(135deg, #eef2ff 0%, #f8f5ff 100%);
            border: 1px solid #e4e7f2;
            margin-bottom: 1.5rem;
        }

        .hero h1 {
            margin-bottom: 0.3rem;
            font-size: 2.4rem;
        }

        .hero p {
            color: #5f6472;
            font-size: 1.05rem;
            margin-bottom: 0;
        }

        .step-card {
            padding: 1rem 1.2rem;
            border: 1px solid #e6e8ef;
            border-radius: 14px;
            background: white;
            margin-bottom: 0.8rem;
        }

        .step-title {
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .step-description {
            color: #6b7280;
            font-size: 0.9rem;
        }

        div[data-testid="stExpander"] {
            border-radius: 14px;
        }

        .report-box {
            padding: 1.4rem;
            border-radius: 16px;
            background: white;
            border: 1px solid #e5e7eb;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🔎 ResearchPilot")
    st.caption("Multi-Agent Research System")

    st.markdown("---")

    st.markdown("### How it works")

    st.markdown(
        """
        **1. 🔍 Search Agent**  
        Finds recent and reliable information.

        **2. 📖 Reader Agent**  
        Selects a relevant source and scrapes it.

        **3. ✍️ Writer Agent**  
        Combines the research into a report.

        **4. 🧐 Critic Agent**  
        Reviews the generated report.
        """
    )

    st.markdown("---")
    st.caption("Powered by LangChain + Tavily + BeautifulSoup")


# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🔎 ResearchPilot</h1>
        <p>
            An AI-powered multi-agent research system that searches the web,
            reads sources, writes a report, and critiques the result.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Research input
# -----------------------------
st.subheader("What do you want to research?")

topic = st.text_area(
    "Research topic",
    placeholder="Example: Impact of generative AI on software development in 2026",
    height=100,
    label_visibility="collapsed",
)

research_button = st.button(
    "🚀 Start Research",
    type="primary",
    use_container_width=True,
)


# -----------------------------
# Run pipeline
# -----------------------------
if research_button:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    topic = topic.strip()

    st.markdown("### Research Pipeline")

    # Progress UI
    progress = st.progress(0)
    status = st.empty()

    status.info("🔍 Running Search Agent...")
    progress.progress(10)

    try:
        # Your existing pipeline handles all four agents.
        result = run_research_pipeline(topic)

        progress.progress(100)
        status.success("✅ Research completed successfully!")

    except Exception as e:
        progress.empty()
        status.error("❌ Something went wrong while running the research pipeline.")

        st.exception(e)
        st.stop()

    # Save result in session state
    st.session_state["research_result"] = result
    st.session_state["research_topic"] = topic


# -----------------------------
# Display results
# -----------------------------
if "research_result" in st.session_state:
    result = st.session_state["research_result"]
    topic = st.session_state["research_topic"]

    st.markdown("---")
    st.subheader(f"📌 Research Results: {topic}")

    # Pipeline summary
    st.markdown("### Agent Outputs")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("🔍 Search Agent — Search Results", expanded=False):
            st.markdown(
                str(result.get("search_results", "No search results available."))
            )

        with st.expander("📖 Reader Agent — Scraped Content", expanded=False):
            st.markdown(
                str(result.get("scraped_results", "No scraped content available."))
            )

    with col2:
        with st.expander("🧐 Critic Agent — Feedback", expanded=False):
            st.markdown(
                str(result.get("feedback", "No critic feedback available."))
            )

        with st.expander("📊 Pipeline State", expanded=False):
            st.write(
                {
                    "topic": topic,
                    "search_results": bool(result.get("search_results")),
                    "scraped_results": bool(result.get("scraped_results")),
                    "report": bool(result.get("report")),
                    "feedback": bool(result.get("feedback")),
                }
            )

    # Final report
    st.markdown("---")
    st.subheader("📝 Final Research Report")

    report = result.get("report", "No report was generated.")

    st.markdown(
        f"""
        <div class="report-box">
        {report}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Download report
    st.download_button(
        label="⬇️ Download Report",
        data=str(report),
        file_name=f"{topic[:50].replace(' ', '_')}_research_report.txt",
        mime="text/plain",
    )
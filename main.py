
from crewai import Crew
from agents import customer_query_agent,knowledge_base_agent,sentiment_analysis_agent,response_generation_agent,feedback_collection_agent
from tasks import extract_key_phrases,retrieve_and_rank_info,analyze_sentiment,generate_response,collect_and_analyze_feedback



crew = Crew(
    agents=[customer_query_agent,knowledge_base_agent,sentiment_analysis_agent,response_generation_agent,feedback_collection_agent],
    tasks=[extract_key_phrases,retrieve_and_rank_info,analyze_sentiment,generate_response,collect_and_analyze_feedback],
    memory=True,
    cache=True,
    verbose = 2
)
customer_inquiry =input("How can I help you?\n")
 
# query_inputs = {"inquiry":customer_inquiry}

result = crew.kickoff(inputs={"customer_inquiry": customer_inquiry})
print(result)

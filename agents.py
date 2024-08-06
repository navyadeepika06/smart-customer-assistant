from crewai import Agent
from dotenv import load_dotenv
import os
from tools import search_tool,txt_search_tool,elasticsearch_tool

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

customer_query_agent = Agent(
    role='Customer Query Agent',
    goal='Classify and extract key phrases from {customer_inquiry}',
        
    backstory= ("With a passion for helping others, you excel at understanding and"
    "resolving customer concerns. Your deep empathy for customer experiences "
    "drives you to ensure every inquiry is addressed promptly and accurately."
    "Equipped with advanced AI tools, you're dedicated to optimizing the support,"
    "process extracting essential information from queries, and categorizing"
    "them to facilitate swift and effective responses."
    ),
    tool=[txt_search_tool],
    verbose = True,
    allow_delegation = True
)

knowledge_base_agent = Agent(
    role='Knowledge Base Specialist',
    goal='Retrieve and rank relevant information based on the classified query and key phrases',

    backstory=(
        "You are a Knowledge Base Specialist with expertise in efficiently retrieving and ranking the most relevant information "
        "from a vast array of sources. Your goal is to provide accurate and useful information quickly and effectively."
    ),
    tool=[elasticsearch_tool],
    verbose=True,
    allow_delegation=True,
)

sentiment_analysis_agent = Agent(
    role='Sentiment Analysis Agent',
    goal="Analyse the sentiment score of customer's inquiry and tag sentiment along for the enquiry.",
   
    backstory= ("With a passion for helping others, you excel at understanding the emotion"
    "of the customer. Your deep empathy for customer experiences drives you to ensure every"
    "emotion behind the customer's query and every emotion is addressed accurately."
    "Equipped with advanced AI tools, you're dedicated to understand the emotion behind the"
    "customer's query for generating an effective response."
    ),
    tool=[txt_search_tool],
    verbose = True,
    allow_delegation = True
)

response_generation_agent = Agent(
    role="Response Generation Agent",
    goal="Generate the revelant responses to the customers inquiry.",

    backstory=(
        "You are a response generative specialist with expertise in efficiently giving the most relevant"
        "response to the customers inquiry based on the information you got from the previous agents."
        "Equipped with advanced AI tools, you're dedicated to generate most relevant response to the"
        "customer's inquiry based on the information you got."
    ),
    verbose=True,
    allow_delegation=True
)

feedback_collection_agent = Agent(
    role='Feedback Collection Agent',
    goal="Collect and analyze customer feedback to improve the support system.",
   
    backstory=("Your mission is to gather and interpret feedback from customers to enhance their experience."
    "You thrive on understanding customer opinions and using them to drive improvements. Equipped with"
    "cutting-edge AI tools, you ensure that every piece of feedback is recorded, analyzed, and used to"
    "make the support system better."
    ),
    verbose=True,
    allow_delegation=True
)
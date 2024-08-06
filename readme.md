Smart Customer Support Assistant

Project Overview
   The Smart Customer Support Assistant is designed to provide efficient and empathetic customer support by leveraging advanced AI tools. The system consists of various agents working together to classify queries, analyze sentiment, collect feedback, and generate appropriate responses. This project aims to enhance customer satisfaction and streamline support processes.

Key Components
   main.py: 
        Main class 
    agents.py: 
        Class defining the CrewAI Agents.
    tasks.py: 
        Class defining the CrewAI Tasks.
    tools.py: 
        Class implementing the GmailDraft Tool.
    response.txt:
        File to show the final output


Running the Code

    This example uses GPT-3.5.

    Configure Environment: 
        project_crewai folder in vs code
        Run conda create --name venv python=3.11

    Install Dependencies: 
        Run pip install crewai
        Run pip install crewai_tools
        Run pip install elasticsearch

    Execute the Script: 
        Run python main.py


Execution: 

    Running the Script: Execute python main.py

    
It is created using CrewAI with following Agents, Tasks, Tools, Inputs, Outputs...

Agents

1. Customer Query Agent
Role: Classify customer queries and extract key phrases.
Goal: Identify the nature of the customer's inquiry to route it appropriately.
Tool: TXTSearchTool

2. Knowledge Base Agent
Role: Retrieve relevant information from the knowledge base.
Goal: Provide accurate and helpful information based on the classified query and key phrases
Tool: ElasticSearch

3. Sentiment Analysis Agent
Role: Analyze the sentiment of customer inquiries.
Goal: Tag the emotional tone of the customer's query for context-aware responses.
Tool: TXTSearchTool

4. Response Generation Agent
Role: Generate contextually relevant responses.
Goal: Address customer queries effectively while considering the emotional tone.

5. Feedback Collection Agent
Role: Collect and analyze customer feedback.
Goal: Gather insights to improve the customer support system.

Tasks

1. Customer Query Processing
Description: Classify customer queries and extract key phrases.
Expected Output: Classified query and key phrases.
Agent: Customer Query Agent

2. Knowledge Retrieval
Description: Retrieve relevant information from the knowledge base using classified queries and key phrases.
Expected Output: Accurate and helpful information related to the customer's inquiry.
Agent: Knowledge Base Agent

3. Sentiment Analysis
Description: Analyze the sentiment of customer inquiries and tag them accordingly.
Expected Output: Sentiment tag (e.g., Positive, Negative, Neutral).
Agent: Sentiment Analysis Agent

4. Generate Response
Description: Generate contextually relevant responses based on the retrieved information and sentiment tag.
Expected Output: A clear, empathetic, and actionable response.
Agent: Response Generation Agent

5. Collect and Analyze Feedback Data
Description: Collect feedback from customers and analyze it to extract key insights.
Expected Output: Comprehensive report including a summary of feedback data, common themes, sentiment analysis, and actionable recommendations.
Agent: Feedback Collection Agent


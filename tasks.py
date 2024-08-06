from crewai import Task
from agents import customer_query_agent,knowledge_base_agent,sentiment_analysis_agent,response_generation_agent,feedback_collection_agent

extract_key_phrases = Task(
    description="Efficiently classify {customer_inquiry} into predefined categories"
        "such as 'Technical Issue', 'Customer Support', 'Product Feedback', etc."
        "Extract key phrases that highlight the main concerns and details within the {customer_inquiry}.",
    expected_output=
        "A dictionary containing the classification category and a list of key phrases.\n"
        "The inquiry should be classified into one of the predefined categories, and key phrases "
        "highlighting the main concerns and details should be extracted. "
        "For example, if the inquiry is about a technical issue with battery life, the output might be:\n"
        "Category: Technical Issue\nKey Phrases: battery life, drains quickly, troubleshooting steps, factory reset, replacement, refund."
   
    ,
    agent=customer_query_agent,
    output_file='key_phrases.txt'
)

retrieve_and_rank_info = Task(
    description="Retrieve and rank relevant information based on the classified query and key phrases provided.\n"
                "The agent should search through available knowledge bases, databases, and other resources to find the most pertinent information.\n"
                "The information should be ranked according to relevance and presented in a clear and concise format.",
    expected_output="A list of relevant information ranked by relevance.\n"
                    "For example, given a classified query about 'Technical Issue' and key phrases like 'battery life, drains quickly', "
                    "the output might be:\n"
                    "1. Solution to improve battery life on device X.\n"
                    "2. Common causes of battery drain and troubleshooting steps.\n"
                    "3. Official guidelines for factory reset to resolve battery issues.",
    agent=knowledge_base_agent,
    output_file='rank_info.txt'
)

analyze_sentiment = Task(
    description="Efficiently find out the sentiment of {customer_inquiry} which has predefined categories"
                " such as 'Positive', 'Negative', 'Neutral', 'Very Positive', 'Mixed', 'Very Negative', etc."
                " Extract the emotion and sentiment score of the customer's inquiry.",
    expected_output="A dictionary containing the inquiry, its classification category, key phrases, sentiment tag, and sentiment score.\n"
                    "The inquiry should be classified into one of the predefined categories of sentiment, "
                    "which describes the emotion of the customer. "
                    "For example, if the customer's emotion is positive, the output might be:\n"
                    "Inquiry: inquiry title\n"
                    "Category: Technical Issue\n"
                    "Key Phrases: battery life, drains quickly, troubleshooting steps\n"
                    "Sentiment Tag: Positive\n"
                    "Sentiment Score: 0.85",
    agent=sentiment_analysis_agent,
    output_file='sentiment.txt'
)


generate_response = Task(
    description="Generate contextually relevant responses based on the retrieved information and sentiment tag provided.\n"
                "The agent should create responses that effectively address the user's concerns while considering the emotional tone indicated by the sentiment tag.\n"
                "The responses should be clear, empathetic, and actionable.",
    expected_output="A contextually relevant response that considers both the content of the retrieved information and the sentiment tag.\n"
                    "For example, if the retrieved information is about 'Technical Issue' and the sentiment tag is 'Negative', "
                    "the output might be:\n"
                    "'We understand your frustration with the battery life issues. Here are some steps you can take to improve battery performance: ...'"
                    "1.Check battery usage settings and close or uninstall high-usage apps.\n"
                    "2.Reduce screen brightness, enable battery saver mode, and turn off unnecessary features.\n"
                    "3.Keep your OS and apps updated, and restart your phone regularly.\n",
    agent=response_generation_agent,
    output_file='response.txt'
)

collect_and_analyze_feedback = Task(
    description="Collect feedback from customers and analyze it to extract key insights.\n"
                "The agent should gather feedback through surveys, reviews, or direct comments.\n"
                "Analyze the collected data to identify common themes, sentiment, and actionable insights.\n"
                "Generate a summary report highlighting the main findings and suggesting improvements based on the feedback.",
    expected_output="A comprehensive report that includes:\n"
                    "1. Summary of collected feedback data.\n"
                    "2. Identification of common themes and issues mentioned by customers.\n"
                    "3. Sentiment analysis of the feedback to gauge overall customer satisfaction.\n"
                    "4. Actionable insights and recommendations for improving the customer support system.\n"
                    "For example, if multiple customers mention 'slow response times' and the sentiment is 'Negative', "
                    "the output might include a recommendation to 'Increase support staff during peak hours to reduce response times'.",
    agent=feedback_collection_agent,
    output_file='feedback_report.txt'
)
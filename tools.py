from crewai_tools import SerperDevTool,TXTSearchTool

from langchain.tools import tool
from elasticsearch import Elasticsearch
 
class ElasticsearchTool:
    def __init__(self, host):
        self.client = Elasticsearch(hosts=[host])
 
    def search(self, index, query):
        response = self.client.search(index=index, body={"query": {"match": {"content": query}}})
        hits = response["hits"]["hits"]
        return "\n".join([hit["_source"]["content"] for hit in hits])
 
# Create an instance of the tool
elasticsearch_tool = ElasticsearchTool("http://localhost:9200")
 
# Define a tool function for LangChain
@tool
def elasticsearch_search(query: str) -> str:
    """Search the Elasticsearch index for the given query and return the results."""
    return elasticsearch_tool.search("documents", query)


txt_search_tool = TXTSearchTool()
search_tool = SerperDevTool()
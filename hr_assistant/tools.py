# step 5 : wrap the retriever as a tool the agent can call.

from langchain.tools import tool

def create_search_tool(retriever):
    """
    return a @tool function that searches the hr policy document.
    """

    @tool
    def search_hr_policy(question : str)-> str:
        """
        search the hr policy document for information about leave, work from home, probation, notice period, and more
        """
        matching_chunks = retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)
    return search_hr_policy

    
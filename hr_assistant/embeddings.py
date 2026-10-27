# step 3 : turn tet into numbers (vectors) using jina

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """
    returns a jina embedding model reads jina api key from the environment
    """
    return JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)


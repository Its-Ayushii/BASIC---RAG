# step 4 : store chunks embedding in FAISS so we can search them later

import os
from langchain_community.vectorstores import FAISS

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model

# build_vector_store

def build_vector_store(chunks):
    """
    embed every chunk and build a searchable FAISS index in memory
    """
    embeddings_model = get_embeddings_model()
    return FAISS.from_documents(chunks, embeddings_model)

# save_vector_store

def save_vector_store(vector_store , path : str = config.VECTOR_STORE_PATH)-> None :
    """
    Save the FAISS index to disk so we don't have to rebuild 
    it every time.
    """
    vector_store.save_local(path)


# load_vector_store

def load_vector_store(path : str = config.VECTOR_STORE_PATH):
    """
    load a previously saved FAISS index from the disk
    """
    embedding_model = get_embeddings_model()
    # allow_dangerous_deserialiazation is safe here because we only ever load
    # an index that this same app created and saved
    return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization = True)

# check_vector_store

def vector_store_exists(path:str = config.VECTOR_STORE_PATH) -> bool:
    return os.path.exists(os.path.join(path, "index.faiss"))

# get retriever

def get_retriever(vector_store, k:int = config.TOP_K_RESULTS):
    return vector_store.as_retriever(search_kwargs={"k":k})


    



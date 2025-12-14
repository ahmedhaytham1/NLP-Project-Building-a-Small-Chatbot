from data.dataset_loader import load_data
from preprocessing.clean_text import preprocess_dataset
from rag.embeddings import load_embedding_model, generate_embeddings
from rag.vector_store import VectorStore
from llm.llm_api import ask_llm
import numpy as np

# Load & preprocess data
dataset = load_data()
dataset = preprocess_dataset(dataset)

texts = dataset["clean_context"]

# Embeddings
model = load_embedding_model()
embeddings = generate_embeddings(texts, model)

# Vector store
vector_store = VectorStore(np.array(embeddings))

def retrieve_context(query, k=2):
    query_embedding = model.encode([query])
    indices = vector_store.search(query_embedding, k)
    return " ".join([texts[i] for i in indices[0]])

print("RAG Chatbot is running (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    context = retrieve_context(user_input)
    answer = ask_llm(user_input, context)

    print("Bot:", answer)

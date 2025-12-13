# NLP Project – Building a Small Chatbot

## 📌 Project Overview

This project demonstrates the practical application of **Natural Language Processing (NLP)** by building a small chatbot that runs in the terminal. The chatbot starts with a simple baseline implementation and is then enhanced using a **Retrieval-Augmented Generation (RAG)** approach integrated with a **Large Language Model (LLM) API**.

The project focuses on understanding NLP fundamentals, working with real datasets, and applying modern techniques such as embeddings, vector search, and secure API usage.

---

## 🎯 Project Objectives

* Understand NLP concepts through hands-on implementation
* Work with a real-world dataset
* Build a terminal-based chatbot
* Integrate an LLM API in a correct and secure way
* Apply an advanced NLP technique (RAG)

---

## 🧠 Project Methodology

The project is divided into multiple stages:

1. Dataset collection
2. Text preprocessing
3. Baseline chatbot implementation
4. Advanced chatbot using RAG
5. LLM API integration
6. API key security

---

## 📊 Dataset

* **Source:** Hugging Face Datasets
* **Dataset Used:** SQuAD (Question Answering Dataset)
* **Reason for Selection:**

  * Well-structured QA format
  * Publicly available and reliable
  * Suitable for retrieval-based systems

The dataset is loaded and a subset is used to ensure fast experimentation.

---

## 🧹 Text Preprocessing

To improve data quality before feeding it into the chatbot, several preprocessing steps are applied:

* Convert text to lowercase
* Remove punctuation, numbers, and special characters
* Normalize text format

These steps help reduce noise and improve embedding quality.

---

## 🤖 Baseline Chatbot

A simple rule-based chatbot is implemented to demonstrate the basic chatbot flow.

**Features:**

* Runs in the terminal
* Continuous user input loop
* Exit condition
* Static responses

This stage focuses on understanding the chatbot interaction flow rather than intelligence.

---

## 🚀 Advanced Chatbot – RAG Implementation

To enhance the chatbot’s intelligence, a **Retrieval-Augmented Generation (RAG)** approach is implemented.

### 🔹 Retrieval Phase

* Text data is converted into embeddings using a sentence transformer model
* Embeddings are stored in a FAISS vector store
* Relevant contexts are retrieved based on semantic similarity to the user query

### 🔹 Generation Phase

* Retrieved context is passed along with the user question to an LLM
* The LLM generates an answer grounded in the retrieved data

This approach reduces hallucinations and improves answer relevance.

---

## 🔐 LLM API Integration & Security

* An external LLM API is used for response generation
* API keys are **never hardcoded** in the source code
* Environment variables are used to securely store API keys

This ensures best practices in security and prevents accidental key exposure.

---

## 📸 Screenshots (Submission Requirements)

The following screenshots are included as proof of implementation:

1. Dataset successfully loaded
2. Data preprocessing results
3. Baseline chatbot running
4. RAG retrieval process
5. LLM API response
6. Secure API key usage (key hidden)

---

## 📁 Project Structure

```
nlp-chatbot/
│
├── data/
│   └── dataset_loader.py
│
├── preprocessing/
│   └── clean_text.py
│
├── rag/
│   ├── embeddings.py
│   └── vector_store.py
│
├── llm/
│   └── llm_api.py
│
├── baseline_chatbot.py
├── main.py
├── README.md
├── .env
└── screenshots/
```

---

## 👥 Team Responsibilities

### 👤 Ahmed Haytham

**Role: Project Integration & Final Chatbot**

* Integrating all components into a single system
* Building the final chatbot pipeline
* Testing the full RAG workflow
* Organizing project structure
* Preparing screenshots and documentation

---

### 👤 Bassant Khaled

**Role: Dataset Collection & Preprocessing**

* Selecting and loading the dataset
* Cleaning and preprocessing text data
* Preparing data for embeddings and retrieval

---

### 👤 Mohamed Gamal

**Role: Baseline Chatbot Development**

* Implementing the terminal-based chatbot
* Handling user input and exit conditions
* Demonstrating the basic chatbot flow

---

### 👤 Malak Ayman

**Role: Embeddings & Vector Store (RAG – Retrieval)**

* Generating embeddings for text data
* Implementing FAISS vector search
* Retrieving relevant contexts

---

### 👤 Abdelrahman Mohamed

**Role: LLM API Integration (RAG – Generation)**

* Integrating the LLM API
* Designing prompts for QA
* Handling API responses securely
* Managing API key security

---

## ✅ Conclusion

This project successfully demonstrates the end-to-end process of building a small NLP-based chatbot. It combines foundational NLP concepts with modern LLM-based techniques while following best practices in software structure and security.

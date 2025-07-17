# 🧠 AI/ML Engineering – Advanced Internship Tasks  

This repository contains my completed tasks for the **Advanced AI/ML Engineering Internship** at DevelopersHub Corporation. The tasks focus on hands-on experience with advanced machine learning techniques, including Transformers, Scikit-learn Pipelines, LangChain-based conversational AI, and LLM applications.  

I have completed the following four tasks out of the five provided:

---

## ✅ Task 1: News Topic Classifier Using BERT

### 🔍 Objective
Fine-tune a Transformer model (`bert-base-uncased`) to classify news headlines into topic categories using the AG News dataset.

### ⚙️ Methodology
- Loaded the AG News dataset from Hugging Face Datasets.
- Preprocessed and tokenized the data using Hugging Face’s `AutoTokenizer`.
- Fine-tuned the BERT model using the `Trainer` API.
- Evaluated performance using **accuracy** and **F1-score**.
- Deployed the model with an interactive frontend using **Streamlit**.

### 📊 Key Results & Observations
- Achieved high accuracy (>90%) in classifying headlines.
- Fine-tuning significantly improved BERT’s classification on this task.
- The deployment allows real-time predictions on user-input headlines.

---

## ✅ Task 2: End-to-End ML Pipeline with Scikit-learn

### 🔍 Objective
Build a production-ready machine learning pipeline for predicting customer churn using the Telco Churn dataset.

### ⚙️ Methodology
- Used Scikit-learn’s **Pipeline API** for complete preprocessing and modeling.
- Included steps: Label encoding, scaling, missing value handling.
- Trained models: **Logistic Regression**, **Random Forest**.
- Used `GridSearchCV` for hyperparameter optimization.
- Exported the final pipeline using `joblib`.

### 📊 Key Results & Observations
- The pipeline provides a robust and reusable framework for future predictions.
- Random Forest outperformed Logistic Regression on both accuracy and F1.
- Exported model can be integrated easily into production systems.

---

## ✅ Task 4: Context-Aware Chatbot Using LangChain

### 🔍 Objective
Create a chatbot that can hold contextual conversations and retrieve relevant answers from an external document corpus using LangChain or RAG (Retrieval-Augmented Generation).

### ⚙️ Methodology
- Built a vector store using `FAISS` from embedded text documents.
- Implemented a chatbot using **LangChain’s ConversationalRetrievalChain**.
- Enabled conversation memory for context awareness.
- Integrated with **Streamlit** for deployment.

### 📊 Key Results & Observations
- The chatbot was able to retrieve accurate information based on prior conversation context.
- LangChain enabled fast development with robust integration.
- The system is ideal for internal knowledge bases or support bots.

---

## ✅ Task 5: Auto Tagging Support Tickets Using LLM

### 🔍 Objective
Automatically tag support tickets into categories using large language models (LLMs), and compare zero-shot, few-shot, and fine-tuned approaches.

### ⚙️ Methodology
- Used a free-text support dataset.
- Applied **zero-shot** classification using OpenAI/Hugging Face LLMs.
- Fine-tuned a transformer model on the labeled dataset.
- Implemented **few-shot learning** to improve performance.
- Output top 3 tag predictions per ticket.

### 📊 Key Results & Observations
- Fine-tuned model performed better than zero-shot models, especially on frequent classes.
- Few-shot approach improved generalization on rare tags.
- Prompt engineering was critical for zero/few-shot setups.



import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model = BertForSequenceClassification.from_pretrained("bert-agnews-model")
tokenizer = BertTokenizer.from_pretrained("bert-agnews-model")
model.eval()

# Load class names
classes = [line.strip() for line in open("classes.txt")]

st.title("📰 AG News Topic Classifier")
text = st.text_area("Enter news headline or short article:")

if st.button("Predict"):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        logits = model(**inputs).logits
        prediction = torch.argmax(logits, dim=1).item()
    st.success(f"Predicted Topic: **{classes[prediction]}**")
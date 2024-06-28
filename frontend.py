import streamlit as st
import requests

# Streamlit UI
st.title("Model Garden Q&A")

context = st.text_area("Context", "Enter the context for the question here.")
question = st.text_input("Question", "Enter your question here.")

models = ["model1", "model2"]
selected_model = st.selectbox("Select a model", models)

if st.button("Switch Model"):
    response = requests.post('http://127.0.0.1:5000/switch_model', json={"model_name": selected_model})
    if response.status_code == 200:
        st.success(f"Switched to {selected_model}")
    else:
        st.error("Error switching model")

if st.button("Get Answer"):
    response = requests.post('http://127.0.0.1:5000/answer', json={"question": question, "context": context})
    if response.status_code == 200:
        answer = response.json()["answer"]
        st.write(f"Answer: {answer}")
    else:
        st.error("Error getting answer")

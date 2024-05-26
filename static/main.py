import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

# Streamlit app
st.title("Text Summarization with T5")



# Input text area
input_text = st.text_area("Enter your text here: ", height=200)

# Generate summary button
if st.button("Generate Summary"):
    # Check if input text is provided
    if not input_text:
        st.error("Please enter some text to summarize.")
    else:
        # Generate summary
        summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
        summarized_text = summary[0]["summary_text"]
        
        # Display summary
        st.subheader("Generated Summary:")
        st.write(summarized_text)

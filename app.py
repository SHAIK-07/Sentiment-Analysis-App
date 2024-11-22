import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
@st.cache_resource
def load_pipeline():
    return pipeline("sentiment-analysis", framework="pt")

sentiment_analyzer = load_pipeline()

# Streamlit app title
st.title("Sentiment Analysis App")
st.subheader("Analyze the sentiment of your text statements")

# Text input from the user
text = st.text_area("Enter a statement for sentiment analysis", height=150)


# Analyze sentiment when the button is clicked
if st.button("Analyze Sentiment"):
    if text.strip():
        result = sentiment_analyzer(text)[0]
        sentiment = result['label']
        confidence = result['score']

        # Display the results
        st.write("### Results:")
        st.write(f"**Sentiment**: {sentiment}")
        st.write(f"**Confidence**: {confidence:.2f}")
    else:
        st.warning("Please enter a valid statement.")


# Footer
st.markdown("---")
st.markdown("Powered by [Hugging Face](https://huggingface.co/) | Developed with ❤️ by [Shaik](https://www.linkedin.com/in/shaik-hidaythulla/)")


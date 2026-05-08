import streamlit as st
from openai import OpenAI
from collections import Counter
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("ReviewSense")
st.subheader("Customer Review Insight Assistant")

uploaded_text = st.text_area(
    "Paste customer reviews here:",
    height=300
)

# -------------------------------
# Baseline keyword analysis
# -------------------------------

keywords = {
    "service": ["slow", "wait", "rude"],
    "price": ["expensive", "price", "cost"],
    "quality": ["cold", "bland", "excellent"],
    "staff": ["friendly", "professional", "unhelpful"]
}

def baseline_analysis(text):
    text_lower = text.lower()
    counts = Counter()

    for category, words in keywords.items():
        for word in words:
            counts[category] += text_lower.count(word)

    return counts

# -------------------------------
# GPT analysis
# -------------------------------

def gpt_analysis(text):

    prompt = f"""
    Analyze the following customer reviews.

    Return:
    1. Main themes
    2. Positive feedback
    3. Negative feedback
    4. Recommended business improvements

    Reviews:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# -------------------------------
# Button
# -------------------------------

if st.button("Analyze Reviews"):

    if uploaded_text.strip() == "":
        st.warning("Please paste some reviews.")
    else:

        st.subheader("Baseline Analysis")

        baseline_results = baseline_analysis(uploaded_text)

        for category, count in baseline_results.items():
            st.write(f"{category}: {count}")

        st.subheader("GenAI Analysis")

        result = gpt_analysis(uploaded_text)

        st.write(result)
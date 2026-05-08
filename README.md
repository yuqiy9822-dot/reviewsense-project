# ReviewSense

ReviewSense is a small GenAI application that helps small-business owners analyze customer reviews and identify common themes, complaints, positive feedback, and improvement priorities.

## 1. Context, User, and Problem

The target user is a small-business owner or manager who receives customer reviews from platforms such as Google, Yelp, or Amazon. Reading reviews manually can be time-consuming and inconsistent.

This project improves the workflow of reviewing customer feedback by turning unstructured reviews into structured business insights.

## 2. Solution and Design

ReviewSense is built as a Streamlit web app.

The user pastes customer reviews into the app. The app provides two outputs:

1. A simple keyword-based baseline analysis
2. A GenAI analysis using an OpenAI model

The GenAI output includes:
- Main themes
- Positive feedback
- Negative feedback
- Recommended business improvements

## 3. Baseline Comparison

The baseline uses keyword matching. For example, words such as "slow," "expensive," "cold," and "friendly" are counted and grouped into categories.

The GenAI version performs better because it can summarize meaning, group related issues, and produce more actionable recommendations.

## 4. Evaluation and Results

I tested the app using a sample set of customer reviews with positive, negative, and mixed feedback.

A good output should:
- Identify the major review themes
- Separate positive and negative feedback
- Provide clear business recommendations
- Avoid vague or unsupported conclusions

The GenAI output was more useful than the baseline because it explained the meaning behind the reviews instead of only counting keywords.

## 5. Failure Cases and Human Oversight

The app may fail when reviews are sarcastic, very short, or ambiguous. It may also overgeneralize from a small number of reviews.

A human manager should still review the original customer comments before making business decisions.

## 6. Setup Instructions

Install dependencies:

```bash
pip install -r requirements.txt
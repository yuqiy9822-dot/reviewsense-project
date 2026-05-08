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

The baseline uses keyword matching. Words such as "slow," "expensive," "cold," and "friendly" are counted and grouped into categories: service, price, quality, and staff.

The GenAI version performs better because it can summarize meaning, understand sentiment direction, group related issues, and produce more actionable recommendations.

## 4. Evaluation and Results

I tested the app using the following 10 sample reviews representing a mix of positive, negative, and mixed feedback:

> "The food was delicious but the service was very slow. Staff members were friendly and professional. The restaurant was too expensive for the portion size. Great atmosphere and clean environment. I waited 40 minutes for my order. The quality of the food was excellent. Customer support was unhelpful and rude. Prices are reasonable and the menu has many choices. The food arrived cold and tasted bland. Amazing experience overall. I would come back again."

**A good output should:**
- Identify the major review themes (food, service, price, staff)
- Clearly separate positive and negative feedback
- Provide actionable business recommendations
- Avoid vague or unsupported conclusions

**Baseline output:**

| Category | Matched Keywords | Count |
|----------|-----------------|-------|
| service  | "slow", "wait", "rude" | 3 |
| price    | "expensive", "price" | 2 |
| quality  | "cold", "bland", "excellent" | 3 |
| staff    | "friendly", "professional", "unhelpful" | 3 |

The baseline correctly detects that all four categories are mentioned, but cannot distinguish positive from negative signals. For example, "excellent" and "bland" both count toward the quality category — producing a score of 3 with no indication of sentiment direction.

**GenAI output (summarized):**
- Main themes: food quality, service speed, pricing, staff attitude
- Positive feedback: food taste, clean atmosphere, friendly staff, overall experience
- Negative feedback: long wait times (40 min), food arriving cold, high price-to-portion ratio, unhelpful customer support
- Recommendations: improve kitchen throughput, retrain customer service staff, review pricing strategy or increase portion sizes

**Conclusion:** The GenAI output is more actionable. It correctly separates "excellent quality" from "arrived cold and bland" as distinct signals, and maps complaints directly to recommended business actions. The baseline can only count keyword frequency with no sentiment awareness.

## 5. Failure Cases and Human Oversight

**Failure Case 1 — Sarcasm:**

Input: "Great, just great… waited 45 minutes for cold food. Loved it."  
Expected output: Negative review  
GenAI behavior: Likely to misread as positive due to "Great" and "Loved it"  
Baseline behavior: Catches "cold" under quality (count: 1) — partial signal only  
→ Human review is required for sarcastic or ironic language.

**Failure Case 2 — Industry-specific keyword mismatch:**

The baseline keyword list is hardcoded for restaurant contexts ("cold", "bland", "wait"). If used for a software product or retail store, most keywords would return 0 matches even for clearly negative reviews.  
→ The baseline does not generalize across industries. GenAI adapts better to different business contexts without modification.

**Failure Case 3 — Very short or vague reviews:**

Input: "It was okay."  
GenAI output: May produce generic themes with no specific insight.  
→ Low-information reviews reduce output quality for both approaches.

**When human oversight is still needed:**
- Before making staffing or pricing decisions based on the output
- When reviews contain sarcasm, dialect, or non-English text
- When the review sample is very small (fewer than 5 reviews)

## 6. Setup Instructions

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Configure your API key:**

Create a `.env` file in the project root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Do not commit this file to your repository. Make sure `.env` is listed in your `.gitignore`.

**Run the app:**

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`, paste customer reviews into the text box, and click **Analyze Reviews**.

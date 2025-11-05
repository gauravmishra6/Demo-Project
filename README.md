# 📊 Sentiment Analysis with TextBlob

This is a simple Python project that performs sentiment analysis on a list of sample text inputs using the `TextBlob` library. The results are saved in a CSV file.

---

## 📁 Project Files

- `sentiment_analysis.py` – Main script that analyzes sentiment
- `requirements.txt` – Python dependencies
- `spec.yml` – AWS CodeBuild specification for pipeline integration

---

## 🚀 How It Works

1. A list of sample text strings is defined in the script.
2. Each text is analyzed using `TextBlob` to calculate sentiment polarity.
3. Based on polarity:
   - Positive if polarity > 0
   - Negative if polarity < 0
   - Neutral if polarity == 0
4. Results are saved to `sentiment_results.csv`.

---

## 🧪 Sample Input

```python
texts = [
    "I love AWS CodePipeline, it's amazing!",
    "This deployment process is so frustrating.",
    "The weather is okay today.",
    "I am extremely happy with the service!",
    "I hate bugs in my code."
]

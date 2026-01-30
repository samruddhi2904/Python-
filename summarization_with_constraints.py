def summarize_with_constraints(article_text, model):
    """
    Summarizes a news article into 2 sentences.
    If the summary exceeds 50 words, it is truncated
    to the nearest complete sentence within 50 words.
    """

    prompt = (
        "Summarize the following news article into exactly 2 sentences:\n\n"
        f"{article_text}"
    )

    # Generate summary using the model
    response = model.generate_content(prompt)
    summary = response.text.strip()

    words = summary.split()

    # If summary exceeds 50 words, truncate safely
    if len(words) > 50:
        truncated = " ".join(words[:50])
        last_period = truncated.rfind(".")
        if last_period != -1:
            summary = truncated[: last_period + 1]
        else:
            summary = truncated

    return summary


# Sample usage (pseudo-example)
if __name__ == "__main__":
    article = (
        "Python continues to dominate the data science industry due to its "
        "simple syntax and powerful ecosystem. Many organizations rely on "
        "Python for machine learning, data analysis, and automation tasks."
    )

    # `model` should be an LLM instance (e.g., Gemini / OpenAI)
    print("Function ready for summarization with constraints.")

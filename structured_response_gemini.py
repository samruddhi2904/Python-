import json
import google.generativeai as genai

def generate_structured_response(api_key):
    """
    Uses the Gemini API to generate a structured JSON response.
    Handles cases where the response is not valid JSON.
    """

    # Configure Gemini API
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-pro")

    prompt = (
        "List 3 benefits of Python for data science. "
        "Return the response strictly in valid JSON format "
        "with a key named 'benefits'."
    )

    response = model.generate_content(prompt)
    text_response = response.text.strip()

    try:
        structured_output = json.loads(text_response)
        print("Valid JSON response received:")
        return structured_output

    except json.JSONDecodeError:
        print("Invalid JSON response received.")
        return {
            "error": "Response is not valid JSON",
            "raw_response": text_response
        }


# Sample execution
if __name__ == "__main__":
    API_KEY = "GEMINI_API_KEY"  
    result = generate_structured_response(API_KEY)
    print(result)

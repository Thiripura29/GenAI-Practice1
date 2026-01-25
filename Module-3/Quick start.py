import os
from dotenv import load_dotenv
from openai import OpenAI

# Land API key from .env file
load_dotenv()

# Initialize the OpenAI client

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --------------------------------------------------
# Quick start example
# ---------------------------------------------------

def ask_ai(prompt: str, model="gpt-4o") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user",
                 "content": prompt
                 }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:

        return f"Error {str(e)}\n\nMake sure OPENAI_API_KEY is set in your .env file"

# Example 1: Simple question

if __name__ == "__main__":
    print("-" * 70)
    print("\n OPENAI  API quick start examples")
    print("-" * 70)
    print("\n simple Question")
    print("-" * 70)
    response = ask_ai("what is COSTAR framework in the prompt Engineering")
    print(response)

# Example 2:Classification

    print("-" * 70)
    print("\n Text Classification")
    print("-" * 70)

    prompt = """
    Classify this review as POSITIVE, NEGATIVE, or NEUTRAL:
    "The product works but arrived 2 weeks late. Quality is good though."
    
    Answer with just the classification.
    """
    response = ask_ai(prompt)
    print(response)

    # Example 3:Content Generation

    print("-" * 70)
    print("\n Content Generation")
    print("-" * 70)

    prompt = """
    Write a email to HR by mentioning that one of the resource is taking sick leave frequently.Employee id =123
    """
    response = ask_ai(prompt)
    print(response)

# Example 4:Data Extraction

    print("-" * 70)
    print("\n Data Generation")
    print("-" * 70)

    prompt = """
    Extract the following from this text and format as JSON:
    - Product name
    - Price
    - Color
    
    Text: "I bought the UltraWidget Pro in blue color for $299.99"
    """
    response = ask_ai(prompt)
    print(response)

    # Example 5: Food  preparation

    print("-" * 70)
    print("\n Data Generation")
    print("-" * 70)

    prompt = """
    How to prepare delicious food  Upma using veggies  
    """
    response = ask_ai(prompt)
    print(response)




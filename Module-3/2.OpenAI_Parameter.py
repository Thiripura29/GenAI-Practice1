import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(
    prompt: str,
    model: str = "gpt-4o",
    top_p: float = 1.0,
    max_tokens: int = 200,
    temperature: float = 0.9
) -> str:
    try:
        response = client.responses.create(
            model=model,
            input=prompt,
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_tokens
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}\nMake sure OPENAI_API_KEY is set correctly."

def run_comparison_examples():
    test_prompt = "Explain AI in different terms."

    examples = [
        {
            "name": "Conservative and Predictable",
            "description": "Low temperature for consistent, factual responses.",
            "temperature": 0.2,
            "top_p": 0.9,
            "max_tokens": 150
        },
        {
            "name": "Balanced General Purpose",
            "description": "Good mix of accuracy and variety.",
            "temperature": 0.7,
            "top_p": 1.0,
            "max_tokens": 200
        },
        {
            "name": "Creative and Varied",
            "description": "Higher temperature for creative writing.",
            "temperature": 1.2,
            "top_p": 1.0,
            "max_tokens": 250
        },
        {
            "name": "Concise and Focused",
            "description": "Short and direct responses.",
            "temperature": 0.3,
            "top_p": 0.9,
            "max_tokens": 75
        }
    ]

    print("\n" + "=" * 80)
    print("OpenAI Parameter Comparison Demo")
    print("=" * 80)
    print(f'\nPrompt used for all examples: "{test_prompt}"')

    for i, config in enumerate(examples, 1):
        print("\n" + "-" * 80)
        print(f"Example {i}: {config['name']}")
        print("-" * 80)
        print(f"Description: {config['description']}")
        print(f"temperature: {config['temperature']}")
        print(f"top_p: {config['top_p']}")
        print(f"max_tokens: {config['max_tokens']}")
        print("\nResponse:")
        print("-" * 80)

        response = ask_ai(
            test_prompt,
            temperature=config["temperature"],
            top_p=config["top_p"],
            max_tokens=config["max_tokens"]
        )

        print(response)

# Run demo
run_comparison_examples()

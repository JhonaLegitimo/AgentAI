import argparse
import os
from dotenv import load_dotenv
from  google import  genai
from google.genai import types

def main():
    load_dotenv()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except RuntimeError:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", contents=messages
    )

    
    if args.verbose:
        print(" ")
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(" ")

    print(response.text)


if __name__ == "__main__":
    main()

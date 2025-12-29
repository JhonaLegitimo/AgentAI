import argparse
import os
from dotenv import load_dotenv
from  google import  genai
from google.genai import types
from config import model_name
from prompts import system_prompt
from call_function import available_functions, call_function
import sys

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
    print("DEBUG available_functions type:", type(available_functions))
    print("DEBUG available_functions:", available_functions)

    for _ in range(20):
        response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    )
        for candidate in response.candidates:
            messages.append(candidate.content)
        
        if args.verbose:
            print(" ")
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(" ")
            

        tool_responses = []

        if response.function_calls:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)

                if not function_call_result.parts:
                    raise RuntimeError("Function call returned no parts")

                part = function_call_result.parts[0]

                if not part.function_response or not part.function_response.response:
                    raise RuntimeError("Function call result missing function_response.response")

                tool_responses.append(part)

                if args.verbose:
                    print(f"-> {part.function_response.response}")
        else:
            print("Final response:")
            print(response.text)
            return
        
        if tool_responses:
            messages.append(
                types.Content(
                    role="user",
                    parts=tool_responses,
                )
            )
    print("Reached maximum number of iterations without a final response.")
    sys.exit(1)


if __name__ == "__main__":
    main()

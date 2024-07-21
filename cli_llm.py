import sys
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python llm_cli.py 'Your prompt here'")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    response = generate_response(prompt)
    print(response)

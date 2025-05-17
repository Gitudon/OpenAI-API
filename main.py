from dotenv import *
from openai import OpenAI

API_KEY = dotenv_values(".env")["API_KEY"]

def main():
    while True:
        prompt = input("Enter your prompt (or 'end' to quit): ")
        if prompt.lower() == "end":
            break
        client = OpenAI(api_key=API_KEY)
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        print(response.output_text)

if __name__=="__main__":
    main()
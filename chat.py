import openai

# Create an OpenAI client with your KRUTRIM API KEY and endpoint
openai.api_key = "yNiHzza+7dBNJ~5bMJCCF_1/YBV"  # Replace with your API key
openai.base_url = "https://cloud.olakrutrim.com/v1"

def chat():
    print("You are now chatting with a helpful assistant. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]

        response = openai.ChatCompletion.create(
            model="Meta-Llama-3-8B-Instruct",
            messages=messages,
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.7,
        )

        assistant_response = response.choices[0].message.content
        print("Assistant:", assistant_response)

if __name__ == "__main__":
    chat()

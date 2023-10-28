import openai
import os

# Set your OpenAI API key here
openai.api_key = "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"


def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can try other engines too
        prompt=prompt,
        max_tokens=150,  # Adjust the response length as needed
    )
    return response.choices[0].text.strip()


def main():
    os.system("clear" if os.name == "posix" else "cls")  # Clear terminal screen
    print("ChatGPT Terminal Interface")
    print("Type 'exit' to end the conversation.")
    print("=" * 30)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye!")
            break

        response = chat_with_gpt("User: " + user_input)
        print("ChatGPT:", response)


if __name__ == "__main__":
    main()

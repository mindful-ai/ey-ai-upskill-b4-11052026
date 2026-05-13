# Use Groq
from groq import Groq

# Read the key from the file
f = open(r"E:\Lenovo Ideapad 330\company-material\ai-upskill-3\key-vault\groq\groq-api-key.txt", "r")
api_key = f.read().strip()
f.close()

# Intialize the Groq client
client = Groq(api_key=api_key)

# Select a model
MODEL = "llama-3.1-8b-instant"


### VIBE CODED USING GITHUB COPILOT
# Create a function to generate responses from the model

def chat():
    # Welcome message
    print("Welcome to the Groq Chat Bot! Type 'exit' to quit.")

    # Create a message history list to store the conversation
    message_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    # Chat loop
    while True:
        # user input
        user_message = input("You: ")

        # Check if the user wants to exit
        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        # Append the user message to the message history
        message_history.append({"role": "user", "content": user_message})

        try:
            # Generate a response from the model using the message history as context
            response = client.chat.completions.create(
                model=MODEL,
                messages=message_history,
                max_tokens=150,
                temperature=0.7,
            )


            # Append the model response to the message history
            message_history.append({"role": "assistant", "content": response.choices[0].message.content})

            # Print the model response
            print(f"Assistant: {response.choices[0].message.content}")
            #print(f"Assistant: {response}")


        except Exception as e:
            print(f"An error occurred: {e}")
    

    print("Chat memory:", message_history)

# Launch the model
if __name__ == "__main__":
    chat()
    
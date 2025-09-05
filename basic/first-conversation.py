# Import prompt templates
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage  # Import system message schema
from langchain_ollama import ChatOllama  # updated import for OpenAI chat model
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Specify custom environment file path
custom_env_path = 'environment/local.env'
# Load environment variables from the specified file
load_dotenv(dotenv_path=custom_env_path, override=True)

# Initialize the Ollama chat model with parameters
llm = ChatOllama(model='llama3.2', temperature=0.1)

prompt = ChatPromptTemplate(
    input_variables=["content"],  # Define input variable for the prompt
    messages=[
        SystemMessage(
            # Set system message for the assistant's role
            content='You are a knowledgeable and professional financial advisor. Provide clear, accurate, and helpful financial advice to users.'),
        HumanMessagePromptTemplate.from_template(
            "{content}")  # Template for human input
    ]
)

# Use RunnableSequence pattern instead of LLMChain
chain = prompt | llm  # Create a chain by piping prompt to the model


def main():
    while True:
        user_input = input('Your prompt: ')  # Get user input
        if user_input.lower() in ['quit', 'exit', 'bye']:  # Check for exit commands
            print('Goodbye!')
            break

        # Use .invoke() instead of .run() to get model response
        # Pass user input to the chain
        response = chain.invoke({'content': user_input})
        print(response.content)  # Print the model's response
        print('-' * 50)  # Print a separator


if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly

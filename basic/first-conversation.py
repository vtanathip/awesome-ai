from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI  # updated import
from dotenv import load_dotenv

custom_env_path = 'environment/local.env'
load_dotenv(dotenv_path=custom_env_path, override=True)

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=1)

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        SystemMessage(
            content='You are a knowledgeable and professional financial advisor. Provide clear, accurate, and helpful financial advice to users.'),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# Use RunnableSequence pattern instead of LLMChain
chain = prompt | llm


def main():
    while True:
        user_input = input('Your prompt: ')
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print('Goodbye!')
            break

        # Use .invoke() instead of .run()
        response = chain.invoke({'content': user_input})
        print(response.content)
        print('-' * 50)


if __name__ == "__main__":
    main()

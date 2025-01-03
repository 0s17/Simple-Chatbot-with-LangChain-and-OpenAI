from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv(".env")
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.5,
        max_tokens=512,
        openai_api_key='API_KEY'
    )
    while True:
        prompt = input("Me : ")
        if prompt == 'exit':
            break
        response = llm.invoke(f'chat:{prompt}')
        print(response.content)
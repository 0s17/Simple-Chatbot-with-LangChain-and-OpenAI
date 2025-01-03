# 🤖 Chatbot with LangChain and OpenAI

This project demonstrates a simple chatbot using **LangChain** with **OpenAI's GPT-3.5 Turbo** model. It allows users to interact with the chatbot in a loop until they type `exit`.

---

## 📋 **Prerequisites**
Make sure you have the following installed:
- Python 3.8+
- `langchain-openai`
- `python-dotenv`
- OpenAI API key

Install dependencies using pip:
```bash
pip install langchain-openai python-dotenv
```

---

## 🛠️ **Environment Setup**
Create a `.env` file in your project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🚀 **Usage**
1. Clone the repository:
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```
2. Run the chatbot script:
```bash
lang chain.py
```
3. Start chatting with the bot!
- Type your questions.
- Type `exit` to quit.

---

## 💻 **Code Explanation**
```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv(".env")

# Initialize the chatbot with OpenAI's GPT-3.5 model
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.5,
    max_tokens=512,
    openai_api_key='API_KEY'
)

# Interactive chat loop
while True:
    prompt = input("Me : ")
    if prompt == 'exit':
        break
    response = llm.invoke(f'chat:{prompt}')
    print(response.content)
```
### Key Points:
- `load_dotenv` loads the API key securely.
- `ChatOpenAI` sets up the GPT-3.5 Turbo model.
- `invoke` sends prompts and retrieves responses.

---

## 📝 **Notes**
- Replace `'API_KEY'` with your actual OpenAI API key if not using `.env`.
- Ensure your API quota is sufficient.

---

## 🤝 **Contributing**
Feel free to fork this repository and submit pull requests!

---

## 📚 **Resources**
- [LangChain Documentation](https://docs.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

## 📄 **License**
This project is licensed under the **MIT License**.

---

Happy Coding! 🚀

# AZURE_AI_CHATBOT

A tiny robot assistant built with **Streamlit** and **Azure OpenAI**.  
Mini lives in the sidebar — always ready to chat: friendly, smart, and fast. 💬  

---

## 🧩 Features
- 🧠 Powered by **Azure OpenAI GPT-4**  
- 💬 Interactive chat UI using Streamlit’s chat components  
- 🤖 Robot avatar in the sidebar  
- 🔁 Reset conversation anytime  
- 🌈 Clean and modern dark theme  

---
```bash
🪜 STEP 1 — Install dependencies

pip install streamlit openai
⚙️ STEP 2 — Configure your Azure OpenAI credentials
Open app.py and replace with your own details:

python
Copy code
AZURE_ENDPOINT   = "https://<your-endpoint>.openai.azure.com/"
AZURE_API_KEY    = "<your-api-key>"
AZURE_DEPLOYMENT = "gpt-4.1-2"
AZURE_API_VERSION = "2024-12-01-preview"
▶️ STEP 3 — Run the app
bash
Copy code
streamlit run app.py
Then open your browser — Mini will be waiting to chat! 🤖💬

📁 Project Structure
csharp
Copy code
chat-with-mini/
├── app.py            # Streamlit app
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
🪄 Example Interaction
You: Hi Mini, what can you do?

Mini: Hello! I can answer your questions, explain things, or just chat with you 😊

🧠 Built With
Streamlit — for the interactive UI

Azure OpenAI — for the language model

👩‍💻 Author
BODDU SRAVANTHI
Built using Streamlit & Azure OpenAI

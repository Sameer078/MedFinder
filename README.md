# 💊🔍 MedFinder

MedFinder is a Streamlit-based application built with **LangChain** and **Google Gemini (Generative AI)** to answer questions about drugs and their side effects.  
Instead of generating unsupported answers, it retrieves accurate information strictly from a structured CSV dataset.  
If the information is not present in the data, MedFinder clearly states that the answer is unavailable.

---

## ✨ Features

- 📄 **CSV-based Knowledge Source**  
  Loads structured drug data (drug names, side effects, and related information) from a CSV file.

- 🧠 **Vector Search (RAG – Retrieval Augmented Generation)**  
  Converts drug data into embeddings using Google Generative AI and stores them in:
  - ChromaDB (persistent local vector database)
  - FAISS (fast in-memory similarity search)

- 🤖 **Gemini-powered Question Answering**  
  Uses Gemini-Pro to generate answers strictly from retrieved context.

- 🔍 **Context-Aware Responses**  
  Clearly responds with *“Answer is not available in the context”* when data is missing.

- 🌐 **Interactive Web Interface**  
  Simple and intuitive UI built with Streamlit.

---

## 🛠️ Tech Stack

| Component        | Technology Used                     |
|------------------|-------------------------------------|
| 🐍 Programming   | Python                              |
| 🤖 LLM           | Google Gemini (Gemini-Pro)          |
| 🔗 Framework     | LangChain                           |
| 📊 Vector DB     | ChromaDB / FAISS                   |
| 🎨 Frontend     | Streamlit                           |
| 📄 Data Source  | CSV (drugs_side_effects_drugs_com.csv) |

---

## 📂 Project Structure

```text
MedFinder/
├── app.py
├── requirements.txt
├── data/
│   └── drugs_side_effects_drugs_com.csv
├── vectorstore/
├── README.md
├── .env
```

---

## ⚙️ Installation & Setup (Using pip)

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/Sameer078/MedFinder
   cd MedFinder
   ```

2. 🧪 Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. 🔑 Set your Google API key:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```
   On Windows:
   ```bash
   set GOOGLE_API_KEY=your_api_key_here
   ```

---

## ⚡ Installation & Setup (Using uv)

`uv` is a fast Python package and environment manager.

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/Sameer078/MedFinder
   cd MedFinder
   ```

2. 📦 Initialize the project:
   ```bash
   uv init .
   ```

3. 🧪 Create a virtual environment:
   ```bash
   uv venv
   ```

4. ▶️ Activate the virtual environment:
   ```bash
   .venv/Scripts/activate
   ```
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

5. 📦 Install dependencies from requirements.txt:
   ```bash
   uv add -r requirements.txt
   ```

6. 🔑 Set your Google API key:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```
   On Windows:
   ```bash
   set GOOGLE_API_KEY=your_api_key_here
   ```

---

## 🧠 Vector Database Selection (Important)

MedFinder supports **two vector databases**: **ChromaDB** and **FAISS**.  
You must manually choose **one** by editing the code.

### 👉 How to Select a Vector Database

1. Open `app.py`
2. Locate the vector store initialization section
3. **Uncomment the block** for the vector database you want to use
4. **Comment out the other one**

⚠️ **Important Notes**
- Use **ChromaDB** if you want persistent storage across runs
- Use **FAISS** for faster, in-memory experimentation
- Only **one vector database should be active at a time**

---

## ▶️ How to Run the Project

🚀 Start the Streamlit application:

```bash
streamlit run app.py
```

---

## 🧑‍💻 Usage Example

1. 🚀 Launch the application  
2. ❓ Ask a question about a drug or its side effects  
3. 🔍 The system retrieves relevant data from the CSV  
4. 🤖 Gemini generates an answer strictly from the retrieved context  
5. ✅ If data is missing, the app responds with a clear “I don’t know”

---

## 🔮 Future Enhancements

- 📚 Support for multiple medical datasets  
- 🏥 Drug interaction and contraindication insights  
- 🧠 Conversation memory for follow-up questions  
- 📊 Dataset upload support via UI  
- 🎨 Enhanced UI with highlighted source references  

---


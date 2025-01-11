
---

# Web Scraping AI

![Web Scraping Simplified](https://www.cubeo.ai/wp-content/uploads/2024/05/Web-Scraper-Tools-LLMs-Integration.png)

**WEB AI: Web Scraping Simplified** is a Streamlit-powered application that makes web scraping intuitive and efficient. With advanced features like AI-powered content parsing, it helps you extract, process, and analyze website content with ease.

---

## 🚀 Features

- **URL Input:** Input any website URL for content extraction.
- **Web Scraping:** Extract and clean the main content of the specified website automatically.
- **DOM Content Viewer:** View the cleaned and processed DOM content in an interactive text area.
- **AI-Powered Parsing:** Use advanced AI methods to analyze and structure content based on your custom descriptions.
- **Expandable Sections:** Easily toggle visibility of extracted content for a better user experience.

---

## 🛠 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/JonathanJourney99/AI-Web-Scraper.git
   cd AI-Web-Scraper
   ```

2. **Install Dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Set Up a Compatible WebDriver:**
   - Install a web driver (e.g., ChromeDriver) compatible with your browser and operating system.

4. **Set Up Ollama:**
   - Install and run the Ollama LLM:
     ```bash
     ollama run llama3.2
     ```

   - For more details, visit [Ollama Documentation](https://ollama.com/search).

---

## ▶️ Usage

1. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Scrape a Website:**
   - Enter the desired website URL in the input box.
   - Click the **"Scrape Site"** button to extract content.

3. **Parse Content:**
   - Provide a description of what you want to analyze.
   - Click the **"Parse Content"** button to process the extracted DOM content using AI.

---

## 📁 Code Structure

- **`scrape.py`:** Core functions for scraping and cleaning website content:
  - `scrape_website(url)`: Fetches and returns HTML content of the specified URL.
  - `extract_body_content(html_content)`: Extracts the main body content from HTML.
  - `clean_body_content(body_content)`: Cleans and formats the extracted body content.
  - `split_dom_content(dom_content)`: Splits the DOM content into manageable chunks.
  
- **`parse.py`:** AI-based parsing functionality:
  - `parse_with_ollama(dom_chunks, parse_description)`: Processes DOM content with AI based on the user’s parsing requirements.

- **`app.py`:** Main Streamlit application, combining scraping and parsing features.

---

## 🌟 Key Technologies

- **Streamlit**: Interactive web app framework.
- **LangChain**: Integration for AI-based content processing.
- **Ollama LLM**: Advanced language model for parsing tasks.

---

## 🤝 Contributing

Contributions are welcome! Whether it's a new feature, bug fix, or suggestion, feel free to:

- Submit a pull request.
- Open an issue.

Please ensure your contributions adhere to the project's coding standards.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  

---

## 🔗 Useful Resources

- [Ollama Documentation](https://ollama.com/search)
- [LangChain Documentation](https://python.langchain.com/docs/integrations/llms/ollama/)

---

With **WEB AI: Web Scraping Simplified**, extract and analyze website content like a pro. 🚀  

---
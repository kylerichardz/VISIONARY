# ✨ Visionary: Text Simplification Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0+-red.svg)
![Google AI](https://img.shields.io/badge/Google%20AI-Gemini-yellow.svg)

A powerful text simplification tool that transforms complex text into clear, easy-to-understand content using Google's Gemini AI.

## 🌟 Features

- **Multiple Simplification Levels**: Choose between Gentle, Moderate, or Strong simplification
- **File Upload Support**: Process text from TXT, MD, and DOCX files
- **Text Statistics**: View word count and estimated reading time
- **Dark Theme**: Easy on the eyes with a modern dark interface
- **History Tracking**: Keep track of your recent simplifications
- **Export Options**: Download simplified text or copy to clipboard
- **Responsive Design**: Works on desktop and mobile devices

## 🚀 Live Demo

Try the app here: [Visionary App](your-streamlit-url-here)

## 💻 Installation

1. Clone the repository: 
bash
git clone https://github.com/your-username/visionary.git
cd visionary
```


2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Set up your Google AI API key:
   - Create a `.streamlit/secrets.toml` file
   - Add your API key:
     ```toml
     GOOGLE_API_KEY = "your-api-key-here"
     ```

5. Run the application:
```bash
streamlit run app.py
```


## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **File Processing**: python-docx
- **Styling**: Custom CSS

## 📁 Project Structure

visionary/
├── .streamlit/
│ └── secrets.toml
├── src/
│ ├── app.py
│ ├── ai_service.py
│ └── text_processor.py
├── requirements.txt
├── README.md
└── .gitignore


## 🔒 Security

- API keys are managed securely through Streamlit's secrets management
- Sensitive files are excluded via .gitignore
- No data is stored permanently

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kyle**

## 🙏 Acknowledgments

- Google AI for providing the Gemini Pro API
- Streamlit for the amazing web framework
- All contributors and users of this tool

---
Made with ❤️ by Kyle
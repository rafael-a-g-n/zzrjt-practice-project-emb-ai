# 🤖 AI Sentiment Analyzer

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![IBM Watson](https://img.shields.io/badge/IBM%20Watson-NLU-blue.svg)](https://www.ibm.com/watson)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Demo-Live-success.svg)](https://sentiment-analyzer-aacl.onrender.com/)

A modern, responsive web application that performs real-time sentiment analysis using IBM Watson Natural Language Understanding (NLU). Built with Flask and featuring a sleek, gradient-based UI with color-coded sentiment results.

## 🌟 Live Demo

**[Try it live here →](https://sentiment-analyzer-aacl.onrender.com/)**

## ✨ Features

- **Real-time Sentiment Analysis** - Instant analysis powered by IBM Watson NLU
- **Multi-language Support** - Analyzes text in English, Spanish, French, German, and more
- **Color-coded Results** - Visual feedback with distinct gradients:
  - 🟢 **Positive** - Green gradient
  - 🔴 **Negative** - Red gradient  
  - 🔵 **Neutral** - Blue gradient
- **Modern UI/UX** - Responsive design with smooth animations and gradient backgrounds
- **Keyboard Shortcuts** - Press Enter to analyze (Shift+Enter for new line)
- **Error Handling** - Comprehensive validation and user-friendly error messages
- **Loading States** - Visual feedback during API calls

## 🛠️ Technologies Used

### Backend
- **Python 3.13** - Core programming language
- **Flask 3.0** - Lightweight web framework
- **IBM Watson SDK** - Natural Language Understanding API
- **python-dotenv** - Environment variable management

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients, flexbox, and animations
- **JavaScript (ES6)** - Async API calls and DOM manipulation
- **SVG** - Custom favicon design

### DevOps & Tools
- **Git** - Version control
- **Render** - Cloud hosting platform
- **Pylint** - Code quality (10/10 score)
- **Flake8** - PEP8 compliance

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- IBM Cloud account with Watson NLU service
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rafael-a-g-n/zzrjt-practice-project-emb-ai.git
   cd zzrjt-practice-project-emb-ai
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   WATSON_NLU_API_KEY=your_api_key_here
   WATSON_NLU_URL=your_service_url_here
   ```
   
   Get your credentials from [IBM Cloud](https://cloud.ibm.com/catalog/services/natural-language-understanding)

5. **Run the application**
   ```bash
   python server.py
   ```

6. **Open in browser**
   
   Navigate to `http://localhost:8080`

## 📁 Project Structure

```
.
├── SentimentAnalysis/
│   ├── __init__.py              # Package initialization
│   └── sentiment_analysis.py    # Watson NLU integration
├── static/
│   ├── favicon.svg              # Custom favicon
│   ├── mywebscript.js          # Frontend JavaScript
│   └── style.css               # Responsive CSS styling
├── templates/
│   └── index.html              # Main HTML template
├── .env                        # Environment variables (not in repo)
├── .env.example               # Example environment file
├── server.py                   # Flask application entry point
├── test_sentiment_analysis.py  # Unit tests
├── requirements.txt            # Python dependencies
├── LICENSE                     # Apache 2.0 License
└── README.md                   # This file
```

## 🧪 Testing

Run the unit tests:

```bash
python -m pytest test_sentiment_analysis.py -v
```

Check code quality:

```bash
# Pylint
python -m pylint server.py SentimentAnalysis/

# Flake8
python -m flake8 .
```

## 🎨 Design Highlights

### Color Scheme
- **Primary Gradient**: Purple to violet (`#667eea` → `#764ba2`)
- **Positive Sentiment**: Green gradient
- **Negative Sentiment**: Red gradient
- **Neutral Sentiment**: Cyan gradient

### Responsive Breakpoints
- Desktop: > 768px
- Tablet: 768px
- Mobile: 480px

### Animations
- Fade-in on page load
- Button hover effects
- Smooth transitions

## 🔒 Security

- Environment variables for sensitive credentials
- Input validation and sanitization
- HTTPS ready for production
- No client-side credential exposure

## 📊 Skills Demonstrated

### Software Development
- ✅ Object-oriented programming
- ✅ RESTful API integration
- ✅ Error handling and validation
- ✅ Modular code architecture
- ✅ Unit testing

### Web Development
- ✅ Full-stack development (Frontend + Backend)
- ✅ Responsive web design
- ✅ AJAX/Asynchronous programming
- ✅ UX/UI best practices

### Cloud & AI
- ✅ IBM Watson AI integration
- ✅ Cloud deployment (Render)
- ✅ Natural Language Processing
- ✅ API authentication

### DevOps
- ✅ Git version control
- ✅ Virtual environments
- ✅ Code quality tools (Pylint, Flake8)
- ✅ Environment configuration

## 📝 API Usage

### Endpoint: `/sentimentAnalyzer`

**Method:** GET

**Parameters:**
- `textToAnalyze` (string, required) - Text to analyze

**Response:**
```json
{
  "status": 200,
  "message": "The given text has been identified as positive with a score of 0.95."
}
```

**Error Codes:**
- `400` - Blank input
- `500` - Invalid input or API error

## 🚀 Deployment

### Deploy to Render

1. Fork this repository
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Environment Variables**: Add `WATSON_NLU_API_KEY` and `WATSON_NLU_URL`
5. Deploy!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Template**: Based on the IBM Skills Network course template
- **Forked From**: [IBM Developer Skills Network - Embedded AI Libraries Project](https://github.com/ibm-developer-skills-network/xzceb-flask_eng_fr)
- **IBM Watson**: Natural Language Understanding API
- **Course**: IBM AI Engineering Professional Certificate on Coursera

## 👨‍💻 Author

**Rafael Nogueira**

- GitHub: [@rafael-a-g-n](https://github.com/rafael-a-g-n)
- Repository: [zzrjt-practice-project-emb-ai](https://github.com/rafael-a-g-n/zzrjt-practice-project-emb-ai)


<div align="center">
  
**[⬆ back to top](#-ai-sentiment-analyzer)**

Made with ❤️ using IBM Watson NLU

</div>

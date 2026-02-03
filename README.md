# AI Customer Support Agent

**Idea #2: AI Customer Support Agent** – Resolves tickets across chat, email, and voice while learning from past interactions.

## Project Overview

This is a proof-of-concept (POC) Streamlit web application that demonstrates AI-powered customer support ticket processing. The application uses Google Gemini 3 Flash Preview API to analyze support tickets, extract key issues and sentiment, and generate professional reply suggestions.

## Installation

**Python Version:** Python 3.8 or higher required (tested on Python 3.14.2)

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### API Key Configuration

1. Get your free Google Gemini API key from: https://makersuite.google.com/app/apikey
2. Create a `.env` file in the project root directory
3. Add your API key to the `.env` file:

```
GEMINI_API_KEY=your-api-key-here
```

**Important:** 
- Use only the **free tier** API key
- The `.env` file is automatically loaded by the app
- Do not commit the `.env` file to version control (it's in `.gitignore`)

## How to Run

Execute the following command in your terminal:

```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

If the browser doesn't open automatically, navigate to the URL shown in the terminal output.

## Usage

1. **Paste Ticket**: Copy and paste a customer support ticket into the text area
2. **Process**: Click the "Process Ticket" button
3. **Review Results**: 
   - View the AI-generated ticket summary (main issue and sentiment)
   - Review the suggested professional reply
4. **Download**: Optionally download the suggested reply as a text file

The AI analyzes the ticket content, identifies the main issue and customer sentiment, then generates an empathetic and professional response suggestion tailored to the ticket.

## Features

- **Real-time AI Processing**: Uses Google Gemini 3 Flash Preview API for live ticket analysis
- **Ticket Summarization**: Extracts main issues and customer sentiment
- **Reply Generation**: Suggests professional, empathetic responses
- **Download Functionality**: Export suggested replies as timestamped text files
- **Error Handling**: Clear error messages for API failures or missing configuration

## Technical Details

- **Framework**: Streamlit 1.53.0
- **AI Model**: Google Gemini 3 Flash Preview (free tier)
- **SDK**: google-genai (v0.2.0+)
- **Environment Management**: python-dotenv
- **Entry Point**: `app.py`

## Troubleshooting

- **"Please set GEMINI_API_KEY in .env file"**: Ensure `.env` file exists in project root with valid API key
- **API Errors**: Verify your API key is valid and you're using the free tier
- **Import Errors**: Run `pip install -r requirements.txt` to install all dependencies
- **Port Already in Use**: Streamlit will automatically use the next available port

## Project Structure

```
.
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── SCOPE_DOCUMENT.md     # Project proposal (Phase 1)
├── AI_DECLARATION.txt    # AI usage disclosure
├── .env                  # API key configuration (not in repo)
└── .gitignore           # Git ignore rules
```

## Requirements Compliance

✅ **Phase 2: Implementation**
- Source code provided (`app.py`)
- Clear run instructions in README
- Dependencies listed in `requirements.txt`
- Real AI processing (no hardcoded responses)
- Free-tier API usage only

## License

This project is part of an academic term project for the Artificial Intelligence course.

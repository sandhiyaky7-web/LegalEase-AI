# LegalEase - AI-Powered Legal Document Generator

LegalEase is an AI-powered application for generating editable drafts of common legal documents.

## Features

- Generate legal-document drafts using Gemini AI
- Support for different document types
- Enter parties, key terms, and dates
- Editable document preview
- Export documents as:
  - TXT
  - DOCX
  - PDF
- FastAPI backend
- Streamlit frontend
- Automated tests

## Project Structure

```text
LegalEase/
│
├── ai_core/
│   ├── __init__.py
│   ├── assets.py
│   ├── generator.py
│   ├── gemini_generator.py
│   └── formatters.py
│
├── frontend/
│   ├── __init__.py
│   └── app.py
│
├── legalEaseAPI/
│   ├── __init__.py
│   ├── main.py
│   └── routes.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_formatters.py
│
├── Image/
├── .env
├── .env.example
├── .gitignore
├── config.py
├── requirements.txt
├── README.md
└── run.sh
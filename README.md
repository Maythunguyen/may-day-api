## Journal Insights Service Backend

Enhanced AI insights feature for deeper emotional analysis. This feature aggregates entries related to the same person or event, allowing the AI to analyze and provide recommendations or alerts regarding their positive or negative impacts.

## Features
Single Journal Entry Analysis:

- Analyze individual journal entries for emotional insights and personal reflections.

- Empathetic and compassionate tone, similar to a professional therapist.

Bulk Journal Entries Analysis:

- Aggregates multiple journal entries, especially highlighting repeated mentions of people or events.

- Provides deeper emotional analysis, alerts, and recommendations based on positive or negative influences detected.

## Tech Stack
Framework: FastAPI

Language: Python

AI Integration: OpenAI API (GPT-4)

Data Validation: Pydantic

# Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/journal-ai-backend.git

#Navigate into the directory:

cd journal-ai-backend

#Create a virtual environment and activate it:

python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate

#Install dependencies:

pip install -r requirements.txt

#Environment Setup

#Create an .env file at the project root with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


#Running the Application

#Start the FastAPI server:

uvicorn app.main:app --reload

```
The API will be available at http://localhost:8000.

## API Endpoints
Root Endpoint (GET /):

Simple health check.

Single Analysis (POST /api/ai_analyse):

Analyzes a single journal entry.

Bulk Analysis (POST /api/ai_analyse_bulk):

Analyzes multiple journal entries to identify recurring emotional impacts.

## API Documentation

FastAPI provides automatic interactive documentation accessible via:

Swagger UI: http://localhost:8000/docs

ReDoc UI: http://localhost:8000/redoc

# Deployment
he recommended platform for deploying this backend service is Render - https://render.com/

## License
This project is licensed under the MIT License. See the LICENSE file for details
# Career Advisor AI 🎓🤖

Career Advisor is a web application designed to help students plan their careers. The app gives career roadmaps based on a user's academic status, specialization, and interests.

## ✨ Key Features

* `Persona-Based Guidance`: Uses system instructions to act as a career counselor.

* `Dynamic Form Handling`: The UI changes based on whether the user is a School Student or a College Student.

* `Optimized Performance`: Uses the gemini-2.5-flash-lite model for fast, high-quality responses with low token costs.

* `Markdown Formatting`: Delivers advice in a clean, readable markdown format.

* `Error Handling`: Includes a fallback if queries are outside the career advice scope.

## 🛠️ Tech Stack

* `Frontend`: Streamlit

* `LLM`: Google Gemini 2.5 Flash Lite

* `API Management`: google-genai SDK

* `Language`: Python 3.10+

## 🚀 Getting Started

### 1. Prerequisites

Get an API key from Google AI Studio.

### 2. Configuration

The application uses a custom keys.py file to manage credentials. Create a file named keys.py in the root directory:

    # python
    # keys.py
    api_key = "YOUR_GOOGLE_AI_STUDIO_API_KEY"

### 3. Installation

Install the required dependencies:

    # bash
    pip install streamlit google-genai
    
### 4. Running the Application

Launch the Streamlit server:

    bash
    streamlit run your_filename.py


## 🧠 Application Logic

* `System Instruction`: The model only answers career-related questions. If a user asks unrelated questions, the model returns: "Something went wrong Please Try Again".

* `Input Collection`:

    * `School Students`: Focuses on 11th-standard streams (Math, Commerce, Biology).

    * `College Students`: Focuses on specific degrees (Engineering, Science, Arts, etc.).

* `Processing`: A simulated 20-second loading state keeps the UI interactive while the prompt is sent to the Gemini API.

* `Generation`: The model uses a temperature=0.7 to balance creative career suggestions with educational pathways.

## 📁 Project Structure

1. `app.py`: The main application script with the Streamlit UI and Gemini integration.

2. `keys.py`: Local storage for the API key (should be in your .gitignore).

### 📅 Version Info

1. `Status`: Active 2025 Development

2. `Model`: Google Gemini 2.5 Flash Lite

3. `UI Version`: Streamlit Interactive Forms


# Image Analyzer

A Streamlit web application that allows users to upload images and ask questions about them using the Gemma 3 AI model.

## Features

- Upload images (PNG, JPG, JPEG)
- Ask natural language questions about images
- Get AI-powered analysis and responses
- Clean, modern dark theme interface

## Prerequisites

- Python 3.7+
- Ollama installed locally
- Gemma 3 model

## Installation

1. Install Ollama from [ollama.ai](https://ollama.ai)

2. Pull the Gemma 3 model:
   ```bash
   ollama pull gemma3:4b
   ```

3. Install required Python packages:
   ```bash
   pip install streamlit pillow requests
   ```

## Usage

1. Start the Ollama server:
   ```bash
   ollama serve
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to the provided URL (usually `http://localhost:8501`)

4. Use the app:
   - Upload an image using the file uploader
   - Enter your question in the text area
   - Click "Analyze Image" to get AI responses

## How It Works

The app connects to a locally running Ollama server that hosts the Gemma 3 model. When you upload an image and ask a question, the image is encoded and sent to the AI model along with your prompt. The model analyzes the image and provides a text response.

## Troubleshooting

- Make sure Ollama is running before starting the app
- Ensure the Gemma 3 model is properly installed (`ollama list` to check)
- Check that all Python dependencies are installed

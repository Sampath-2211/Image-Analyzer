# Image Analyzer

A Streamlit-based web application that allows users to upload images and ask questions about them using the Gemma 3 language model through Ollama.

## Features

- **Image Upload**: Support for PNG, JPG, and JPEG image formats
- **Interactive Q&A**: Ask natural language questions about uploaded images
- **Modern UI**: Dark theme with gradient buttons and clean design
- **Real-time Analysis**: Get instant responses about image content
- **Image Preview**: View uploaded images before analysis

## Prerequisites

Before running this application, ensure you have the following installed:

1. **Python 3.7+**
2. **Ollama** - Install from [ollama.ai](https://ollama.ai)
3. **Gemma 3 Model** - Pull the model using Ollama

### Install Ollama and Gemma 3

```bash
# Install Ollama (follow instructions for your OS at ollama.ai)

# Pull the Gemma 3 model
ollama pull gemma3:4b
```

## Installation

1. Clone or download the project files
2. Install required Python packages:

```bash
pip install streamlit pillow requests
```

## Usage

1. **Start Ollama server**:
   ```bash
   ollama serve
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

4. **Use the application**:
   - Upload an image using the file uploader
   - Optionally preview the image by clicking "Preview Image"
   - Enter your question about the image in the text area
   - Click "Analyze Image" to get AI-generated responses

## How It Works

The application uses:
- **Streamlit** for the web interface
- **PIL (Pillow)** for image processing
- **Ollama API** to communicate with the locally running Gemma 3 model
- **Base64 encoding** to send images to the AI model

The workflow:
1. User uploads an image and enters a question
2. Image is converted to base64 format
3. Request is sent to Ollama's local API endpoint
4. Gemma 3 model analyzes the image and responds to the question
5. Response is displayed in the web interface

## Configuration

The application is configured to:
- Connect to Ollama at `http://localhost:11434`
- Use the `gemma3:4b` model
- Set temperature to 0.1 for consistent responses
- Limit responses to 1000 tokens
- Timeout requests after 300 seconds

You can modify these settings in the `query_gemma()` function.

## Troubleshooting

**Connection Error**: 
- Ensure Ollama is running (`ollama serve`)
- Verify the Gemma 3 model is installed (`ollama list`)

**Model Not Found**:
- Pull the model: `ollama pull gemma3:4b`

**Slow Response Times**:
- The model runs locally, so performance depends on your hardware
- Consider using a smaller model variant if available

**Image Upload Issues**:
- Ensure image format is PNG, JPG, or JPEG
- Check image file size (very large images may cause timeouts)

## Customization

You can customize the application by:
- Modifying the CSS styles in the `st.markdown()` section
- Changing the model name in the `query_gemma()` function
- Adjusting temperature and token limits for different response styles
- Adding support for additional image formats

## Dependencies

- `streamlit` - Web application framework
- `pillow` - Image processing library
- `requests` - HTTP library for API calls
- `base64` - Built-in library for encoding
- `io` - Built-in library for byte operations

## License

This project is open source and available under standard usage terms.

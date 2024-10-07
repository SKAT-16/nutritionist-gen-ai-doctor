# Nutritionist Generative AI Doctor 🥗🧠

This application leverages Google's Gemini AI model to analyze food images and provide nutritional summaries, including health benefits and dietary advice. Upload an image of your meal, and the AI will summarize its content within 250 words.

## Demo

You can access the live demo of the app [here](https://nutritionist-gen-ai-doctor.streamlit.app/)

## Features

- **Image Upload**: Upload an image of your daily food (supported formats: `.jpg`, `.jpeg`, `.png`).
- **Nutritional Analysis**: AI-generated analysis of food's nutritional content and health benefits.
- **Streamlit Interface**: User-friendly and easy to navigate.

## Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.7+**
- **Google Gemini AI** API key
- Python packages:
  - `streamlit`
  - `google-generativeai`
  - `Pillow`
  - `python-dotenv`

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SKAT-16/nutritionist-gen-ai-doctor
   cd nutritionist-generative-ai-doctor
   ```

2. **Set up environment variables**:

   Create a `.env` file and add your Google API key:

   ```bash
   touch .env
   ```

   Inside `.env` file, add:

   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Install dependencies**:

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:

   To start the app, run:

   ```bash
   streamlit run app.py
   ```

5. **Access the app**:

   The app will launch in your web browser. You can upload images and get nutritional summaries from the AI.

## Usage

- **Input**: Upload an image of your food and input any additional context.
- **AI Summary**: The AI will analyze the food and provide a summary of the nutritional content, health benefits, and dietary advice.

## Example

Upload an image like this:

![Example](http://img.youtube.com/vi/example/0.jpg)

The AI will return something like:

- Nutritional Value: High in protein and fiber.
- Health Benefits: Great for heart health and digestion.
- Dietary Advice: Suitable for weight management and low-sugar diets.

## License

This project is licensed under the MIT License.

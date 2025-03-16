# Indian Languages Quiz Generator

A Streamlit application that generates quiz questions in various Indian languages using Google's Gemini AI model.

![Indian Languages Quiz Generator](https://i.imgur.com/JQXpJXB.png)

## Features

- **Multilingual Support**: Generate quizzes in 6 Indian languages:
  - Telugu
  - Hindi
  - Tamil
  - Kannada
  - Malayalam
  - Bengali

- **Customizable Topics**: Create quizzes on various subjects including:
  - Indian History
  - Geography
  - Science & Technology
  - Indian Culture
  - Sports
  - Current Affairs

- **Flexible Configuration**:
  - Choose the number of questions (5-20)
  - Select your preferred language
  - Enter any topic of interest

- **User-Friendly Interface**:
  - Separate tabs for questions and answers
  - Clean, intuitive design
  - Real-time generation with progress indicator

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/satvik314/indian_language_quiz.git
   cd indian_language_quiz
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a file at `streamlit/secrets.toml`
   - Add your Google API key:
     ```toml
     GOOGLE_API_KEY = "your-google-api-key"
     ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run indian_quiz.py
   ```

2. In the sidebar:
   - Select your preferred language
   - Enter a topic for the quiz
   - Adjust the number of questions
   - Click "Generate Quiz"

3. View the generated quiz:
   - Questions tab: Shows all questions with multiple-choice options
   - Answer Key tab: Provides correct answers with explanations

## How It Works

The application uses:
- **Streamlit**: For the web interface
- **Educhain**: To structure and format educational content
- **LangChain**: To interface with Google's Generative AI
- **Google Gemini**: To generate contextually relevant quiz questions in multiple languages

The system uses carefully crafted prompts in each language to ensure proper formatting and cultural relevance of the generated questions.

## Requirements

- Python 3.7+
- streamlit
- educhain
- langchain-google-genai
- Google API key with access to Gemini models

## Use Cases

- Educational institutions teaching Indian languages
- Students preparing for exams on Indian culture and languages
- Language enthusiasts wanting to test their knowledge
- Teachers creating multilingual educational content

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini](https://ai.google.dev/)
- Uses [Educhain](https://github.com/educhain-official/educhain) for educational content structuring
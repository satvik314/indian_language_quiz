import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from educhain import Educhain, LLMConfig

# Initialize Gemini model
def init_llm():
    gemini = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=st.secrets["GOOGLE_API_KEY"]
    )
    gemini_config = LLMConfig(custom_model=gemini)
    return Educhain(gemini_config)

# Language prompt templates
LANGUAGE_TEMPLATES = {
    "Telugu": """
తెలుగులో {num} బహుళైచ్ఛిక ప్రశ్నలను సృష్టించండి.
అంశం: {topic}

ప్రతి ప్రశ్నకు:
1. ప్రశ్న
2. నాలుగు సమాధాన ఎంపికలు (ఎ, బి, సి, డి)
3. సరైన సమాధానం
4. వివరణ
    """,
    
    "Hindi": """
हिंदी में {num} बहुविकल्पीय प्रश्न बनाएं।
विषय: {topic}

प्रत्येक प्रश्न के लिए:
1. प्रश्न
2. चार विकल्प (क, ख, ग, घ)
3. सही उत्तर
4. व्याख्या
    """,
    
    "Tamil": """
தமிழில் {num} பல்தேர்வு வினாக்களை உருவாக்கவும்.
தலைப்பு: {topic}

ஒவ்வொரு கேள்விக்கும்:
1. கேள்வி
2. நான்கு விருப்பங்கள் (அ, ஆ, இ, ஈ)
3. சரியான பதில்
4. விளக்கம்
    """,
    
    "Kannada": """
ಕನ್ನಡದಲ್ಲಿ {num} ಬಹು ಆಯ್ಕೆ ಪ್ರಶ್ನೆಗಳನ್ನು ರಚಿಸಿ.
ವಿಷಯ: {topic}

ಪ್ರತಿ ಪ್ರಶ್ನೆಗೆ:
1. ಪ್ರಶ್ನೆ
2. ನಾಲ್ಕು ಆಯ್ಕೆಗಳು (ಎ, ಬಿ, ಸಿ, ಡಿ)
3. ಸರಿಯಾದ ಉತ್ತರ
4. ವಿವರಣೆ
    """,
    
    "Malayalam": """
മലയാളത്തിൽ {num} ബഹുവരണ ചോദ്യങ്ങൾ സൃഷ്ടിക്കുക.
വിഷയം: {topic}

ഓരോ ചോദ്യത്തിനും:
1. ചോദ്യം
2. നാല് ഓപ്ഷനുകൾ (എ, ബി, സി, ഡി)
3. ശരിയായ ഉത്തരം
4. വിശദീകരണം
    """,
    
    "Bengali": """
বাংলায় {num} টি বহুনির্বাচনী প্রশ্ন তৈরি করুন।
বিষয়: {topic}

প্রতিটি প্রশ্নের জন্য:
1. প্রশ্ন
2. চারটি বিকল্প (ক, খ, গ, ঘ)
3. সঠিক উত্তর
4. ব্যাখ্যা
    """
}

# Streamlit UI
st.title("🎯 Indian Languages Quiz Generator")
st.write("Generate quiz questions in various Indian languages!")

# Sidebar for inputs
with st.sidebar:
    st.header("Quiz Settings")
    language = st.selectbox(
        "Select Language",
        options=list(LANGUAGE_TEMPLATES.keys()),
        index=0
    )
    
    topic = st.text_input("Enter Topic", "Indian History")
    num_questions = st.slider("Number of Questions", 5, 20, 10)
    
    st.markdown("---")
    st.markdown("### Topics Suggestions:")
    st.markdown("""
    - Indian History
    - Geography
    - Science & Technology
    - Indian Culture
    - Sports
    - Current Affairs
    """)

# Main content
if st.button("Generate Quiz"):
    with st.spinner(f"Generating {num_questions} questions in {language}..."):
        try:
            client = init_llm()
            
            # Generate questions using the selected language template
            questions = client.qna_engine.generate_questions(
                topic=topic,
                num=num_questions,
                prompt_template=LANGUAGE_TEMPLATES[language]
            )
            
            # Display questions
            st.success("✅ Quiz generated successfully!")
            st.markdown("---")
            
            # Create tabs for Questions and Answer Key
            q_tab, a_tab = st.tabs(["Questions", "Answer Key"])
            
            with q_tab:
                for i, q in enumerate(questions.questions, 1):
                    st.markdown(f"### Question {i}")
                    st.write(q.question)
                    
                    # Display options in columns
                    cols = st.columns(2)
                    for j, option in enumerate(q.options):
                        with cols[j//2]:
                            st.write(option)
                    
                    st.markdown("---")
            
            with a_tab:
                for i, q in enumerate(questions.questions, 1):
                    st.markdown(f"### Question {i} - Answer")
                    st.write(f"**Correct Answer:** {q.answer}")
                    st.write(f"**Explanation:** {q.explanation}")
                    st.markdown("---")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please try again or check your API key configuration.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Educhain and Gemini")
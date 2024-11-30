import streamlit as st
from ai_service import simplify_text
import text_processor as tp
from datetime import datetime

# Basic page config
st.set_page_config(
    page_title="Visionary - Text Simplification",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Custom CSS
st.markdown("""
    <style>
    /* Force all text to be white */
    .stTextInput, .stTextArea, textarea, .stMarkdown, p, span {
        color: white !important;
    }
    
    /* Make placeholder text slightly dimmer but still visible */
    textarea::placeholder {
        color: #cccccc !important;
    }
    
    /* Ensure input text is white */
    textarea[data-baseweb="textarea"] {
        color: white !important;
    }
    
    /* Make radio button text white */
    .stRadio label {
        color: white !important;
    }
    
    /* Result text containers with enforced white text */
    .text-display {
        background-color: #363636;
        padding: 20px;
        border-radius: 10px;
        height: 400px;
        overflow-y: auto;
        border: 1px solid #404040;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);
        color: white !important;
        font-size: 1.1em;
        line-height: 1.5;
    }
    
    /* Force white text in all text areas */
    div[data-baseweb="base-input"] textarea {
        color: white !important;
    }
    
    /* Overall dark theme */
    [data-testid="stAppViewContainer"] {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Main title styling */
    h1 {
        color: #00B4D8;
        padding-bottom: 20px;
        border-bottom: 2px solid #00B4D8;
        margin-bottom: 30px;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: #cccccc;
        font-size: 1.2em;
        font-style: italic;
        margin-bottom: 30px;
    }
    
    /* Card-like containers */
    .stTextInput, .stTextArea {
        background-color: #2d2d2d !important;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.4);
        border: 1px solid #404040;
    }
    
    /* Text area specific styling */
    textarea {
        border: 2px solid #00B4D8 !important;
        color: #ffffff !important;
        background-color: #2d2d2d !important;
        font-size: 1.1em !important;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #00B4D8;
        color: white;
        padding: 10px 25px;
        border-radius: 25px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
        font-weight: bold;
        font-size: 1.1em;
    }
    
    .stButton>button:hover {
        background-color: #0096c7;
        box-shadow: 0 4px 8px rgba(0,0,0,0.6);
        transform: translateY(-2px);
    }
    
    /* Results container styling */
    .results-container {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px solid #404040;
        box-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }
    
    /* Headers in results */
    .results-container h3 {
        color: #00B4D8;
        margin-bottom: 15px;
        font-weight: bold;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        background: #2d2d2d;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #404040;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #4a4a4a;
    }
    
    /* Footer styling */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #1a1a1a;
        padding: 10px;
        text-align: center;
        font-size: 0.8em;
        color: #888;
        border-top: 1px solid #404040;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: rgba(0, 180, 216, 0.2) !important;
        color: #ffffff !important;
    }
    
    /* Error message styling */
    .stError {
        background-color: rgba(255, 76, 76, 0.2) !important;
        color: #ffffff !important;
    }
    
    .copy-button {
        background-color: #404040;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        border: 1px solid #505050;
        cursor: pointer;
        float: right;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.title("✨ Visionary: Text Simplification Tool")
st.markdown('<p class="subtitle">Transform complex text into clear, easy-to-understand content.</p>', unsafe_allow_html=True)

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

def get_text_stats(text):
    words = len(text.split())
    # Average reading speed: 200 words per minute
    reading_time = round(words / 200)
    return words, reading_time

# Input method selection
input_method = st.radio(
    "Choose input method:",
    ["✏️ Text Input", "📁 File Upload"]
)

# Add simplification level selector before text input
simplification_level = st.select_slider(
    "Select simplification level:",
    options=["Gentle", "Moderate", "Strong"],
    value="Moderate",
    help="Choose how much to simplify the text"
)

text_to_simplify = ""

if "✏️ Text Input" in input_method:
    text_to_simplify = st.text_area(
        "Enter your text:",
        height=200,
        placeholder="Paste your complex text here, and we'll make it clearer..."
    )
else:
    uploaded_file = st.file_uploader(
        "Upload a text file",
        type=["txt", "md", "doc", "docx"]
    )
    if uploaded_file:
        try:
            text_to_simplify = tp.process_uploaded_file(uploaded_file)
            st.success("File uploaded successfully!")
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

# Center the button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    process_button = st.button("✨ Simplify Text", use_container_width=True)

if process_button and text_to_simplify:
    with st.spinner(""):
        st.markdown("""
            <div style='text-align: center; color: #00B4D8;'>
                <h3>✨ Magic in progress ✨</h3>
                <p>Transforming your text...</p>
            </div>
        """, unsafe_allow_html=True)
        try:
            # Pass the simplification level to the API
            simplified_text = simplify_text(text_to_simplify, level=simplification_level)
            
            # Calculate stats
            orig_words, orig_time = get_text_stats(text_to_simplify)
            simp_words, simp_time = get_text_stats(simplified_text)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 📝 Original Text")
                st.markdown(f"Words: {orig_words} | Reading time: {orig_time} min")
                st.markdown(f'<div class="text-display">{text_to_simplify}</div>', unsafe_allow_html=True)
                st.markdown("""
                    <button class="copy-button" onclick="navigator.clipboard.writeText(document.querySelector('.original-text').innerText)">
                        📋 Copy
                    </button>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### ✨ Simplified Text")
                st.markdown(f"Words: {simp_words} | Reading time: {simp_time} min")
                st.markdown(f'<div class="text-display">{simplified_text}</div>', unsafe_allow_html=True)
                st.markdown("""
                    <button class="copy-button" onclick="navigator.clipboard.writeText(document.querySelector('.simplified-text').innerText)">
                        📋 Copy
                    </button>
                """, unsafe_allow_html=True)
            
            if simplified_text:
                st.download_button(
                    label="📥 Download Results",
                    data=f"""Original Text:\n{text_to_simplify}\n\nSimplified Text:\n{simplified_text}""",
                    file_name="simplified_text.txt",
                    mime="text/plain"
                )
            
            # After successful simplification
            st.session_state.history.append({
                'original': text_to_simplify,
                'simplified': simplified_text,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
        except Exception as e:
            st.error("""
                😕 Oops! Something went wrong.
                Try refreshing the page or using a shorter text.
                
                Technical details: {}
            """.format(str(e)))

if not text_to_simplify and process_button:
    st.info("ℹ️ Please enter some text to simplify!")

# Add a history section
if st.sidebar.checkbox("Show History"):
    st.sidebar.write("### Recent Simplifications")
    for item in reversed(st.session_state.history[-5:]):  # Show last 5
        with st.sidebar.expander(f"🕒 {item['timestamp']}"):
            st.write("**Original:**", item['original'][:100] + "...")
            st.write("**Simplified:**", item['simplified'][:100] + "...")

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by Quinn | Powered by Google AI
    </div>
""", unsafe_allow_html=True)

if len(text_to_simplify) > 5000:  # Adjust limit as needed
    st.warning("⚠️ Long texts may take more time to process. Consider breaking it into smaller chunks.")
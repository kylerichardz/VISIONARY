import streamlit as st
import google.generativeai as genai

def init_genai():
    """Initialize Google GenerativeAI with API key."""
    api_key = st.secrets["GOOGLE_API_KEY"]
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in secrets")
    genai.configure(api_key=api_key)

def simplify_text(text: str, level: str = "Moderate") -> str:
    """
    Simplify text using Google's GenerativeAI.
    
    Args:
        text (str): The text to simplify
        level (str): Simplification level ("Gentle", "Moderate", or "Strong")
        
    Returns:
        str: Simplified text
    """
    init_genai()
    
    # Initialize model
    model = genai.GenerativeModel('gemini-pro')
    
    # Adjust prompt based on simplification level
    level_instructions = {
        "Gentle": "Make this text slightly easier to understand while keeping most of the original language:",
        "Moderate": "Simplify this text to make it clearer and more accessible for a general audience:",
        "Strong": "Significantly simplify this text for maximum clarity and accessibility:"
    }
    
    # Craft the prompt
    prompt = f"""
    {level_instructions.get(level, level_instructions["Moderate"])}
    
    {text}
    
    Simplified version:
    """
    
    # Generate response
    response = model.generate_content(prompt)
    
    return response.text 
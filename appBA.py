import streamlit as st
import random

# --- 1. CONFIGURATION & STATE MANAGEMENT ---
st.set_page_config(page_title="ROBIN", layout="wide", page_icon="🐦")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Initialize session state for selections
if 'selections' not in st.session_state:
    st.session_state.selections = {}

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def toggle_selection(key):
    st.session_state.selections[key] = not st.session_state.selections.get(key, False)

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    /* Global Variables */
    :root {
        --app-bg: #1b263b;
        --box-bg: #0d1b2a;
        --text-mint: #76c8b9;
        --text-dark: #0d1b2a;
    }

    .stApp {
        background-color: var(--app-bg);
        color: var(--text-mint);
    }

    /* =========================================
       1. GLOBAL BIG BOXES (Home/Ideas)
       This targets ALL Primary buttons by default
       ========================================= */
    div.stButton > button[kind="primary"] {
        background-color: var(--box-bg) !important;
        color: var(--text-mint) !important;
        border: none !important;
        border-radius: 15px !important;
        
        font-size: 22px !important; 
        text-align: left !important;
        white-space: pre-wrap !important;
        font-family: 'Helvetica', sans-serif !important;
        
        width: 100% !important;
        min-height: 50vh !important; /* THE GIANT HEIGHT */
        padding: 40px !important;
        margin-top: 20px !important;
        
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: var(--text-mint) !important; 
        color: var(--text-dark) !important;            
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4) !important;
    }
    
    div.stButton > button[kind="primary"]:hover p {
        color: var(--text-dark) !important;
    }

    /* =========================================
       2. BACK BUTTON (The Bat)
       ========================================= */
    div.stButton > button[kind="secondary"] {
        background-color: var(--text-mint) !important; 
        border: none !important;
        border-radius: 12px !important;
        color: transparent !important;  
        text-shadow: 0 0 0 var(--text-dark) !important; 
        font-size: 50px !important;
        line-height: 50px !important;
        height: auto !important;
        width: auto !important;
        padding: 10px 20px !important;
        min-height: 0px !important;
        transition: transform 0.2s ease !important;
    }
    
    div.stButton > button[kind="secondary"]:hover {
        transform: scale(1.1) !important; 
        background-color: #ffffff !important; 
    }

    /* =========================================
       3. SUBMIT BUTTON (Tertiary)
       ========================================= */
    div.stButton > button[kind="tertiary"] {
        background-color: var(--text-mint) !important;
        color: var(--text-dark) !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: auto !important;
        padding: 15px !important;
        min-height: 0px !important;
        margin-top: 20px !important;
    }
    
    div.stButton > button[kind="tertiary"]:hover {
        background-color: #ffffff !important;
        transform: scale(1.01) !important;
    }

    /* =========================================
       4. SMALL SELECTION GRID OVERRIDES
       This fixes the "Giant Box" issue on selection
       ========================================= */
    
    /* Target ANY button inside the .small-grid wrapper */
    div.small-grid button {
        min-height: 0px !important;  /* KILL THE GIANT HEIGHT */
        height: auto !important;
        padding: 15px !important;
        font-size: 16px !important;
        text-align: center !important;
        width: 100% !important;
        margin-top: 5px !important;
        box-shadow: none !important;
    }

    /* UNSELECTED STATE (Inside Grid) */
    /* We use 'secondary' logic here but override appearance */
    div.small-grid button[kind="secondary"] {
        background-color: var(--box-bg) !important; /* Dark Blue */
        color: var(--text-mint) !important;

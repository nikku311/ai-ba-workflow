import streamlit as st
# Importing functions from module folder
from modules.requirement_generator import generate_user_story

# Set page title and icon
st.set_page_config(page_title="AI BA Workflow", page_icon="🤖")
st.title("🤖 AI Business Analyst Workflow")
st.markdown("---")

# For sidebar setting
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["gemini-2.5-flash (Free)", "gemini-2.5-pro (Better)"]
)

st.sidebar.info("✅ Using Google Gemini - Free Tier!")

# Main Area
st.header("📝 Requirement to User Story")

requirement = st.text_area(
    "Enter your business requirement:",
    placeholder="Example: I want an e-commerce app where users can buy products...",
    height=150
)

# When user clicks "Generate" button
if st.button("🚀 Generate User Story", type="primary"):
    if requirement:
        with st.spinner("AI soch raha hai... ⏳"):
            # Bring result by calling function
            result = generate_user_story(requirement, model_choice)
            
        st.success("✅ User Story Generated!")
        st.markdown("### 📄 Output:")
        st.markdown(result)
        st.code(result, language="markdown")
    else:
        st.warning("⚠️ Pehle kuch requirement toh likho!")

st.markdown("---")
st.caption("Powered by Google Gemini | Made with ❤️ for aspiring BAs")

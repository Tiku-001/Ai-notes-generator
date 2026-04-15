import streamlit as st
import ollama

st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

.main {
    background-color: #0e1117;
}

h1 {
    color: #00adb5;
    text-align: center;
}

textarea {
    background-color: #1e1e1e !important;
    color: white !important;
    border-radius: 10px !important;
}

button {
    background-color: #00adb5 !important;
    color: white !important;
    border-radius: 10px !important;
}

.sidebar .sidebar-content {
    background-color: #1e1e1e;
}
</style>
""", unsafe_allow_html=True)
# Page setup
st.set_page_config(page_title="AI Notes Generator", page_icon="🧠")

# Title
st.markdown("""
<h1>🧠 AI Notes Generator</h1>
<p style='text-align: center; color: gray;'>
Turn boring text into smart notes instantly 🚀
</p>
""", unsafe_allow_html=True)
st.markdown("### 📚 Turn long text into smart study notes instantly")

# Sidebar options
st.sidebar.title("Options")
mode = st.sidebar.selectbox("Select Mode", ["Full Notes", "Summary", "Exam Prep"])

# Input box
user_input = st.text_area("Enter your text here:")

# Buttons
col1, col2 = st.columns(2)

generate = col1.button("Generate Notes")
clear = col2.button("Clear")

# Clear functionality
if clear:
    st.rerun()

# Generate output
if generate:
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        with st.spinner("Generating... Please wait ⏳"):

            # Prompt based on mode
            if mode == "Summary":
                prompt = f"Give a short and clear summary:\n{user_input}"

            elif mode == "Exam Prep":
                prompt = f"""
Generate:
1. Important Questions
2. Short Answers

Text:
{user_input}
"""

            else:
                prompt = f"""
Convert this into:
1. Short Summary
2. Bullet Points
3. Simple Explanation
4. 3 Important Questions

Text:
{user_input}
"""

            # Call Ollama
            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response['message']['content']

            # Display output
            st.subheader("📌 Generated Notes")
            st.markdown(f"""
<div style="
background-color:#1e1e1e;
padding:20px;
border-radius:15px;
box-shadow:0px 0px 10px rgba(0,0,0,0.5);
">
<h3 style="color:#00adb5;">📌 Generated Notes</h3>
<p>{output}</p>
</div>
""", unsafe_allow_html=True)

            # Download button
            st.download_button(
                label="📥 Download Notes",
                data=output,
                file_name="notes.txt"
            )

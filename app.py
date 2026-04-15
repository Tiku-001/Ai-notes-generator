import streamlit as st
import ollama

# Page setup
st.set_page_config(page_title="AI Notes Generator", page_icon="🧠")

# Title
st.title("🧠 AI Notes Generator")
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
            st.text_area("Output", output, height=300)

            # Download button
            st.download_button(
                label="📥 Download Notes",
                data=output,
                file_name="notes.txt"
            )
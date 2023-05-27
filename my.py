import streamlit as st
import openai
import os
import time

api_key = os.environ.get('OPENAI_API_KEY')

def BasicGeneration(userprompt, words, creativity):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=words,
        temperature=creativity,
        messages=[
            {"role": "user", "content": userprompt}
        ]
    )
    return completion.choices[0].message.content

def generate_blog():
    topic = st.text_input("Enter your topic:")
    
    if st.button("Generate Headline"):
        prompt = f"write an eye-catching and interacting headline for my blog about {topic}"
        words = 20
        creativity = 1
        headline = BasicGeneration(prompt, words, creativity)
        st.write("Generated Headline:")
        st.write(headline)
    
    if st.button("Generate Outlines"):
        prompt = f"write atleast 10 eye-catching and interacting outlines or subtopics for my blog about {headline}"
        words = 200
        creativity = 1
        outlines = BasicGeneration(prompt, words, creativity)
        st.write("Generated Outlines:")
        st.write(outlines)
    
    # Wait for 20 seconds
    time.sleep(60)
    
    generated_outlines = []
    
    for i, outline in enumerate(outlines.split("\n")[:3], 1):
        prompt = f"write a paragraph for my blog about {outline}.\n\n{outline}\n{'-' * len(outline)}\n"
        words = 500
        creativity = 1
        generated_outline = BasicGeneration(prompt, words, creativity)
        generated_outlines.append(generated_outline)
    
    # Wait for 20 seconds
    time.sleep(60)
    
    for i, outline in enumerate(outlines.split("\n")[3:6], 4):
        prompt = f"write a paragraph for my blog about {outline}.\n\n{outline}\n{'-' * len(outline)}\n"
        words = 500
        creativity = 1
        generated_outline = BasicGeneration(prompt, words, creativity)
        generated_outlines.append(generated_outline)
    
    # Wait for 20 seconds
    time.sleep(60)
    
    for i, outline in enumerate(outlines.split("\n")[6:9], 7):
        prompt = f"write a paragraph for my blog about {outline}.\n\n{outline}\n{'-' * len(outline)}\n"
        words = 500
        creativity = 1
        generated_outline = BasicGeneration(prompt, words, creativity)
        generated_outlines.append(generated_outline)
    
    # Wait for 20 seconds
    time.sleep(60)
    
    outline = outlines.split("\n")[9]  # Select the last outline
    
    prompt = f"write a paragraph for my blog about {outline}.\n\n{outline}\n{'-' * len(outline)}\n"
    words = 500
    creativity = 1
    generated_outline = BasicGeneration(prompt, words, creativity)
    generated_outlines.append(generated_outline)
    
    # Print the generated outlines
    st.write("Generated Outlines:")
    for i, outline in enumerate(generated_outlines, 1):
        st.write(f"{i}. {outline}")

# Run the Streamlit app
if __name__ == "__main__":
    st.title("Blog Generator")
    generate_blog()

import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110, background_color='white').generate(text)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    st.pyplot(plt)

def main():
    st.title("Word Cloud Generator")

    # File upload widget
    uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")

    if uploaded_file is not None:
        st.write("### File Uploaded Successfully!")

        # Read the Excel file using pandas
        df = pd.read_excel(uploaded_file)

        # Column selection
        content_column = st.selectbox("Select the content column", df.columns)

        # Concatenate all text from the selected column
        all_text = ' '.join(str(text) for text in df[content_column])

        # Generate and display the word cloud
        generate_wordcloud(all_text)

if __name__ == "__main__":
    main()
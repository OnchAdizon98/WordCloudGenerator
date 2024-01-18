import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import string

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110, background_color='white').generate(text)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    st.pyplot(plt)

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    result_string = input_string.translate(translator)

    return result_string

with open('stopwords.json', 'r') as json_file:
    stopwords_list = json.load(json_file)["STOPWORDS"]
   # print(stopwords_list)

def main():
    st.title("Word Cloud Generator")

    uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")

    if uploaded_file is not None:
        st.write("### File Uploaded Successfully!")

        df = pd.read_excel(uploaded_file)

        content_column = 'Content'

        original_text = ' '.join(str(text) for text in df[content_column])


        edited_text = remove_punctuation(original_text)

        text_to_list = edited_text.split()

        filtered_word_list = [word for word in text_to_list if word not in stopwords_list]

        filtered_word_string = ' '.join(filtered_word_list)

        generate_wordcloud(filtered_word_string)


if __name__ == "__main__":
    main()

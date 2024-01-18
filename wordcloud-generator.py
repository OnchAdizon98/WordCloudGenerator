import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import string
import numpy as np
from PIL import Image

def generate_wordcloud(text):

    mask = np.array(Image.open(r'circle2.png'))

    wordcloud = WordCloud(
        width = mask.shape[1],
        height = mask.shape[0],
        background_color ='white',
        stopwords = stopwords_list,
        max_font_size = 250,
        min_font_size = 10,
        max_words=100,
        font_path='Benne-Regular.otf',
        prefer_horizontal=1,
        mask=mask
        ).generate(text)
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
    st.title("MMI Word Cloud Generator")

    uploaded_file = st.file_uploader("Upload your Excel file", type="xlsx")

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

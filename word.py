import streamlit as st
import json
import os

WORDS_FILE = 'words.json'

def load_words():
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_words(words):
    with open(WORDS_FILE, 'w') as file:
        json.dump(words, file)

# 加载现有的单词
words = load_words()

st.title("Note Saver")

# 输入单词的表单
new_word = st.text_input("Enter a note:")

if st.button("Save note"):
    if new_word:
        words.append(new_word)
        save_words(words)
        st.success(f"The word '{new_word}' has been saved!")
        st.experimental_rerun()  # 重新运行以刷新页面并显示新单词

# 显示所有保存的单词
st.header("Saved Notes")
for word in words:
    st.write(f"- {word}")

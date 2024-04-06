import streamlit as st
from textblob import TextBlob

st.write("Translator app")
st.write("You can translate into these languages: Chinese, Spanish, German, and French")

st.write("Enter text and choose your language:")

text = st.text_input("Enter input:", "")

cs = ["Chinese", "Spanish", "Greman", "French"] 
classification_space = st.sidebar.selectbox("Language to be translated into:", cs)
option = ''

if classification_space == "Chinese":
    option = 'zh'
elif classification_space == "Spanish":
    option = 'es'
elif classification_space == "Greman":
    option = 'de'
elif classification_space == "French":
    option = 'fr'

# for language codes have a look at https://cloud.google.com/translate/docs/languages
# complete the language translation option for spanish, german and french
if st.button('Translate'):
    blob = TextBlob(text)
    Pronounce = blob.translate(to = option)  
    st.write(Pronounce)

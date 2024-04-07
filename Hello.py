import streamlit as st
# from textblob import TextBlob
import argostranslate.package
import argostranslate.translate

st.write("Translator app")
st.write("You can translate into these languages: Chinese, Spanish, German, and French")

st.write("Enter text and choose your language:")

text = st.text_input("Enter input:", "")

cs = ["Chinese", "Spanish", "Greman", "French"] 
classification_space = st.sidebar.selectbox("Language to be translated into:", cs)

# install argostranslate
from_code = "en"
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

if classification_space == "Chinese":
    to_code = 'zh'
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
elif classification_space == "Spanish":
    to_code = 'es'
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
elif classification_space == "Greman":
    to_code = 'de'
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
elif classification_space == "French":
    to_code = 'fr'
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

# for language codes have a look at https://cloud.google.com/translate/docs/languages
# complete the language translation option for spanish, german and french
if st.button('Translate'):
    # Translate
    translatedText = argostranslate.translate.translate(text, from_code, option)
    st.write(translatedText)

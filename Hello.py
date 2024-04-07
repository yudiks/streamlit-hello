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
option = ''

# install argostranslate
from_code = "en"
to_code = "es"
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

if classification_space == "Chinese":
    option = 'zh'
    to_code = 'zh'
    # Download and install Argos Translate package
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
elif classification_space == "Spanish":
    option = 'es'
elif classification_space == "Greman":
    option = 'de'
elif classification_space == "French":
    option = 'fr'


# for language codes have a look at https://cloud.google.com/translate/docs/languages
# complete the language translation option for spanish, german and french
if st.button('Translate'):
    # Translate
    translatedText = argostranslate.translate.translate(text, from_code, option)
    # print(translatedText)

    # blob = TextBlob(text)
    # Pronounce = blob.translate(to = option)  
    st.write(translatedText)

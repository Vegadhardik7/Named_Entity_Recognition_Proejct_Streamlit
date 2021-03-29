import spacy
import wikipedia
import streamlit as st
from spacy import displacy

nlp = spacy.load('en_core_web_md')

def main():
    st.title("NAMED ENTITY RECOGNITION PROJECT")
    st.subheader("Natural Language Processing")

    # NAMED ENTITY RECOGNITION
    if st.checkbox("SHOW NAMED ENTITY RECOGNITION"):
        st.subheader("Input:")
        msg = st.text_input("Enter You Subject:","Abdul Kalam")
        rawtext = wikipedia.summary(msg, auto_suggest=False)
        mydoc = nlp(rawtext)

        myhtmlval = displacy.render(mydoc, style='ent')
        myhtmlval = myhtmlval.replace("\n\n", "\n")



        if st.button("Result"):
            st.subheader("Web Scraped Data:")
            st.success(rawtext)
            st.subheader("Output:")
            st.write(myhtmlval, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
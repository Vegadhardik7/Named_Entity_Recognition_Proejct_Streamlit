# Named_Entity_Recognition_Project_Streamlit
This is the named entity recognition project done with the help of Python, Streamlit.

In this project we are going to highlight the entities which are we get after extracting the text with the help of web scraping. 


# Web-App URL:

https://streamlit-ner-project.herokuapp.com/


# What Is Named Entity Recognition:
Named Entity Recognition <b>(NER)</b> seeks to locate & classify named entities mentioned in unstructured text pre-defined categories such as...
- Person             (PERSON)
- Organization       (ORG) 
- Location           (GPE) 
- Date               (DATE)
- Money              (MONEY)   
- Product            (PRODUCT)
...etc.

All of the above mentioned categories are highligted with some color which is completely different for all the entities and beside that entity it's category is written.

Example:

![](NER1.png)

# Technologies Used:

- Python
- PyCharm
- HTML/CSS/JS
- Spacy
- Streamlit
- Wikipedia
- HeroKu


# Working Mechanish Of This Project:

At first I imported all the essential libraries such as spacy, streamlit, wikipedia...etc. Then I started to create a basic streamlit model.
After that at main function I took the subject that the user is interstead in and started to do web scraping. After the web scraping is over I gave that scraped data to the scpacy which which will give me the final output as I had show above in the form of NER.


# Reference:

- https://streamlit.io/
- https://spacy.io/api/doc/
- https://devcenter.heroku.com/categories/reference

#Sample File
import streamlit
import pandas

streamlit.title("KS Bala's Streamlit App")

streamlit.header("Heading")
streamlit.text("Hello! My Name is Bala Sellamuthu")

simple_csv = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Indexing
simple_csv = simple_csv.set_index("Fruit")

streamlit.multiselect("Pick some fruits:", list(simple_csv.index),['Grapes', 'Apple','Avocado','Strawberries'])
streamlit.dataframe(simple_csv)



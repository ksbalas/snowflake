#Sample File
import streamlit
import pandas

streamlit.title("KS Bala's Streamlit App")

streamlit.header("Heading")
streamlit.text("Hello! My Name is Bala Sellamuthu")

fruit_csv = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Indexing
fruit_csv = fruit_csv.set_index("Fruit")

fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruit_csv.index),['Grapes', 'Apple','Avocado','Strawberries'])

#Filter fruits based on above list
fruits_to_show  = fruit_csv.loc[fruits_selected]
streamlit.dataframe(fruit_csv)

#Filtered list 
streamlit.dataframe(fruits_to_show) 



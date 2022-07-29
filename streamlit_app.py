#Sample File
import streamlit
import pandas

streamlit.title("KS Bala's Streamlit App")

streamlit.header("Heading")
streamlit.text("Hello! My Name is Bala Sellamuthu")

simple_csv = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(simple_csv)

#Multiselect 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

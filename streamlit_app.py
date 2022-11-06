import streamlit

streamlit.title('Loving it to explore')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal🍳')
streamlit.text('Kale, Spinach & Rocket Smoothie🍹')
streamlit.text('🥚🥚Hard-Boiled Free-Range Egg')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchone()
streamlit.text("The Fruit Load List contains")
streamlit.text(my_data_row)

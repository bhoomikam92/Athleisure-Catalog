import streamlit
streamlit.title('New Store')
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("""
    SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
    CURRENT_REGION(), CURRENT_ROLE()
""")

my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

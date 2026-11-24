import logging
import mysql.connector
import streamlit as st
from crud import add_passenger

logger = logging.getLogger(__name__)

from crud import add_passenger

st.title("Global Airline Booking Portal")

with st.form("add_passenger_form"):
    passenger_id = st.text_input("Passenger ID")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=0, step=1)
    nationality = st.text_input("Nationality")
    submitted = st.form_submit_button("Add Passenger")

if submitted:
    try:
        add_passenger(
            passenger_id,
            first_name,
            last_name,
            gender,
            int(age),
            nationality,
        )
    except ValueError as error:
        st.error(str(error))
    except mysql.connector.Error:
        logger.exception("Saving passenger failed")
        st.error("Could not save passenger. Please try again.")
    else:
        st.success("Passenger added successfully!")
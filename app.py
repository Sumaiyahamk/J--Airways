import streamlit as st
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
    if not passenger_id.strip() or not first_name.strip() or not last_name.strip():
        st.error("Passenger ID, First Name, and Last Name cannot be empty.")
    else:
        add_passenger(
            passenger_id.strip(),
            first_name.strip(),
            last_name.strip(),
            gender,
            int(age),
            nationality.strip(),
        )
        st.success("Passenger added successfully!")
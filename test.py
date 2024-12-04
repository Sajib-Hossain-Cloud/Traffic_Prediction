import streamlit as st

st.title("Traffic prediction")

def display_form():
    with st.form(key='vehicle_count_form'):
        date = st.text_input('Date (YYYYMMDD)', '20240101')
        time = st.text_input('Time (HH:MM)', '08:00')
        day_of_week = st.selectbox('Day of the Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        car_count = st.number_input('Car Count', min_value=0, value=1)
        bike_count = st.number_input('Bike Count', min_value=0, value=20)
        bus_count = st.number_input('Bus Count', min_value=0, value=10)
        truck_count = st.number_input('Truck Count', min_value=0, value=5)

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write(f'Total Vehicle Count: {car_count + bike_count + bus_count + truck_count}')

if __name__ == "__main__":
    display_form()
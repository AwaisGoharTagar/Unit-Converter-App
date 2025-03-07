import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

# **Dropdown for category selection**
category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])

# **Unit selection based on category**
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱ Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds", 
        "Minutes to Hours", "Hours to Minutes", 
        "Hours to Days", "Days to Hours"
    ])

# **Input for value to convert**
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# **Conversion function**
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    
    return None

# **Conversion Button**
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion.")


# import streamlit as st

# st.title("🌍Unit Converter App")
# st.markdown("### Converts Length, Weight And Time Instantly")
# st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

# category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])

# def convert_units(category, value, unit):
#     if category == "Length":
#         if unit == "Kiloneters to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
        
#     elif category == "Weight":
#         if unit == "kilograms to pounds":
#             return value * 2.20462
#         elif unit == "Pounds to kilograms":
#             return value / 2.20462

#     elif category == "Time":
#         if unit == "seconds to minutes":
#             return value / 60
#         elif unit == "Minutes to seconds":
#             return value * 60
#         elif unit == "Minutes to hours":
#             return value / 60
#         elif unit == "Hours to minutes":
#             return value * 60
#         elif unit == "Hours to days":
#             return value / 24
#         elif unit == "Days to hours":
#             return value * 24
    
#     return 0
    
        
#     if category == "Length":
#         unit = st.selectbox("📏Select Conversation", ["Kiloneters to Miles", "Miles to Kilometers"])
    
#     elif category == "Weight":
#         unit = st.selectbox("⚖ Select Conversation", ["kilograms to pounds", "Pounds to kilograms"])
    
#     elif category == "Time":
#         unit = st.selectbox("⏱ Select Conversation", ["seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

#     value = st.number_input("Enter the value to convert")
   
#     if st.button("Convert"):
#         result = convert_units(category, value, unit)
#         st.success(f"The result is {result:.2f}") 
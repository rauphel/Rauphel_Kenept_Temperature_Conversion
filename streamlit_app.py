# Temperature Conversion Program
# Rauphel Kenept
# Oct 17, 2024

import streamlit as st
loop = True 
min_temp = 0.00
max_temp = 100.00

# Ask what type of conversion they want
start_temp = st.radio(
    "What type temperature do you want to convert?",
    ["Celsius", "Farenheit", "Kelvin"],
)

#Changes min to absolute zero of that value
if start_temp == "Celsius":
    min_temp = -273.15
elif start_temp == "Farenheit":
    min_temp = -459.67
else:
    min_temp = 0.00
    
# Ask for start temperature number
temperature = st.number_input("Original temperature value", min_value=min_temp, max_value=None,
value=0.00, step=.00, placeholder="Input temperature value", help="Please input temperature above absolute zero.")

# Asks what to convert to
convertion = st.radio(
    "What type temperature do you want to convert to?",
    ["Celsius", "Farenheit", "Kelvin"],
)

# Converting from Celsius
if start_temp == convertion:
    end_temperature = temperature
elif start_temp == "Celsius":
    if convertion == "Farenheit":
        end_temperature = (9/5 * temperature + 32)
    else:
        end_temperature = (273.15 + temperature)
        
# Converting from Farenheit
elif start_temp == "Farenheit":
    if convertion == "Celsius":
        end_temperature = (temperature - 32) * (5/9)
    else:
        end_temperature = (temperature - 32) * (5/9) + 273.15

# Converting from Kelvin
else :
    if convertion == "Celsius":
        end_temperature = (temperature - 273.15)
    else:
        end_temperature = (temperature - 273.15) * (9/5) + 32
        
#prints out the resulting temperature
st.write(end_temperature, convertion)
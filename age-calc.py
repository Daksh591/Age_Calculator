from datetime import datetime
import streamlit as st
st.text("Age Calculator")
today = datetime.today()
date = f"{today.year}-{today.month}-{today.day}"
birthdate = st.text_input("Enter your birthdate (YYYY-MM-DD): ")
today =st.text_input("Enter today date in format (YYYY-MM-DD)",date)
but = st.button("Submit")
if but:
    try:
    # Convert the input string to a datetime object
        birthdate2 = datetime.strptime(birthdate, "%Y-%m-%d")
        today2 =datetime.strptime(today,"%Y-%m-%d")
            # Get the current date
        today = datetime.today()

            # Calculate the difference in years, months, and days
        years = today2.year - birthdate2.year
        months = today2.month - birthdate2.month
        days = today2.day - birthdate2.day

            # Adjust for negative days
        if days < 0:
            months -= 1
            days += 31

            # Adjust for negative months
        if months < 0:
            years -= 1
            months += 12
        st.text(f"You are {years} years, {months} months and {days} days")
        st.markdown("""[Weather App](weatherappdaksh.streamlit.app)""")
        st.markdown("[Know BMI](knowbmibody.streamlit.app)")
        st.markdown("[Know phone number service provider](knowdaksh.streamlit.app)")
        st.text("""
The age of a person can be 
counted differently in different cultures. 
This calculator is based on the most common age system. In this system, 
age increases on a person's birthday. 
For example, the age of a person who has lived for 3 years and 11 months is 3, 
and their age will increase to 4 on their next birthday one month later. 
Most western countries use this age system.

In some cultures, 
age is expressed by 
counting years with or without including the current year. 
For example, a person who is twenty 
years old is the same age as another person who is in their twenty-first year of life. 
In one of the traditional Chinese age systems, 
people are born at age 1 and their age increases up at the 
Traditional Chinese New Year rather than their birthday. 
For example, if one baby is born just one day before the Traditional Chinese New Year, 
2 days later, the baby will be 2 even though he/she is only 2 days old.

In some situations, the months and day result of this age calculator may be confusing, 
especially when the starting date is the end of a month. 
For example, we count Feb. 20 to Mar. 20 to be one month. 
However, there are two ways to calculate the age from Feb. 28, 
2022 to Mar. 31, 2022. If we consider Feb. 28 to Mar. 28 to 
be one month, then the result is one month and 3 days. If we
 consider both Feb. 28 and Mar. 31 as the end of the month, 
 then the result is one month. Both calculation results are reasonable. 
 Similar situations exist for dates like Apr. 30 to May 31, May 30 to June 30, etc. 
 The confusion comes from the uneven number of days in different months. 
 In our calculations, we use the former method.
    
        
        
        
        
        """)
        st.markdown("""[Weather App](weatherappdaksh.streamlit.app)""")
        st.markdown("[Know BMI](knowbmibody.streamlit.app)")
        st.markdown("[Know phone number service provider](knowdaksh.streamlit.app)")
        st.text("""Some more websites
        Weather App - weatherappdaksh.streamlit.app
        Know BMI - knowbmibody.streamlit.app
        Know phone number service provider - knowdaksh.streamlit.app""")
        st.markdown("""[Weather App](weatherappdaksh.streamlit.app)""")
        st.markdown("[Know BMI](knowbmibody.streamlit.app)")
        st.markdown("[Know phone number service provider](knowdaksh.streamlit.app)")


    except Exception as e:
        st.text("Enter correct dates")









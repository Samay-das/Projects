# Importing the required libraries such as streamlit, time, google and an optional keys in our case
"""
Used of this libraries
>>>streamlit - to make an interactive frontend application
>>>time - for time related work
>>>google - to use their gemini model for this project
"""
import streamlit as st
import time 
import keys # (Optitional only for window user)
from google import genai
from google.genai.types import GenerateContentConfig

# Creating client using google.Client class an in the api key we use keys module to get the api key for this case.
client = genai.Client(api_key=keys.api_key)

#Using Gemini 2.5 Flash Lite model of google gemini family for his low cost token input and output charges.
model = 'gemini-2.5-flash-lite'

# Giving system intruction to the model by which we can give a persona to the model according to our use case.
system_intruction = """You are a career advisor who`s work is to 
give a student proper future career educational or technical 
(hand-on practice) option according to there qualification, 
specialization and their interest and give answer in the form
 of markdown and if the question does not match your work 
simply write 'Something went wrong Please Try Again'"""

# Creating interface using streamlit module by using classes such as st.title, st.header, st.form etc
st.title("Career Advisor")
st.header("Your Best Friend in Career Advancement")
with st.form(key='user-input'):
    st.subheader('Fill Out This Form')
    # User will choice from the giving option and the program will proceed according to their choice.
    career_state = st.radio(label="Which state are you right now in your life?",options=['None','School Student','College Student'],index=0)
    st.form_submit_button(label="Click To Update") # Have to click this button to update the form.
    if career_state == 'School Student':
        career_qualification = st.radio(label="What did you take in your 11th standard?",options=['Math','Commerce','Biology'])
        career_specialization = st.text_input("Please Specify the Specication of your degree",placeholder="PCM (Physic,Chmistry,Math), Commerce (Plain) etc.")
        career_interest = st.text_input("What are the thing which make you interest the most?",placeholder='Space Research , Animation etc.')
    elif career_state == 'College Student':
        career_qualification = st.radio(label="What degree did you take in your college?",options=['Bachelor Of Engineer','Bachelor Of Science','Bachelor Of Commerce','bachelor of Art','Bachelor of Design'])
        career_specialization = st.text_input("Please Specify the Specication of your degree",placeholder="Computer Science, Biochemistry etc.")
        career_interest = st.text_input("What are the thing which make you interest the most?",placeholder="Reserch, entrepreneurship etc.")
    button = st.form_submit_button(label="Submit") # Click this button to submit the form and to proceed futher.

# Coping this loading effect from the streamlit official website.
if button is True:
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(20) # Give the loading effect for the 20 second.
    # When a user click other option than None this statememt will executed.
    if career_state != 'None':
        # This will the prompt for the model to which it will give the answer.
        prompt = f"""
        This person is a {career_state} 
        which is doing {career_qualification} qualification 
        in {career_specialization} domain,
        which having {career_interest} as a interest.
        So give a appropriate career advise according 
        to their interest"""

        # In this area we receving the response from the model after giving prompt and some other thing into the model.
        response = client.models.generate_content(
        model=model, # We specify at the top.
        contents=prompt, # Prompt will be give in here.
        config=GenerateContentConfig(
            temperature=0.7, # Temperature range from 0 to 1 and can be change accordingly.
            system_instruction=system_intruction, # System Instruction to the model.
            max_output_tokens=1000 # Put max output to 1000 for low token outut for now.
        )
    )
    st.success("Done!")
    # Printing the response of the model using st.markdown to display to the user at the frontend.
    st.markdown(response.text) 
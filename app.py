import os
import streamlit as st
import google.generativeai as genai

# Set up Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure this is set in the environment
genai.configure(api_key="AIzaSyBG4WTbPeIuasxY5cU3W6W9xrrhAoBRk1M")

# Function to generate resume
def generate_resume(user_details):
    model = genai.GenerativeModel("gemini-1.5-pro")  # Initialize the model correctly

    prompt = f"""Generate a resume for:
    Name: {user_details['name']}
    Degree: {user_details['degree']}
    Field: {user_details['field']}
    Location: {user_details['location']}
    GPA: {user_details['gpa']}
    Skills: {", ".join(user_details['skills'])}
    Projects: {", ".join(user_details['projects'])}
    Internships: {", ".join(user_details['internships'])}
    Additional Info: {user_details['additional']}
    """

    response = model.generate_content(prompt)  # Call generate_content correctly

    return response.text if response else "Error generating resume."

# Streamlit UI
st.title("AI Resume Generator")
st.write("Fill in the details below, and AI will generate a professional resume for you.")

# User input fields
name = st.text_input("Full Name")
degree = st.text_input("Highest Degree Earned")
field = st.text_input("Field of Study")
location = st.text_input("Location")
gpa = st.text_input("GPA")
skills = st.text_area("Skills (comma-separated)")
projects = st.text_area("Projects (comma-separated)")
internships = st.text_area("Internships (comma-separated)")
additional = st.text_area("Additional Information (Certifications, Awards, etc.)")

if st.button("Generate Resume"):
    user_details = {
        "name": name,
        "degree": degree,
        "field": field,
        "location": location,
        "gpa": gpa,
        "skills": skills.split(","),
        "projects": projects.split(","),
        "internships": internships.split(","),
        "additional": additional
    }
    resume = generate_resume(user_details)
    st.text_area("Generated Resume", resume, height=500)

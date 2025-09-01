import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Portfolio", layout="wide")

# Title of my project
st.title(" Nitesh Shukla - Info Portfolio")
# Sidebar
st.sidebar.header("Navigation") 
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Page Content 
if page == "Home":
    st.header("Welcome ") 
    st.write("Hi, I'm *Nitesh Shukla*, a Data Analyst skilled in Python & It's Library (Pandas, Numpy, Matplotlib), SQL, Power BI, and Excel.")
    st.write("""🔴About Me (Short Bio)

Education 
             . BCA student at City College of Management.

Career Goal 
             . Aspiring Data Analyst / Data Scientist (I future).

Strengths 
             . problem-solving, logical thinking.""")
    st.write("""🔴Education & Certifications

🎓 BCA - City College of Management (2023-2026)

📜 Python for Data Analysis - Coursera""") 
    st.write("""🔴Internship / Tranining
             
Python with Data Analysis Training (6 Month)
             
Duration  01-jul-2024 to 02-dec-2024 
             
Regis No: SBIT2024/2698""")
    st.write("""🔴Quick Facts Section
             
🟢 2+ Projects completed

🟢 Skilled in Python & it's library, SQL, Power BI & EXCEL

🟢 Interested in Data Analytics & Software Engineering""")
    

elif page == "Projects": 
    st.header(" My Projects") 
    st.subheader("1. movie-recommendationsystem") 
    st.write("✔ Interactive dashboard and advance feature of search movies with python and its library, SQL etc.")
    st.write("A Movie Recommendation System is an intelligent system that suggests movies to users based on their preferences, past behavior, or similarity with other users.It helps platforms like Netflix, Amazon Prime, Hotstar improve user experience by recommending personalized content instead of showing random movies.") 
    st.subheader("2. Nitesh's Interactive Resume") 
    st.write("✔ Intractive portfolio for my resume.")
    st.write("""I developed a personal portfolio web application using Streamlit, an open-source Python framework for creating interactive web apps.
The portfolio showcases my skills, projects, and contact information in a structured and interactive way, allowing recruiters and professionals to quickly understand my background and work.""") 
    st.success("Thanks! Go to the next step of my identity.")


elif page == "Contact": 
    st.header("Contact Me") 
    st.write("Email: *nitesh2042@gmail.com*") 
    st.write("LinkedIn: www.linkedin.com/in/nitesh-shukla-a12214313")
    st.write("Phone No:  *9555206303*")
    st.markdown("[🔗 View on GitHub](https://github.com/NiteshShukla2042")
    #st.file_uploader("GitHub Image",type=["png","jpg","jpeg"], width=500)
   

    
    #st.success("Thanks! If you want to contact with me please go to next step.")

    #st.image("profile.jpg", width=200)
    #st.header("Image")
    #st.file_uploader("Upload an Image",type=["png","jpg","jpeg"], width=200)
    #st.success("Thanks[! Go to the next step of my identity.")

    #st.header("This is my Resume")
    #st.file_uploader("Upload an Image",type=["png","jpg","jpeg"], width=700)
    #st.success("Thanks! Go to the next step of my identity.")



    
    with st.form("contact_form"):
        st.header("For Contact Fill It")
        name = st.text_input("Your Name")
        company = st.text_input("Your Company")
        message = st.text_area("Feedback")
        submit = st.form_submit_button("Send")
    if submit:

        st.success("Thanks! I will get back to you soon.")
        

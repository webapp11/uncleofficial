import requests
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Uncle Official", page_icon="🌹", layout="wide")




# ---- LOAD ASSETS ----
yt_logo = Image.open("images/yt_logo.png")
yt_cover = Image.open("images/yt_cover.png")
moeen_image = Image.open("images/moeen_image.png")
coding_img = Image.open("images/coding_img.jpg")

# --- MENU ----

selected = option_menu(
    menu_title=None,
    options=["Home", "Videos", "Source", "About", "Contact"],
    icons=['house', 'tv', 'code', 'info-circle', 'telephone'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#b8860b"},
            "nav-link-selected": {"background-color": "#12c9bb"},
    }
)


# ---- HOME ----
if selected == "Home":
    with st.container():
        st.write("##")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("")
        with col2:
            st.image(yt_logo)
        with col3:
            st.write("")
        st.markdown(
            "<h1 style='text-align: center; text-decoration: underline; font-size: 50px; font-family: copper black; color: black;'>Uncle Official. </h1>",
            unsafe_allow_html=True)
        st.write("---")
        st.markdown(
            "<h2 style='text-align: center; font-size: 35px; font-family: Copper Black; color: gray;'>Welcome to 'Uncle Official' YouTube channel's website. </h2>",
            unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: left; font-size: 35px; color:black;'>What is coding?<h2/>",unsafe_allow_html=True)
        st.write("You’ve seen the craze for learning code. But what exactly is coding?"
                 "Coding is what makes it possible for us to create computer software,"
                 "apps and websites. Your browser, your OS, the apps on your phone, Facebook,"
                 "and this website – they’re all made with code.")
        st.markdown("<h2 style='text-align: left; font-size: 35px; color:black;'>101 Coding:<h2/>",unsafe_allow_html=True)
        st.write("If you don’t know the first thing about coding, you’ve come to the right place."
                 " We’ve put together a beginner’s tutorial which will give you all the background information you need on coding,"
                 " before you start learning it for real.\n\nIt starts with an explanation on the benefits of learning coding. "
                 "Here, you’ll find out what you’ll be able to do once you know how to work with code. "
                 "Then, you’ll get a deeper understanding of how coding works, "
                 "and how the code you write gets converted into an instruction that a computer can ‘understand’. Very satisfying to know!")
        col1, col2, col3 = st.columns(3)
        with col2:
            st.image(coding_img)
        st.write("That’s followed by an outline of today’s coding languages."
                 " After all, every language has a purpose – some are for the web, "
                 "others for app development, others for desktop software.You’ll find out why web development is an ideal form of coding to start off with,"
                 " and then get a full overview of it. You’ll also be introduced to web design and app development.")
        st.markdown("<h2 style='text-align: left; font-size: 35px; color:black;'>Benifits of Coding Learning:<h2/>",unsafe_allow_html=True)
        st.write("There are several benefits of coding.")
        st.write(
            """
            - First, you develop an analytical thinking while you learn to code. 
              Instructing the computer what to do helps us develop the habit of analyzing any process or problem in a step wise manner.
              When w learn to break a process into small steps, it becomes easy for us to solve real world problems by analyzing them in a better manner.
            - Learning to code also helps you land high paying jobs. Nowadays, programming jobs are most sought after jobs and you can easily land a 
              $100k job if you learn to code efficiently in at least one programming language.
            - Another benefit of coding is continuous learning. If you are a programmer, you have to learn new things daily to develop softwares. 
              Computer science industry is a relatively new industry. Due to this, there are various tools, techniques, and programming languages 
              launched every year.To compete in the job market, you need to learn the new tools and programming language. Thus, continuous learning becomes your habit.
            """
        )
# ---- VIDEOS ----
if selected == "Videos":
    with st.container():
        st.markdown(
            "<h2 style='text-align: center; text-decoration: underline; font-family: Copper Black; font-size: 35px ; color: black;'>Videos on YouTube </h2>",
             unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.video("https://youtu.be/jAq2R08q-gg")
            st.write("[Watch on YouTube](https://youtu.be/jAq2R08q-gg)")
        with col2:
            st.video("https://youtu.be/MlljYZYMTCg")
            st.write("[Watch on YouTube](https://youtu.be/MlljYZYMTCg)")
        with col3:
            st.video("https://youtu.be/pWTHLPhV1Aw")
            st.write("[Watch on YouTube](https://youtu.be/pWTHLPhV1Aw)")

        st.write("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.video("https://youtu.be/jAq2R08q-gg")
            st.write("[Watch on YouTube](https://youtu.be/jAq2R08q-gg)")
        with col2:
            st.video("https://youtu.be/MlljYZYMTCg")
            st.write("[Watch on YouTube](https://youtu.be/MlljYZYMTCg)")
        with col3:
            st.video("https://youtu.be/pWTHLPhV1Aw")
            st.write("[Watch on YouTube](https://youtu.be/pWTHLPhV1Aw)")

        st.write("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.video("https://youtu.be/jAq2R08q-gg")
            st.write("[Watch on YouTube](https://youtu.be/jAq2R08q-gg)")
        with col2:
            st.video("https://youtu.be/MlljYZYMTCg")
            st.write("[Watch on YouTube](https://youtu.be/MlljYZYMTCg)")
        with col3:
            st.video("https://youtu.be/pWTHLPhV1Aw")
            st.write("[Watch on YouTube](https://youtu.be/pWTHLPhV1Aw)")


# ---- ABOUT CHANNEL OWNER ----
if selected == 'About':
    with st.container():
        st.markdown(
            "<h2 style='text-align: center; text-decoration: underline; font-family: Copper Black; font-size: 35px ; color: black;'>About channel creator</h2>",
            unsafe_allow_html=True)
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(moeen_image)
        with text_column:
            st.markdown("<h2 style='text-align: left; color: black; font-size: 30px; font-family: Copper Black;'>Md Moeen Uddin</h2>",
                unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: left; color: black; font-size: 20px; font-family: Copper Black;'>🖐, I'm Moeen.\n\n Lives in Khulna,Bangladesh.\n\nLearning at Diploma in "
                "Engineering [Department: Computer Science And Engineering]"
                "</h2>",
                unsafe_allow_html=True)


        st.write("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button('Follow me on'):
                st.write("[Facebook](https://www.facebook.com/moeen.u9)")
                st.write("[Instagram]()")

# ---- CONTACT ----
if selected == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Copper Black'; color: #190F05;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact:</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2', clear_on_submit=True):
        Name = st.text_input(label='Please Enter Your Name')
        Email = st.text_input(label='Please Enter Email')
        Message = st.text_input(label='Please Enter Your Message')
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')


# ---- FOOTER SECTION ----

with st.container():
    st.write("----")
    st.markdown("<h2 style='text-align: center; font-size:15px; font-family: Sashore Pro; color: #ffffff'>Copyrightⓒ2022-Uncle Official.All rights reserved.</h2>",
                unsafe_allow_html=True)
    st.write("----")
    st.empty()


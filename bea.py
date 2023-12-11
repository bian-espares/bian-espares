from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="SNSU-BEA",page_icon=":🐼:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',  unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("images/jon.jpg")
img_github = Image.open("images/github.png")

with st.container():
    st.subheader('Hi,my name is BIANCA FAITH ESPARES🐣')
    st.title('PROGRAMMING, LOGIC AND DESIGN')
    st.write('Life is like programming, there might be some errors but we can correct it.')
    st.write('ITS HARD BUT ITS FUN🎉')
    st.write('[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY)')

with st.container():
    st.write('---')
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What to know?")
        st.write("##")
        st.write(
            """
            I am currently studying at SNSU 
            under CEIT department with BSCpE 1B course. 
            I am parent of 1year old baby. 
            """
        )
        
    st.write("[For more information >](https://web.facebook.com/snsumainsao/?_rdc=1&_rdr)")
with right_column:
    st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.write("My Inspiration")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("He is JON EDJAY BAGANI ESPARES")
    st.write(
        """
        He is 1year old. He arrive in my life in a very unexpected time and situation.
        Now he is my everything, the reason why I keep standing up after many failure. 
        He change me into a better version of myself.
        """     
        )
    st.markdown("[watch the video...](https://www.facebook.com/reel/1410154259577343)")

with st.container():
    st.write("---")
    st.write("my project")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_github)

with text_column:
    st.subheader("What is GitHub?")
    st.write(
        """
         Github, Inc. is a platform and cloud-based service for software development and version contron, 
         allowing developer to store and manage the codes.
        """     
        )
    st.markdown("[see my github...](https://github.com/bian-espares/st.web)")

with st.container():
    st.subheader('COMPUTER PROGRAMMING💻')
    st.write('Computer programming or coding is the composition of sequences of instructions, called programs, that computers can follow to perform tasks')
    st.write('It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages')
    st.subheader('What is the purpose of programming?')
    st.write('It helps us solve problems and carry out tasks more efficiently.')
    st.write('It also allows us to automate processes and create new ways of doing things.')
    st.write('Computer programming is a highly sought-after skill in an increasingly technological world.')
    
    st.markdown("[for more information>](https://www.google.com/search?q=what+is+programming+in+computer&sca_esv=589298829&ei=L-lzZcG1GtHn2roPwIae6AY&oq=what+is+programming+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHdoYXQgaXMgcHJvZ3JhbW1pbmcgKgIIADIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI7JZLUM0IWK6AS3ATeAGQAQGYAeoCoAG1L6oBCDAuMzQuMi4xuAEByAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAgsQABiABBiKBRiRAsICBhAAGBYYHsICCxAAGIAEGIoFGIYDwgIIEAAYFhgeGArCAgUQIRigAcICCBAhGBYYHhgdwgIHECEYoAEYCsICChAhGBYYHhgPGB3CAgoQABgWGB4YDxgKwgIIEAAYFhgeGA_CAgQQIRgV4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serp)")

    st.write(
        """
        -Learning programming for me is a blessing. 
        I am very bless that there are people who is really willing to teach me everything👨‍👩‍👦-.
        """
        )
    st.markdown("[my family>](https://www.facebook.com/reel/274642328473894)")

with st.container():
    st.write("---")
    st.header('For Any concerns You Can Contact Me!')
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/esparesbiancafaith@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message  here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

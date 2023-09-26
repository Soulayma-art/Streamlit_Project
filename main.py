import streamlit as st
from PIL import Image

st.title("Hello Gomycode ")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("Hello Gomycode")
st.markdown("### This is a markdown")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
img = Image.open("images/sss.jpg")
st.image(img, width=200)
if st.checkbox("Show/Hide"):
	st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female'))
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function

if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")
# first argument takes the titleof the selectionbox
# second argument takes options :

hobby = st.selectbox("Hobbies: ",
					['Dancing', 'Reading', 'Sports'])
# print the selected hobby :

st.write("Your hobby is: ", hobby)
hobbies = st.multiselect("Hobbies: ",
						['Dancing', 'Reading', 'Sports'])

st.write("You selected", len(hobbies), 'hobbies')
st.button("Click me for no reason")

if(st.button("About")):
	st.text("Welcome To Gomycode!!!")
name = st.text_input("Enter Your name", "Type Here ...")

if(st.button('Submit')):
	result = name.title()
	st.success(result)
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)
# print the level
# format() is used to print value of a variable at a specific position
st.text('Selected: {}'.format(level))
# import the streamlit library

# give a title to our app
st.title('Welcome to BMI Calculator')
# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")
# TAKE HEIGHT INPUT
# radio button to choose height format status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
if (status == 'cms'):
    height = st.number_input('Centimeters')

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")
elif (status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if (st.button('Calculate BMI')):

    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of BMI index
    if (bmi < 16):
        st.error("You are Extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif (bmi >= 30):
        st.error("Extremely Overweight")
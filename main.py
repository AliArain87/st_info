import streamlit as st 

st.set_page_config(
    page_title="CS-Department Course Codes",
    page_icon='✈', layout='wide', initial_sidebar_state='auto'
)

# Hide Menu and Footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """   
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Course Codes for CS-Department")
st.markdown("___")

# options for the dropdown

batch = st.selectbox("Select Batch", ("2019", "2020", "2021", "2022"))


semester = st.selectbox("Select Semester", ("","1", "2", "3", "4", "5", "6", "7", "8"))


# 19 batch
sem1_19 = ("","Computer Fundamentals","Applied Calculus","Functional English","Electronic Engineering","Basic Electrical Engineering")

sem2_19 = ("","Computer Programming","Digital Logic and Design","Linear Algebra and Analytical Geometry","Communication Skills","Pakistan Studies","Islamic Studies/Ethics")

sem3_19 = ("","Computer Architecture and Assembly","Object Oriented Programming","Computer Graphic","Electrical Circuits","Differential Equations")

sem4_19 = ("","Data Structure and Algorithm Analysis","Microprocessors and Interfacing Techniques","Modeling and Simulation","Database Management Systems","Fourier Series and Transforms")

sem5_19 = ("","Analogue and Digital Signal Processing","Operating Systems Design Concepts","Engineering Economics and Management","Technical Report Writing","Statistics and Probability")

sem6_19 = ("","Communication Systems","Professional Ethics","Mobile Application Development","Web Engineering","Embedded Systems")

sem7_19 = ("","Digital Image Processing","Computer Communication and Networks","Software Engineering","Computer Engineering Project – I")

sem8_19 = ("","Mobile and Wireless Communication","Artificial Intelligence","Entrepreneurship and Leadership","Data Science and Analytics", "Computer Engineering Project – II")





# make a dictionary for the course codes

code_dict_19 = {"Computer Fundamentals":"CS-101","Applied Calculus":"MTH-102","Functional English":"ENG-101","Electronic Engineering":"ES-121","Basic Electrical Engineering":"EL-101",

"Computer Programming":"CS-151","Digital Logic and Design":"CS-152","Linear Algebra and Analytical Geometry":"MTH-112","Communication Skills":"ENG-102","Pakistan Studies":"PS-106","Islamic Studies/Ethics":"IS-111 /SS-104",

"Computer Architecture and Assembly":"CS-201","Object Oriented Programming":"CS-202","Computer Graphic":"CS-204","Electrical Circuits":"EL-103","Differential Equations":"MTH-224",

"Data Structure and Algorithm Analysis":"CS-251","Microprocessors and Interfacing Techniques":"CS-252","Modeling and Simulation":"CS-253","Database Management Systems":"CS-255","Fourier Series and Transforms":"MTH-226",

"Analogue and Digital Signal Processing":"CS-301","Operating Systems Design Concepts":"CS-302","Engineering Economics and Management":"INM-302","Technical Report Writing":"CS-305","Statistics and Probability":"MTH-311",

"Communication Systems":"CS-351","Professional Ethics":"CS-355","Mobile Application Development":"CS-356","Web Engineering":"CS-370","Embedded Systems":"CS-354",

"Digital Image Processing":"CS-401","Computer Communication and Networks":"CS-403","Software Engineering":"CS-404","Computer Engineering Project – I":"CS-499",

"Mobile and Wireless Communication":"CS-451","Artificial Intelligence":"CS-452","Entrepreneurship and Leadership":"CS-453","Data Science and Analytics":"CS-454", "Computer Engineering Project – II":"CS-499"
}





# 21 batch



sem1_21 = ("","Applied Calculus","Information and Communication Technologies","Computer Programming","Functional English","Basic Electrical Engineering")

sem2_21 = ("","Linear Algebra and Analytical Geometry","Electrical Circuit Analysis","Object Oriented Programming","Islamic Studies/Ethics","Pakistan Studies")

sem3_21 = ("","Digital Logic and Design","Communication Skills","Electronic Circuits and Devices","Discrete Structures","Differential Equations")

sem4_21 = ("","Signals and Systems","Fourier Series and Transforms","Data Structures and Algorithms","Computer Architecture and Assembly Programming","Engineering Economics and Project Management")

sem5_21 = ("","Microprocessors and Interfacing","Computer Networks","Database Management System","Statistics and Probability","Operating Systems")

sem6_21 = ("","Technical and Scientific Writing","Web Engineering","Software Engineering","Embedded Systems","Digital Image Processing")

sem7_21 = ("","System and Network security","Mobile And Wireless Communication","Artificial Intelligence","Entrepreneurship","Final Year Project-I")

sem8_21 = ("","Data Science and Analytics","MDEE-I","Human Computer Interaction","Organizational Behavior", "Final Year Project")





# make a dictionary for the course codes

code_dict_21 = {"Applied Calculus":"MTH-108","Information and Communication Technologies":"CS-111","Computer Programming":"CS-151","Functional English":"ENG-101","Basic Electrical Engineering":"EL-101",

"Linear Algebra and Analytical Geometry":"MTH-112","Electrical Circuit Analysis":"EL-103","Object Oriented Programming":"CS-153","Islamic Studies/Ethics":"IS-111 /SS-104","Pakistan Studies":"PS-106",

"Digital Logic and Design":"CS-211","Communication Skills":"ENG-201","Electronic Circuits and Devices":"ES-231","Discrete Structures":"CS-221","Differential Equations":"MTH-224",

"Signals and Systems":"TL-231","Fourier Series and Transforms":"MTH-226","Data Structures and Algorithms":"CS-251","Computer Architecture and Assembly Programming":"CS-201","Engineering Economics and Project Management":"IND-202",

"Microprocessors and Interfacing":"CS-311","Computer Networks":"CS-321","Database Management System":"CS-353","Statistics and Probability":"MTH-317","Operating Systems":"CS-302",

"Technical and Scientific Writing":"ENG-301","Web Engineering":"CS-373","Software Engineering":"CS-331","Embedded Systems":"ES-316","Digital Image Processing":"CS-363",

"System and Network security":"TL-376","Mobile And Wireless Communication":"CS-431","Artificial Intelligence":"CS-452","Entrepreneurship":"ENT-421","Final Year Project-I":"CS-498",

"Data Science and Analytics":"CS-461","MDEE-I":" ","Human Computer Interaction":"CS-471","Organizational Behavior":"MGT-426", "Final Year Project":"CS-499"
}







# 22 batch

sem1_22 = ("","Applied Calculus","Information and Communication Technologies","Computer Programming","Functional English","Basic Electrical Engineering")

sem2_22 = ("","Linear Algebra and Analytical Geometry","Electronic Devices and Circuits","Object Oriented Programming","Islamic Studies/Ethics","Pakistan Studies")

sem3_22 = ("","Digital Logic and Design","Communication Skills","Data Structures and Algorithms","Discrete Structures","Differential Equations","Engineering Economics and Project Management")

sem4_22 = ("","Signals and Systems","Fourier Series and Transforms","Database Management System","Computer Architecture and Assembly Programming","Operating Systems")

sem5_22 = ("","Microprocessors and Interfacing","Computer Networks","Software Engineering","Statistics and Probability","Web Engineering")

sem6_22 = ("","Technical and Scientific Writing","System and Network security","Artificial Intelligence","Embedded Systems","Digital Image Processing","Community Service")

sem7_22 = ("","CEDE-I","Mobile application & Game development","Data Science and Analytics","Entrepreneurship","Final Year Project-I")

sem8_22 = ("","Cloud and distributed computing","MDEE-I","Human Computer Interaction","Organizational Behavior", "Final Year Project")



# make a dictionary for the course codes

code_dict_22 = {"Applied Calculus":"MTH-108","Information and Communication Technologies":"CS-111","Computer Programming":"CS-151","Functional English":"ENG-101","Basic Electrical Engineering":"EL-101",

"Linear Algebra and Analytical Geometry":"MTH-112","Electronic Devices and Circuits":"ES-231","Object Oriented Programming":"CS-153","Islamic Studies/Ethics":"IS-111 /SS-104","Pakistan Studies":"PS-106",

"Digital Logic and Design":"CS-211","Communication Skills":"ENG-201","Data Structures and Algorithms":"CS-251","Discrete Structures":"CS-221","Differential Equations":"MTH-224","Engineering Economics and Project Management":"IND-202",

"Signals and Systems":"TL-231","Fourier Series and Transforms":"MTH-226","Database Management System":"CS-353","Computer Architecture and Assembly Programming":"CS-201","Operating Systems":"CS-302",

"Microprocessors and Interfacing":"CS-311","Computer Networks":"CS-321","Software Engineering":"CS-331","Statistics and Probability":"MTH-317","Web Engineering":"CS-373",

"Technical and Scientific Writing":"ENG-301","System and Network security":"TL-376","Artificial Intelligence":"CS-452","Embedded Systems":"ES-316","Digital Image Processing":"CS-363","Community Service":"N/A",

"CEDE-I":" ","Mobile application & Game development":"CS-493","Data Science and Analytics":"CS-461","Entrepreneurship":"ENT-421","Final Year Project-I":"CS-498",

"Cloud and distributed computing":" ","MDEE-I":" ","Human Computer Interaction":"CS-471","Organizational Behavior":"MGT-426", "Final Year Project":"CS-499"
}





course_name = ""
if batch == "2019":
    if semester == "1":
        course_name = st.selectbox("Select the Course Name", sem1_19)

    elif semester == "2":
        course_name = st.selectbox("Select the Course Name", sem2_19)

    elif semester == "3":
        course_name = st.selectbox("Select the Course Name", sem3_19)

    elif semester == "4":
        course_name = st.selectbox("Select the Course Name", sem4_19)

    elif semester == "5":
        course_name = st.selectbox("Select the Course Name", sem5_19)

    elif semester == "6":
        course_name = st.selectbox("Select the Course Name", sem6_19)

    elif semester == "7":
        course_name = st.selectbox("Select the Course Name", sem7_19)

    elif semester == "8":
        course_name = st.selectbox("Select the Course Name", sem8_19)








elif batch == "2020":
    if semester == "1":
        course_name = st.selectbox("Select the Course Name", sem1_19)

    elif semester == "2":
        course_name = st.selectbox("Select the Course Name", sem2_19)

    elif semester == "3":
        course_name = st.selectbox("Select the Course Name", sem3_19)

    elif semester == "4":
        course_name = st.selectbox("Select the Course Name", sem4_19)

    elif semester == "5":
        course_name = st.selectbox("Select the Course Name", sem5_19)

    elif semester == "6":
        course_name = st.selectbox("Select the Course Name", sem6_19)

    elif semester == "7":
        course_name = st.selectbox("Select the Course Name", sem7_19)

    elif semester == "8":
        course_name = st.selectbox("Select the Course Name", sem8_19)






elif batch == "2021":
    if semester == "1":
        course_name = st.selectbox("Select the Course Name", sem1_21)

    elif semester == "2":
        course_name = st.selectbox("Select the Course Name", sem2_21)

    elif semester == "3":
        course_name = st.selectbox("Select the Course Name", sem3_21)

    elif semester == "4":
        course_name = st.selectbox("Select the Course Name", sem4_21)

    elif semester == "5":
        course_name = st.selectbox("Select the Course Name", sem5_21)

    elif semester == "6":
        course_name = st.selectbox("Select the Course Name", sem6_21)

    elif semester == "7":
        course_name = st.selectbox("Select the Course Name", sem7_21)

    elif semester == "8":
        course_name = st.selectbox("Select the Course Name", sem8_21)


elif batch == "2022":
    if semester == "1":
        course_name = st.selectbox("Select the Course Name", sem1_22)

    elif semester == "2":
        course_name = st.selectbox("Select the Course Name", sem2_22)

    elif semester == "3":
        course_name = st.selectbox("Select the Course Name", sem3_22)

    elif semester == "4":
        course_name = st.selectbox("Select the Course Name", sem4_22)

    elif semester == "5":
        course_name = st.selectbox("Select the Course Name", sem5_22)

    elif semester == "6":
        course_name = st.selectbox("Select the Course Name", sem6_22)

    elif semester == "7":
        course_name = st.selectbox("Select the Course Name", sem7_22)

    elif semester == "8":
        course_name = st.selectbox("Select the Course Name", sem8_22)











if batch == "2019":
    if course_name == "":
        st.warning("Select the Course Name")

    else:
        st.success("Course Code👇")
        st.info(code_dict_19[course_name])

# elif batch == "2020":
#     if course_name == "":
#         st.warning("Select the Course Name")

#     else:
#         st.success("Course Code")
#         st.info(code_dict_20[course_name])

elif batch == "2021":
    if course_name == "":
        st.warning("Select the Course Name")

    else:
        st.success("Course Code👇")
        st.info(code_dict_21[course_name])

elif batch == "2022":
    if course_name == "":
        st.warning("Select the Course Name")

    else:
        st.success("Course Code👇")
        st.info(code_dict_22[course_name])




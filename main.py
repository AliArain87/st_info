import streamlit as st
import pandas as pd



st.set_page_config(page_title="CS Course Planner", page_icon="🎓")
st.title("Computer Systems-Course Planner")


# Hide Menu and Footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """   
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Define the data for each batch and semester
batch_data = {
    '19': {
        '1': ["Computer Fundamentals", "Applied Calculus", "Functional English", "Electronic Engineering", "Basic Electrical Engineering"],
        '2': ["Computer Programming", "Digital Logic and Design", "Linear Algebra and Analytical Geometry", "Communication Skills", "Pakistan Studies", "Islamic Studies/Ethics"],
        '3': ["Computer Architecture and Assembly", "Object Oriented Programming", "Computer Graphic", "Electrical Circuits", "Differential Equations"],
        '4': ["Data Structure and Algorithm Analysis", "Microprocessors and Interfacing Techniques", "Modeling and Simulation", "Database Management Systems", "Fourier Series and Transforms"],
        '5': ["Analogue and Digital Signal Processing", "Operating Systems Design Concepts", "Engineering Economics and Management", "Technical Report Writing", "Statistics and Probability"],
        '6': ["Communication Systems", "Professional Ethics", "Mobile Application Development", "Web Engineering", "Embedded Systems"],
        '7': ["Digital Image Processing", "Computer Communication and Networks", "Software Engineering", "Computer Engineering Project – I"],
        '8': ["Mobile and Wireless Communication", "Artificial Intelligence", "Entrepreneurship and Leadership", "Data Science and Analytics", "Computer Engineering Project – II"]
    },
    '21': {
        '1': ["Applied Calculus", "Information and Communication Technologies", "Computer Programming", "Functional English", "Basic Electrical Engineering"],
        '2': ["Linear Algebra and Analytical Geometry", "Electrical Circuit Analysis", "Object Oriented Programming", "Islamic Studies/Ethics", "Pakistan Studies"],
        '3': ["Digital Logic and Design", "Communication Skills", "Electronic Circuits and Devices", "Discrete Structures", "Differential Equations"],
        '4': ["Signals and Systems", "Fourier Series and Transforms", "Data Structures and Algorithms", "Computer Architecture and Assembly Programming", "Engineering Economics and Project Management"],
        '5': ["Microprocessors and Interfacing", "Computer Networks", "Database Management System", "Statistics and Probability", "Operating Systems"],
        '6': ["Technical and Scientific Writing", "Web Engineering", "Software Engineering", "Embedded Systems", "Digital Image Processing"],
        '7': ["System and Network security", "Mobile And Wireless Communication", "Artificial Intelligence", "Entrepreneurship", "Final Year Project-I"],
        '8': ["Data Science and Analytics", "MDEE-I", "Human Computer Interaction", "Organizational Behavior", "Final Year Project"]
    },
    '22': {
        '1': ["Applied Calculus","Information and Communication Technologies","Computer Programming","Functional English","Basic Electrical Engineering"],
        '2': ["Linear Algebra and Analytical Geometry","Electronic Devices and Circuits","Object Oriented Programming","Islamic Studies/Ethics","Pakistan Studies"],
        '3': ["Digital Logic and Design","Communication Skills","Data Structures and Algorithms","Discrete Structures","Differential Equations","Engineering Economics and Project Management"],
        '4': ["Signals and Systems","Fourier Series and Transforms","Database Management System","Computer Architecture and Assembly Programming","Operating Systems"],
        '5': ["Microprocessors and Interfacing","Computer Networks","Software Engineering","Statistics and Probability","Web Engineering"],
        '6': ["Technical and Scientific Writing","System and Network security","Artificial Intelligence","Embedded Systems","Digital Image Processing","Community Service"],
        '7': ["CEDE-I","Mobile application & Game development","Data Science and Analytics","Entrepreneurship","Final Year Project-I"],
        '8': ["Cloud and distributed computing","MDEE-I","Human Computer Interaction","Organizational Behavior", "Final Year Project"]
    }
}

# Define the course codes for each batch
course_codes_19 = {
    "Computer Fundamentals": "CS-101",
    "Applied Calculus": "MTH-102",
    "Functional English": "ENG-101",
    "Electronic Engineering": "ES-121",
    "Basic Electrical Engineering": "EL-101",
    "Computer Programming": "CS-151",
    "Digital Logic and Design": "CS-152",
    "Linear Algebra and Analytical Geometry": "MTH-112",
    "Communication Skills": "ENG-102",
    "Pakistan Studies": "PS-106",
    "Islamic Studies/Ethics": "IS-111 /SS-104",
    "Computer Architecture and Assembly": "CS-201",
    "Object Oriented Programming": "CS-202",
    "Computer Graphic": "CS-204",
    "Electrical Circuits": "EL-103",
    "Differential Equations": "MTH-224",
    "Data Structure and Algorithm Analysis": "CS-251",
    "Microprocessors and Interfacing Techniques": "CS-252",
    "Modeling and Simulation": "CS-253",
    "Database Management Systems": "CS-255",
    "Fourier Series and Transforms": "MTH-226",
    "Analogue and Digital Signal Processing": "CS-301",
    "Operating Systems Design Concepts": "CS-302",
    "Engineering Economics and Management": "INM-302",
    "Technical Report Writing": "CS-305",
    "Statistics and Probability": "MTH-331",
    "Communication Systems": "CS-351",
    "Professional Ethics": "CS-355",
    "Mobile Application Development": "CS-356",
    "Web Engineering": "CS-370",
    "Embedded Systems": "CS-354",
    "Digital Image Processing": "CS-401",
    "Computer Communication and Networks": "CS-403",
    "Software Engineering": "CS-404",
    "Computer Engineering Project – I": "CS-499",
    "Mobile and Wireless Communication": "CS-451",
    "Artificial Intelligence": "CS-452",
    "Entrepreneurship and Leadership": "CS-453",
    "Data Science and Analytics": "CS-454",
    "Computer Engineering Project – II": "CS-499"
}


course_codes_21 = {
    "Applied Calculus":"MTH-108",
    "Information and Communication Technologies":"CS-111",
    "Computer Programming":"CS-151",
    "Functional English":"ENG-101",
    "Basic Electrical Engineering":"EL-101",
    "Linear Algebra and Analytical Geometry":"MTH-112",
    "Electrical Circuit Analysis":"EL-103",
    "Object Oriented Programming":"CS-153",
    "Islamic Studies/Ethics":"IS-111 /SS-104",
    "Pakistan Studies":"PS-106",
    "Digital Logic and Design":"CS-211",
    "Communication Skills":"ENG-201",
    "Electronic Circuits and Devices":"ES-231",
    "Discrete Structures":"CS-221",
    "Differential Equations":"MTH-224",
    "Signals and Systems":"TL-231",
    "Fourier Series and Transforms":"MTH-226",
    "Data Structures and Algorithms":"CS-251",
    "Computer Architecture and Assembly Programming":"CS-201",
    "Engineering Economics and Project Management":"IND-202",
    "Microprocessors and Interfacing":"CS-311",
    "Computer Networks":"CS-321",
    "Database Management System":"CS-353",
    "Statistics and Probability":"MTH-317",
    "Operating Systems":"CS-302",
    "Technical and Scientific Writing":"ENG-301",
    "Web Engineering":"CS-373",
    "Software Engineering":"CS-331",
    "Embedded Systems":"ES-316",
    "Digital Image Processing":"CS-363",
    "System and Network security":"TL-376",
    "Mobile And Wireless Communication":"CS-431",
    "Artificial Intelligence":"CS-452",
    "Entrepreneurship":"ENT-421",
    "Final Year Project-I":"CS-498",
    "Data Science and Analytics":"CS-461",
    "MDEE-I":" ",
    "Human Computer Interaction":"CS-471",
    "Organizational Behavior":"MGT-426",
    "Final Year Project":"CS-499"
}




course_codes_22 = {
    "Applied Calculus":"MTH-108",
    "Information and Communication Technologies":"CS-111",
    "Computer Programming":"CS-151",
    "Functional English":"ENG-101",
    "Basic Electrical Engineering":"EL-101",
    "Linear Algebra and Analytical Geometry":"MTH-112",
    "Electronic Devices and Circuits":"ES-231",
    "Object Oriented Programming":"CS-153",
    "Islamic Studies/Ethics":"IS-111 /SS-104",
    "Pakistan Studies":"PS-106",
    "Digital Logic and Design":"CS-211",
    "Communication Skills":"ENG-201",
    "Data Structures and Algorithms":"CS-251",
    "Discrete Structures":"CS-221",
    "Differential Equations":"MTH-224",
    "Engineering Economics and Project Management":"IND-202",
    "Signals and Systems":"TL-231",
    "Fourier Series and Transforms":"MTH-226",
    "Database Management System":"CS-353",
    "Computer Architecture and Assembly Programming":"CS-201",
    "Operating Systems":"CS-302",
    "Microprocessors and Interfacing":"CS-311",
    "Computer Networks":"CS-321",
    "Software Engineering":"CS-331",
    "Statistics and Probability":"MTH-317",
    "Web Engineering":"CS-373",
    "Technical and Scientific Writing":"ENG-301",
    "System and Network security":"TL-376",
    "Artificial Intelligence":"CS-452",
    "Embedded Systems":"ES-316",
    "Digital Image Processing":"CS-363",
    "Community Service":"N/A",
    "CEDE-I":" ",
    "Mobile application & Game development":"CS-493",
    "Data Science and Analytics":"CS-461",
    "Entrepreneurship":"ENT-421",
    "Final Year Project-I":"CS-498",
    "Cloud and distributed computing":" ",
    "MDEE-I":" ",
    "Human Computer Interaction":"CS-471",
    "Organizational Behavior":"MGT-426", 
    "Final Year Project":"CS-499"
}




opt = st.radio("Select Option", options=['CS-Dept','Outside-Dept'])

if opt == 'CS-Dept':
    batch = st.selectbox("Select batch", options=['19', '21', '22'])
    semester = st.selectbox("Select semester", options=['1', '2', '3', '4', '5', '6', '7', '8'])

    if batch == '19':
        
        courses = batch_data[batch][semester]

        table_data = [[course_codes_19[course], course] for course in courses]
        st.table(table_data)

    elif batch == '21':
        courses = batch_data[batch][semester]

        table_data = [[course_codes_21[course], course] for course in courses]
        st.table(table_data)

    elif batch == '22':
        courses = batch_data[batch][semester]

        table_data = [[course_codes_22[course], course] for course in courses]
        st.table(table_data)



    st.success("Courses for Batch {} Semester {} displayed successfully!".format(batch, semester))






    # show the all courses code 
    if st.checkbox('Show all course codes'):
        st.table([[course_codes_19[course], course] for course in course_codes_19])
        st.table([[course_codes_21[course], course] for course in course_codes_21])
        st.table([[course_codes_22[course], course] for course in course_codes_22])

        










    # function to save the dataset in csv file
    def save_data(batch_data, course_codes, batch):
        data = []
        for semester in batch_data[batch]:
            courses = batch_data[batch][semester]
            for course in courses:
                data.append([course_codes[course], course])
        df = pd.DataFrame(data, columns=['Course Code', 'Course Name'])
        df.to_csv('batch_{}.csv'.format(batch), index=False)


    # make a button to save the data in csv file

    if st.button('Save Data'):
        save_data(batch_data, course_codes_19, '19')
        save_data(batch_data, course_codes_21, '21')
        save_data(batch_data, course_codes_22, '22')
        st.success('Data saved successfully!')
        st.balloons()







## OUTSIDE DEPT SECTION


else:
    st.title("Outside-Dept")
    st.write("This is the outside dept section")


    course_codes_outside = pd.DataFrame({
        'Course Code': ['CS-140', 'CS-141', 'CS-131', 'CS-331', 'CS-227', 'CS-218', 'CS-225', 'CS-115', 'CS-231', 'CS-340/240', 'CS-145', 'CS-104', 'CS-260', 'CS-150', 'CS-113', 'CS-215', 'CS-490', 'CS-103', 'CS-121'],
        'Course Name': ['ITC & C++ Programming','ITC & C++ Programming Lab','Computer sided learning','Information & DB Management','Introduction to computers and c++ programming','Introduction to computers and c++ programming','ITC & C++ Programming','Introduction to computing','Computer Programming and Software Application','Introduction to computers and c++ programming','Introduction to computing','Introduction to computing and programming','Microprocessor systems','Introduction to computing','Computer programming','Computer aided engineering drawing','Artificial Intelligence','Introduction to computing','Data structures'],
        'Semester': ['2', '1', '2', '5', '4', '3', '4', '1', '3', '3/5', '1', '1', '4', '1', '2', '3', '8', '1', '2'],
        'Dept': ['Civil Department','Environment Dept','Environment Dept','CRP','Chemical Dept','Industrial','Mechanical','Metallurgy','Petroleum & gas','Textile','BSE-English','Electrical','Electrical','Electronics','Electronics','Electronics','Electronics','Telecommunication','Telecommunication']
    })

    st.table(course_codes_outside)


    # show the all courses code

    if st.checkbox('Show all course codes'):
        # show the first column of the dataframe
        st.table(course_codes_outside.iloc[:, 0:1])


        
    # function to save the dataset in csv file

    def save_data_outside(course_codes_outside):
        df = pd.DataFrame(course_codes_outside, columns=['Course Code', 'Course Name', 'Semester', 'Dept'])
        df.to_csv('outside_dept.csv', index=False)


    # make a button to save the data in csv file

    if st.button('Save Data'):
        save_data_outside(course_codes_outside)
        st.success('Data saved successfully!')
        st.balloons()





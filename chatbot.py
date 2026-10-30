import re
import random

# ============================================================
# SCSVMV COLLEGE ENQUIRY CHATBOT
# File: chatbot.py
# ============================================================

COLLEGE_NAME = (
    "Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya "
    "(SCSVMV / Kanchi University)"
)

COLLEGE_INFO = {
    "location": "Enathur, Kanchipuram, Tamil Nadu - 631561",
    "established": "1993",
    "type": "Deemed-to-be University",
    "phone": "+91 96290 32323 / +91 96290 01144",
    "email": "admission@kanchiuniv.ac.in",
    "registrar_email": "registrar@kanchiuniv.ac.in",
    "website": "https://www.kanchiuniv.ac.in/",
    "academic_directory": "https://kanchiuniv.ac.in/academics/",
}

# ============================================================
# 1. COURSES
# ============================================================

COURSES = {
    "Engineering": [
        "B.E.",
        "B.Tech",
        "M.E.",
        "M.Tech",
        "Ph.D.",
    ],
    "Arts, Science and Commerce": [
        "B.A.",
        "B.Sc.",
        "B.Com.",
        "BCA",
        "BBA",
        "MBA",
        "MCA",
        "B.Ed.",
    ],
    "Health Sciences": [
        "B.A.M.S.",
        "B.P.T.",
        "B.Optom.",
    ],
    "Law": [
        "B.A. LL.B.",
        "BBA LL.B.",
    ],
}

# ============================================================
# 2. APPROXIMATE COURSE FEES
# ============================================================

FEES = {
    "btech": "₹5,45,000–₹8,25,000 for four years",
    "be": "₹5,45,000–₹8,25,000 for four years",
    "bsc": "₹1,20,000–₹5,00,000 for three years",
    "bcom": "₹1,62,000–₹1,80,000 for three years",
    "mba": "₹1,25,000–₹2,75,000 for the programme",
    "bams": "₹10,75,000–₹18,37,000 for the programme",
    "law": "Approximately ₹7,50,000 for the programme",
    "bca": "₹1,62,000–₹1,82,000 for the programme",
    "bba": "₹1,62,000–₹1,82,000 for the programme",
}

# ============================================================
# 3. ADMISSION INFORMATION
# ============================================================

ADMISSIONS = {
    "engineering": (
        "B.E./B.Tech admission generally depends on Class 12 eligibility "
        "and the university's current admission rules. Entrance scores "
        "or academic merit may be considered."
    ),
    "bams": (
        "B.A.M.S. admission generally requires NEET-UG qualification "
        "and the applicable counselling process."
    ),
    "mba": (
        "MBA admission generally requires a recognised bachelor's degree. "
        "Entrance examinations or other selection criteria depend on "
        "the current admission policy."
    ),
    "general": (
        "Admission requirements differ by course. Check the current "
        "prospectus and contact admission@kanchiuniv.ac.in for eligibility, "
        "application dates, documents and selection procedures."
    ),
}

# ============================================================
# 4. DAILY TIMETABLE
# ============================================================

DAILY_TIMETABLE = """
SCSVMV DAILY TIMETABLE
(Reported timetable framework)

Morning Assembly and Hour 1: 08:00 AM - 09:10 AM
Hour 2: 09:10 AM - 10:10 AM
Mid-Morning Recess: 10:10 AM - 10:20 AM
Hours 3 and 4: 10:20 AM - 12:20 PM
Lunch Break: 12:20 PM - 01:20 PM
Hours 5 and 6: 01:20 PM - 04:10 PM

The reported classroom framework runs approximately from
08:10 AM to 04:10 PM.

Actual timings may differ by department, course, semester
and the official timetable.

Official ECE timetable:
https://kanchiuniv.ac.in/academics/department-of-electronics-and-communication-engineering/time-table/
"""

# ============================================================
# 5. CSE COURSE STRUCTURE
# ============================================================

CSE_COURSE_STRUCTURE = """
CSE COURSE STRUCTURE

Programme: B.E./B.Tech in Computer Science and Engineering
Duration: 4 years
Reported credit range for the referenced curriculum: approximately
167-171 credits. The exact requirement depends on the applicable syllabus.

FIRST YEAR - FOUNDATIONS
- Engineering Mathematics
- Programming Fundamentals
- Engineering Sciences
- Basic Electrical and Electronics concepts
- Engineering practicals and laboratory work

SECOND YEAR - CORE SUBJECTS
- Data Structures
- Digital Electronics
- Object-Oriented Programming
- Mathematics and computing subjects
- Core programming and laboratory work

THIRD YEAR - ADVANCED SUBJECTS
- Operating Systems
- Database Management Systems (DBMS)
- Java Programming
- Automata Theory
- Advanced computer science subjects
- Programme electives, depending on the syllabus
- Possible AI/ML or Cybersecurity electives, if offered

FOURTH YEAR - ADVANCED STUDY AND PROJECT
- Advanced and open electives
- Practical software laboratories
- Project work
- Final-year capstone or comprehensive project
- Other requirements specified in the applicable syllabus

The exact subjects, semesters and credits must be checked in
the syllabus applicable to the student's admission year.

Official CSE syllabus:
https://kanchiuniv.ac.in/wp-content/uploads/2024/04/Syllabus-2024-2025_CSE.pdf

CSE course materials:
https://kanchiuniv.ac.in/academics/department-of-computer-science-and-engineering/course-material-cse/
"""

# ============================================================
# 6. CSE TIMETABLE INFORMATION
# ============================================================

CSE_TIMETABLE_INFO = """
CSE TIMETABLE INFORMATION

The daily timetable framework is listed separately in this chatbot.
The exact CSE subject timetable depends on the semester, section,
academic year and department schedule.

For the actual subject-by-subject CSE timetable, including
periods, subjects, laboratory sessions and faculty assignments,
consult the latest timetable published by the CSE department.

CSE course materials:
https://kanchiuniv.ac.in/academics/department-of-computer-science-and-engineering/course-material-cse/

Academic directory:
https://kanchiuniv.ac.in/academics/
"""

# ============================================================
# 7. ACADEMIC EVALUATION AND ATTENDANCE
# ============================================================

EXAMINATION_INFO = """
ACADEMIC EVALUATION SYSTEM
(Reported CSE syllabus information)

Internal Assessment: 40% of total marks.
External University Examination: 60% of total marks.

The referenced syllabus reports a minimum of 24 marks out of
60 in the external examination for the applicable passing requirement.

Internal assessment may include:
- Periodic internal examinations
- Assignments
- Laboratory assessments
- Practical work
- Other course-specific assessments

ATTENDANCE

Attendance requirements depend on the applicable university regulations.
A threshold in the 70%-80% range has been reported, but students must
confirm the exact minimum for their programme and admission year.

Insufficient attendance may lead to an attendance shortage status
and ineligibility to take an end-semester examination.

Do not assume that the same passing marks or attendance rules apply
to every programme. Check the current syllabus and regulations.

CSE syllabus:
https://kanchiuniv.ac.in/wp-content/uploads/2024/04/Syllabus-2024-2025_CSE.pdf

IT syllabus:
https://kanchiuniv.ac.in/wp-content/uploads/2024/04/Syllabus-2024-2025_IT.pdf
"""

# ============================================================
# 8. FACULTY INFORMATION
# ============================================================

FACULTY = {
    "cse": {
        "names": [
            "Prof. Dr. R. Vasanth Kumar Mehta",
            "Dr. M. Senthil Kumaran",
            "Dr. P. Shanmugapriya",
            "Dr. V. Geetha",
            "Dr. M. Saraswathi",
            "Dr. C. K. Gomathy",
            "Dr. R. Prema",
            "Mr. R. Manickavasagam",
            "Mr. E. Sankar",
            "Mr. P. Ramesh Chandra",
            "Dr. M. Gayathri",
            "Dr. D. Thamaraiselvi",
            "Mr. V. Balu",
        ],
        "url": (
            "https://kanchiuniv.ac.in/academics/"
            "department-of-computer-science-and-engineering/"
            "faculty-department-computer-science-and-engg/"
        ),
    },
    "eee": {
        "names": [
            "Dr. M. Rathinakumar",
            "Dr. R. Modathi",
            "Dr. S. SentamilSelvan",
            "Dr. N. Ashokkumar",
            "Dr. B. Kandavel",
            "Dr. K. Anisha",
            "Mr. M. Mahendran",
        ],
        "url": (
            "https://kanchiuniv.ac.in/academics/"
            "department-of-electrical-and-electronics-engineering/"
            "faculty-department-eee/"
        ),
    },
    "ece": {
        "names": [
            "Dr. G. Senthil Kumar",
        ],
        "url": (
            "https://kanchiuniv.ac.in/academics/"
        ),
    },
    "management": {
        "names": [
            "Dr. B. Balaji Srinivasan",
            "Dr. Sweta Shrivastava",
            "Dr. M. S. Ramaratnam",
            "Dr. R. Jayaraman",
        ],
        "url": (
            "https://kanchiuniv.ac.in/academics/"
            "department-of-management-studies/"
            "faculty-faculty-of-management-studies/"
        ),
    },
    "law": {
        "names": [
            "Prof. (Dr.) Nirmala Kumari K",
            "Prof. Dr. L. Priyadharshini",
            "Prof. S. S. N. Murthy",
        ],
        "url": (
            "https://kanchiuniv.ac.in/academics/"
            "department_of_law/faculty/"
        ),
    },
    "education": {
        "names": [
            "Prof. Dr. K. Venkatramanan",
            "A. Amulraj",
        ],
        "url": (
            "https://kanchiuniv.ac.in/academics/"
            "school-of-education/faculty-school-of-education/"
        ),
    },
}

# ============================================================
# 9. BUS ROUTES AND APPROXIMATE ANNUAL FEES
# ============================================================

BUS_ROUTES = {
    "poonamallee": (
        "POONAMALLEE ROUTE\n"
        "Stops: Poonamallee Bypass, Nazarethpettai (Ayurveda College Campus), "
        "Chembarambakkam, Thandalam, Irungattukottai and "
        "Sriperumbudur Tollgate.\n"
        "Reported annual fee: ₹18,000-₹23,000."
    ),
    "ranipet": (
        "RANIPET BHEL ROUTE\n"
        "Stops: Muthukadai, Arcot Bypass, Walajapet, Kaveripakkam, Ocheri, "
        "Panapakkam, Thamal, Baluchetty Chatram and Kilambi.\n"
        "Reported annual fee: approximately ₹25,000."
    ),
    "chengalpattu": (
        "CHENGALPATTU ROUTE\n"
        "Stops: Walajabad, Rajampettai, Ekanampettai, Iyyampettai and Tollgate.\n"
        "Reported annual fee: approximately ₹20,000."
    ),
    "thiruthani": (
        "THIRUTHANI ROUTE\n"
        "Stops: Thanigaipolur, Arakkonam, SR Gate, Thakkolam Cross Road, "
        "Senthamangalam, Pallur and Kooram Gate.\n"
        "Reported annual fee: approximately ₹18,000."
    ),
    "vandavasi": (
        "VANDAVASI ROUTE\n"
        "Stops: Manamathi Cross Road, Perunagar, Koozhamandal, Aakoor and Dusi.\n"
        "Reported annual fee: ₹15,000-₹20,000."
    ),
    "uthiramerur": (
        "UTHIRAMERUR ROUTE\n"
        "Stops: Magaral, Thirupulivanam, Karuveppampoondi and Orikkai Mandapam.\n"
        "Reported annual fee: ₹12,000-₹18,000."
    ),
    "kanchipuram": (
        "LOCAL KANCHIPURAM ROUTE\n"
        "Stops: Kanchipuram Bus Stand, Rajaveethi, Ekambaranathar Temple, "
        "Pookadai Chathiram, Olimohammedpettai and old/new railway stations.\n"
        "Reported annual fee: approximately ₹12,000."
    ),
}

TRANSPORT_INFO = """
University transport is reported to serve Poonamallee, Ranipet,
Chengalpattu, Thiruthani, Vandavasi, Uthiramerur and local Kanchipuram.

Routes, bus availability, stops and annual fees may change each year.
Confirm current information with the university transport office.

Official transport page:
https://kanchiuniv.ac.in/campus-life/facilities/transport/

Alternate transport page:
https://kanchiuniv.ac.in/transport_facilities/
"""

# ============================================================
# 10. HOSTEL AND FOOD
# ============================================================

HOSTEL_INFO = """
HOSTEL FACILITIES

Separate accommodation is reported for male and female students.

Reported approximate annual hostel fee: ₹96,000.
Reported semester split:
Odd semester: ₹50,000.
Even semester: ₹46,000.

Room occupancy may range from 2 to 8 students depending on the block.
Reported facilities may include room furnishings, backup power,
Wi-Fi, drinking water and laundry.

Availability, room type, fees and facilities must be confirmed
with the university.

Official hostel page:
https://kanchiuniv.ac.in/campus-life/hostel/
"""

MESS_INFO = """
HOSTEL MESS AND FOOD

Reported food options include vegetarian South Indian, North Indian
and Andhra-style meals.

Indicative meal timings:
Breakfast: 06:50 AM-07:50 AM
Lunch: 01:00 PM-02:00 PM
Tea and snacks: 04:30 PM-05:30 PM
Dinner: 07:00 PM-08:30 PM

Actual menus, meal timings and charges may change.
"""

CANTEEN_INFO = """
CAMPUS CANTEEN

The campus is reported to have a Day Scholar and Visitor Canteen.
Reported offerings include breakfast, lunch, tiffin items, snacks,
tea and filter coffee.

Current opening hours, prices and menus should be confirmed on campus.
"""

# ============================================================
# 11. PLACEMENTS
# ============================================================

PLACEMENT_INFO = """
PLACEMENT INFORMATION
(Reported indicative figures; not guaranteed)

Highest reported package: ₹8.00-₹8.50 LPA.
Average reported package: ₹4.00-₹6.50 LPA.
Lower-end reported packages: ₹1.44-₹2.25 LPA.

Reported recruiters include:
- Cognizant
- TCS
- Accenture
- Hexaware Technologies

Actual placements and salary packages depend on the year, programme,
employer, student performance and available opportunities.

Confirm the latest placement report with the university.
"""

# ============================================================
# 12. SCHOLARSHIPS
# ============================================================

SCHOLARSHIP_INFO = """
SCHOLARSHIPS AND FEE CONCESSIONS

Scholarships or fee concessions may be available based on academic
merit and eligibility.

Reported nearby districts associated with possible concessions include:
Chennai, Kanchipuram, Chengalpattu, Ranipet, Vellore,
Tiruvannamalai and Tiruvallur.

A previous information summary mentioned merit relief of up to ₹95,000,
but this amount and eligibility have not been independently verified.

Contact the admissions office to confirm current scholarship schemes,
eligibility, required documents and deadlines.
"""

# ============================================================
# 13. CURRICULUM
# ============================================================

CURRICULUM_INFO = """
CURRICULUM AND SYLLABUS

The curriculum depends on the course, academic year and applicable
university regulations.

Some programmes may use a Choice Based Credit System (CBCS).
Coursework may include lectures, practicals, projects, electives,
internal assessment and semester examinations.

Some curricula may integrate Sanskrit, Indian Culture or related
subjects alongside modern academic disciplines.

Credit requirements and assessment weights differ by programme.
Check the latest syllabus published by the relevant department.
"""

# ============================================================
# 14. ACCREDITATION
# ============================================================

ACCREDITATION_INFO = """
ACCREDITATION AND CERTIFICATES

For current NAAC accreditation grade, validity, approvals and
institutional certificates, consult the university's official website
or administration.

A previous information summary reported a NAAC Grade A, but the
current grade and validity should be checked against official records.

University website:
https://www.kanchiuniv.ac.in/
"""

# ============================================================
# 15. LIBRARY
# ============================================================

LIBRARY_INFO = """
CENTRAL LIBRARY

The university has the Sri Chandrasekharendra Saraswathi Central Library.

Reported resources include:
- Books and reference materials
- Academic journals
- Digital learning resources
- Historical or rare manuscript collections

Previous information summaries mentioned more than 200,000 volumes,
over 100 journals and a collection of rare manuscripts. These figures
should be verified with the library.

Reported opening hours: Monday-Friday, approximately 9:00 AM-6:00 PM.
Current timings may differ.
"""

# ============================================================
# 16. WIFI
# ============================================================

WIFI_INFO = """
CAMPUS WI-FI

Wi-Fi has been reported in academic areas and student hostels.
Access may require university login credentials.

Coverage, speed, availability and usage rules depend on current
campus IT arrangements. Contact the university IT support team
for confirmed details.
"""

# ============================================================
# 17. LABORATORIES
# ============================================================

LAB_INFO = """
LABORATORIES AND TECHNICAL FACILITIES

Laboratory facilities vary by department.

Previously reported engineering resources include:
- CAD/CAM facilities
- Electrical and electronics laboratories
- Testing equipment
- Universal Testing Machines
- Geotechnical testing facilities
- Electro-pneumatic training arrays
- LabVIEW-related resources
- Siemens PLC-related equipment
- ARISTO 6XT Robot

The availability of specific equipment should be confirmed with
the relevant department.
"""

# ============================================================
# 18. MEDICAL FACILITIES
# ============================================================

MEDICAL_INFO = """
MEDICAL FACILITIES

A campus sick room and medical assistance have been reported.
Sankara Multi Speciality Hospital is reported nearby in Enathur.

Facilities and opening hours may change. For an emergency, contact
local emergency services or campus administration immediately.
"""

# ============================================================
# 19. CULTURAL EVENTS
# ============================================================

CULTURE_INFO = """
CULTURAL ACTIVITIES

Reported cultural activities include:

TARUNYAM:
An annual youth festival that may include dance, music, drama,
fashion and fine arts.

NADA SAMARPANA AND TYAGARAJA ARADHANA:
Events associated with Indian classical music and cultural heritage.

TEJAS YOGA FESTIVAL:
Yoga-related activities reportedly associated with International Yoga Day.

Other activities may include cultural nights, music, dance and
interdepartmental programmes.

Event names, dates and activities can change each year.

Cultural information:
https://kanchiuniv.ac.in/cultural-foot.htm
"""

# ============================================================
# 20. SPORTS AND PHYSICAL EDUCATION
# ============================================================

SPORTS_INFO = """
SPORTS AND PHYSICAL EDUCATION

Sports and physical education activities depend on current facilities
and university schedules.

Contact the Physical Education Department for details about sports,
competitions, playgrounds, fitness facilities and student participation.
"""

# ============================================================
# 21. TEACHING METHODS
# ============================================================

TEACHING_INFO = """
TEACHING AND LEARNING

Teaching methods depend on the programme and department and may include:
- Classroom lectures
- Laboratory practicals
- Assignments
- Seminars and presentations
- Projects
- Internal assessments
- Semester examinations

Contact the relevant department for its current teaching and
assessment arrangements.
"""

# ============================================================
# 22. DEPARTMENT COUNT
# ============================================================

DEPARTMENT_INFO = """
ACADEMIC DEPARTMENTS

The university offers programmes across areas including:
- Engineering and Technology
- Science
- Arts and Humanities
- Sanskrit and Indian Culture
- Management Studies and Commerce
- Law
- Education
- Health-related programmes

A previous summary reported around 9 major faculties and approximately
21 departments. The current count and department structure should be
verified in the official academic directory:

https://kanchiuniv.ac.in/academics/
"""

# ============================================================
# 23. CONTACT INFORMATION
# ============================================================

CONTACT_INFO = f"""
UNIVERSITY CONTACT INFORMATION

Name: {COLLEGE_NAME}
Address: {COLLEGE_INFO['location']}
Established: {COLLEGE_INFO['established']}
Institution type: {COLLEGE_INFO['type']}

Phone: {COLLEGE_INFO['phone']}
Admissions email: {COLLEGE_INFO['email']}
Registrar email: {COLLEGE_INFO['registrar_email']}

Website: {COLLEGE_INFO['website']}
Academic directory: {COLLEGE_INFO['academic_directory']}
"""

# ============================================================
# 24. HELPER FUNCTIONS
# ============================================================

def normalize(text):
    """Convert user input to lowercase and normalize spaces."""
    return re.sub(r"\s+", " ", text.lower().strip())


def get_response(user_message):
    """Generate a response to a college enquiry."""

    message = normalize(user_message)

    if not message:
        return "Please type your question about SCSVMV."

    # Greetings
    if any(word in message for word in [
        "hello", "hi", "hey", "good morning",
        "good afternoon", "good evening"
    ]):
        return (
            f"Hello! Welcome to the {COLLEGE_NAME} enquiry chatbot.\n"
            "You can ask about courses, fees, admissions, CSE, timetable, "
            "examinations, attendance, placements, faculty, hostels, "
            "transport, library, laboratories and cultural activities."
        )

    if any(word in message for word in ["thank you", "thanks"]):
        return "You're welcome! Please ask if you need more information."

    if message in ["bye", "goodbye", "exit", "quit", "stop"]:
        return "Thank you for contacting SCSVMV. Goodbye!"

    # Daily timetable
    if any(word in message for word in [
        "timetable", "time table", "daily schedule",
        "class timing", "class timings", "college timing",
        "college hours", "working hours", "lunch break",
        "recess", "break time", "class schedule",
        "college starts", "college ends", "regular classes",
        "regular class", "daily classes"
    ]):
        return DAILY_TIMETABLE

    # CSE-specific timetable
    if any(word in message for word in [
        "cse timetable", "cse time table", "cse class timing",
        "computer science timetable", "computer science time table",
        "cse period", "cse schedule", "cse class schedule",
        "cse subject timetable"
    ]):
        return CSE_TIMETABLE_INFO

    # CSE course structure
    if any(word in message for word in [
        "cse syllabus", "cse course structure",
        "computer science syllabus", "computer science course structure",
        "cse credits", "btech cse", "b.tech cse",
        "b.e. cse", "cse subjects", "cse curriculum",
        "computer engineering syllabus", "cse first year",
        "cse second year", "cse third year", "cse fourth year",
        "cse final year", "cse project"
    ]):
        return CSE_COURSE_STRUCTURE

    # Examination, marks and attendance
    if any(word in message for word in [
        "exam pattern", "evaluation", "assessment",
        "internal marks", "external marks", "40%",
        "60%", "pass mark", "passing marks", "24 out of 60",
        "attendance", "attendance shortage", "i grade",
        "semester exam", "end semester", "end-semester",
        "exam eligibility", "minimum attendance", "attendance percentage"
    ]):
        return EXAMINATION_INFO

    # College details
    if any(word in message for word in [
        "college name", "university name", "about college",
        "about university", "what is scsvmv",
        "tell me about the college", "established",
        "deemed university"
    ]):
        return (
            f"University: {COLLEGE_NAME}\n"
            f"Location: {COLLEGE_INFO['location']}\n"
            f"Established: {COLLEGE_INFO['established']}\n"
            f"Type: {COLLEGE_INFO['type']}\n"
            f"Website: {COLLEGE_INFO['website']}"
        )

    if any(word in message for word in [
        "location", "address", "where is", "college place",
        "university place"
    ]):
        return f"The university is located at {COLLEGE_INFO['location']}."

    # Contact details
    if any(word in message for word in [
        "contact", "phone", "telephone", "email", "e-mail",
        "website", "admission office", "registrar"
    ]):
        return CONTACT_INFO

    # Course fees
    if any(word in message for word in [
        "fee", "fees", "tuition", "cost", "price", "how much"
    ]):
        if any(word in message for word in ["bams", "b.a.m.s", "ayurveda"]):
            key = "bams"
        elif any(word in message for word in ["btech", "b.tech", "engineering"]):
            key = "btech"
        elif any(word in message for word in ["b.e.", " be fee", " be fees"]):
            key = "be"
        elif any(word in message for word in ["b.sc", "bsc"]):
            key = "bsc"
        elif any(word in message for word in ["b.com", "bcom", "commerce"]):
            key = "bcom"
        elif "mba" in message:
            key = "mba"
        elif "bca" in message:
            key = "bca"
        elif "bba" in message:
            key = "bba"
        elif any(word in message for word in ["law", "llb", "ll.b"]):
            key = "law"
        else:
            return (
                "Please specify the course for which you need the fee, "
                "such as B.Tech, B.Sc., B.Com., MBA, BAMS, BCA, BBA or Law. "
                "The figures in this chatbot are estimates and must be "
                "confirmed with the admissions office."
            )

        return (
            f"Indicative fee for {key.upper()}: {FEES[key]}.\n"
            "Fees may change by batch and may exclude additional charges. "
            "Confirm the current official fee structure."
        )

    # Admissions
    if any(word in message for word in [
        "admission", "apply", "application", "eligibility",
        "entrance exam", "join college", "how to join"
    ]):
        if any(word in message for word in ["bams", "ayurveda"]):
            return ADMISSIONS["bams"]

        if any(word in message for word in [
            "btech", "b.tech", "engineering", "b.e."
        ]):
            return ADMISSIONS["engineering"]

        if "mba" in message:
            return ADMISSIONS["mba"]

        return ADMISSIONS["general"]

    # Scholarships
    if any(word in message for word in [
        "scholarship", "scholarships", "fee concession",
        "fee waiver", "financial aid", "merit concession"
    ]):
        return SCHOLARSHIP_INFO

    # Placements
    if any(word in message for word in [
        "placement", "placements", "salary", "package", "lpa",
        "recruiter", "job opportunity", "highest package",
        "average package", "lowest package"
    ]):
        if any(word in message for word in [
            "highest", "maximum", "top package"
        ]):
            return (
                "Reported highest placement package: ₹8.00–₹8.50 LPA. "
                "This is an indicative, unverified range and is not guaranteed."
            )

        if any(word in message for word in [
            "average", "mean package"
        ]):
            return (
                "Reported average placement package: ₹4.00–₹6.50 LPA. "
                "Actual outcomes vary by year, course, student and employer."
            )

        if any(word in message for word in [
            "lowest", "minimum package"
        ]):
            return (
                "Reported lower-end packages: ₹1.44–₹2.25 LPA. "
                "This is not a guaranteed minimum salary."
            )

        return PLACEMENT_INFO

    # Faculty
    if any(word in message for word in [
        "faculty", "professor", "teacher", "lecturer",
        "staff names", "hod", "head of department"
    ]):
        if any(word in message for word in [
            "cse", "computer science"
        ]):
            key = "cse"
        elif any(word in message for word in ["eee", "electrical"]):
            key = "eee"
        elif any(word in message for word in ["ece", "electronics"]):
            key = "ece"
        elif any(word in message for word in ["management", "commerce"]):
            key = "management"
        elif "law" in message:
            key = "law"
        elif "education" in message:
            key = "education"
        else:
            return (
                "Which department's faculty do you need: CSE, EEE, ECE, "
                "Management, Law or Education? You can also visit "
                "https://kanchiuniv.ac.in/academics/."
            )

        details = FACULTY[key]
        return (
            f"Reported faculty for {key.upper()}:\n"
            + "\n".join(details["names"])
            + f"\nOfficial directory: {details['url']}\n"
            "Please verify current names and designations."
        )

    # Departments
    if any(word in message for word in [
        "departments", "how many departments",
        "faculties", "academic schools", "department list"
    ]):
        return DEPARTMENT_INFO

    # Hostel food before general hostel response
    if any(word in message for word in [
        "hostel food", "mess food", "mess menu",
        "hostel menu", "hostel breakfast", "hostel lunch",
        "hostel dinner", "food timing"
    ]):
        return MESS_INFO

    # Hostel
    if any(word in message for word in [
        "hostel", "hostel fee", "boys hostel",
        "girls hostel", "hostel room", "accommodation",
        "hostel facilities", "room sharing"
    ]):
        return HOSTEL_INFO

    # Canteen
    if any(word in message for word in [
        "canteen", "canteen food", "canteen timing",
        "canteen menu", "food prices"
    ]):
        return CANTEEN_INFO

    # General food
    if any(word in message for word in [
        "food", "mess", "menu", "breakfast", "lunch",
        "dinner", "snacks", "vegetarian"
    ]):
        return MESS_INFO + "\n" + CANTEEN_INFO

    # Specific bus routes
    for place, details in BUS_ROUTES.items():
        if place in message:
            return (
                details
                + "\nConfirm the current route and charges with "
                "the university transport office."
            )

    # General transport
    if any(word in message for word in [
        "bus", "transport", "bus route", "bus fee",
        "college vehicle", "college bus"
    ]):
        return TRANSPORT_INFO

    # Library
    if any(word in message for word in [
        "library", "books", "journals", "reading room",
        "digital library", "library timing", "central library"
    ]):
        return LIBRARY_INFO

    # Wi-Fi
    if any(word in message for word in [
        "wifi", "wi-fi", "internet", "wireless"
    ]):
        return WIFI_INFO

    # Curriculum
    if any(word in message for word in [
        "curriculum", "syllabus", "subjects",
        "credit system", "cbc", "course structure"
    ]):
        return CURRICULUM_INFO

    # Accreditation
    if any(word in message for word in [
        "naac", "accreditation", "grade", "certificate",
        "approval", "recognition", "ugc"
    ]):
        return ACCREDITATION_INFO

    # Laboratories
    if any(word in message for word in [
        "lab", "labs", "laboratory", "laboratories",
        "workshop", "equipment"
    ]):
        return LAB_INFO

    # Medical facilities
    if any(word in message for word in [
        "medical", "hospital", "doctor", "health centre",
        "health center", "first aid", "sick room", "emergency"
    ]):
        return MEDICAL_INFO

    # Teaching methods
    if any(word in message for word in [
        "teaching", "teaching quality", "learning",
        "education quality", "teaching method"
    ]):
        return TEACHING_INFO

    # Cultural events
    if any(word in message for word in [
        "tarunyam", "cultural", "culture", "festival",
        "dance", "music", "drama", "saufest",
        "cultural events"
    ]):
        return CULTURE_INFO

    # Classical music events
    if any(word in message for word in [
        "nada samarpana", "tyagaraja", "thyagaraja",
        "aradhana", "classical music"
    ]):
        return (
            "Nada Samarpana and Tyagaraja Aradhana are associated with "
            "Indian classical music and cultural heritage. Check the "
            "university's announcements for current dates.\n"
            "Cultural page: https://kanchiuniv.ac.in/cultural-foot.htm"
        )

    # Yoga
    if any(word in message for word in [
        "yoga", "tejas", "international yoga day"
    ]):
        return (
            "Yoga-related activities may include the reported Tejas Yoga "
            "Festival around International Yoga Day. Check university "
            "announcements for current dates."
        )

    # Sports
    if any(word in message for word in [
        "sports", "games", "playground", "gym", "fitness"
    ]):
        return SPORTS_INFO

    # Campus facilities
    if any(word in message for word in [
        "facilities", "campus", "infrastructure", "amenities"
    ]):
        return (
            "Reported campus facilities include academic buildings, "
            "department laboratories, a central library, hostels, canteen, "
            "transport, sports activities and medical assistance. "
            "Availability should be confirmed with the university."
        )

    # General help
    if any(word in message for word in [
        "help", "what can you do", "topics", "options"
    ]):
        return (
            "I can answer questions about:\n"
            "1. College information and contact details\n"
            "2. Courses and departments\n"
            "3. Course fees and admissions\n"
            "4. Scholarships and placements\n"
            "5. Faculty information\n"
            "6. Regular daily timetable\n"
            "7. CSE timetable and course structure\n"
            "8. Internal/external examinations and attendance\n"
            "9. Hostels, rooms and food\n"
            "10. Bus routes and transport fees\n"
            "11. Library, Wi-Fi and laboratories\n"
            "12. Medical facilities and teaching\n"
            "13. Accreditation, sports and campus facilities\n"
            "14. Cultural festivals, classical music and yoga"
        )

    # Default response
    return random.choice([
        "Sorry, I couldn't understand your question. Try asking about courses, fees, admissions, timetable, CSE subjects, exams, placements or transport.",
        "I can help with SCSVMV enquiries. Type 'help' to see the topics I support.",
        "Please rephrase your question or ask about a specific department, course, facility or campus service.",
    ])


# ============================================================
# 25. RUN DIRECTLY FROM THE TERMINAL
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print(COLLEGE_NAME)
    print("College Enquiry Chatbot")
    print("Type 'help' to see available topics.")
    print("Type 'exit' to stop.")
    print("=" * 60)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Bot: Thank you for contacting SCSVMV. Goodbye!")
            break

        print("\nBot:", get_response(user_input))

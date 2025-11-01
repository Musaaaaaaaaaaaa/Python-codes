##Name: Moosa Abbasi
##U-Number: U37033529
##Brief description of program: Write a program that creates a tuple for the following course numbers:


course_names = {
    'COP 2510': 'Programming Concepts',
    'EGN 3000L': 'Foundations of Engineering Lab',
    'MAC 2281': 'Calculus I',
    'MUH 3016': 'Survey of Jazz',
    'PHY 2048': 'General Physics I',
}

instructors = {
    'COP 2510': 'S. Small',
    'EGN 3000L': 'J. Anderson',
    'MAC 2281': 'A. Makaryus',
    'MUH 3016': 'A. Wilkins',
    'PHY 2048': 'G. Pradhan',
}

class_times = {
    'COP 2510': 'TR 8:00am – 9:15am',
    'EGN 3000L': 'TR 11:00am – 12:15pm',
    'MAC 2281': 'MW 9:30am – 10:45am',
    'MUH 3016': 'online asynchronous',
    'PHY 2048': 'TR 5:00pm – 6:15pm',
}

def search_course_info(course_number):
    if course_number in course_names:
        ##print(f"Course Number: {course_number}")
        print('The course details are:') 
        print(f"Course Name: {course_names[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Class Times: {class_times[course_number]}")
    else:
        print(f"Course {course_number} is an invalid number.")

while True:
    user_input = input("Enter a course number (e.g., COP 2510): ")
    if user_input == "quit":
       break
    search_course_info(user_input)
    break

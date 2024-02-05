class StudentEnrollement:
    def __init__(self, student_id, course_id, semester, year):
        self.PersonalInfo = None
        self.acedamicInfo = None
        self.locations = ['peshawar', 'islamabad', 'lahore', 'karachi']

    def signUp(self):
        name = input("Enter your name: ")
        father_name = input("Enter your father name: ")
        email = input("Enter your email: ")

        location = input("Enter your location: ")
        if location not in self.locations:
            print("Invalid location")
            return
        
        self.PersonalInfo = {
            'name': name,
            'father_name': father_name,
            'email': email,
            'location': location
        }

    def getAcedamicinfo(self):

        if self.PersonalInfo is None:
            print("Please sign up first")
            return
        else:
            degree = input("Enter your degree: ")
            cgpa = input("Enter your cgpa: ")
            self.acedamicInfo = {
                'degree': degree,
                'cgpa': cgpa
            }
    def finalMsg(self):
        print("Thank you for signing up")

def printingHello(name):
    print("Hello " + name)

def greeting(name):
    print("Welcome " + name)
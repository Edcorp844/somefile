import time

class student:
    def __init__(self, firstname:str, othernames:str, dateOFBirth:str, course_taken:str, reg_number:str, phone_number = None, email = None):
        self.firstname = firstname
        self.othernames = othernames
        self.dateOFBirth = dateOFBirth
        self.course_taken = course_taken
        self.yearOfBirth =  dateOFBirth[-4:]
        self.reg_number = reg_number
        self.phone_number = phone_number
        self.email = email

    # Method to calculate age auotomaticall accordind to the date of birth
    # the date must be in formart "dd/mm/yyy"
    def get_age(self):
       age = int(time.asctime()[-4:]) - int(self.yearOfBirth) 
       return age
    
    def store(self):
        student_array = []
        student_array.append({"firstname":self.firstname})
        student_array.append({"othernames":self.othernames})
        student_array.append({"date_of_birth":self.dateOFBirth})
        student_array.append({"course_taken":self.course_taken})
        student_array.append({"reg_number":self.reg_number})
        if self.phone_number != None:
            student_array.append({"phone_number":self.phone_number})
        if self.email != None:
            student_array.append({"email":self.email})
        
        return student_array

    # Method to store the student details in the database
    
    def to_database(self):
        #code here
        pass

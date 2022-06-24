################################################################
# This software is under the creative license of EDCORP        #
# Copy rights for Edson Corperations                           #
################################################################


class grade:
    def __init__(self, array, course_unit_name = None, score = None, credit_unit = None):
        self.arr = array
        self.course_unit = course_unit_name
        self.score = score
        self.credit_unit = credit_unit
        self.grade()
    
    def assign_grades(self):
        if self.score >= 80:
            grade = 'A'
            gp    =  5.0
        elif self.score >= 75:
            grade = 'B+' 
            gp    =  4.5
        elif self.score >= 70:
            grade = 'B'
            gp    =  4.0
        elif self.score >= 65:
            grade = 'B-'
            gp    =  3.5
        elif self.score >= 60:
            grade = 'C+'
            gp    =  3.0
        elif self.score >= 55:
            grade = 'C'
            gp    =  2.5
        elif self.score >= 50:
            grade = 'C-'
            gp    =  2.0
        elif self.score >= 45:
            grade = 'D+'
            gp    =  1.5
        elif self.score >= 40:
            grade = 'D'
            gp    =  1.0
        elif self.score >= 35:
            grade = 'D-'
            gp    =  0.5
        else:
            grade = 'E'
            gp    =  0


        self.container = []
        self.container.append(gp)
        self.container.append(grade)


    def grade(self):
        if self.score == None:
            pass
        else:
            self.assign_grades()
            gp = self.container[0]
            gpa = gp * self.credit_unit
            container = []
            container.append(self.course_unit)
            container.append(self.score)
            container.append(self.container[0])
            container.append(self.container[1])
            container.append(self.credit_unit)
            container.append(gpa)
            self.arr.append(container)

    def GPA(self):
        sum_gp = 0
        sum_credit_unit = 0

        for i in range (0, len(self.arr)):
            course = self.arr[i]
            sum_gp += course[5]

        for i in range (0, len(self.arr)):
            course = self.arr[i]
            sum_credit_unit += course[2]

        gpa = sum_gp / sum_credit_unit

        return gpa
        

arr = []
credit_unit = grade(arr, 'credit_unit1', 72, 3)
credit_unit = grade(arr, 'credit_unit1', 55, 3)
credit_unit = grade(arr, 'credit_unit3', 60, 4)
credit_unit = grade(arr, 'credit_unit4', 59, 4)
credit_unit = grade(arr, 'credit_unit5', 86, 4)
print(arr)
print(f"GPA = {grade(arr).GPA():.2f}")

class Student:

    numofStudent = 0              # class attribute to count students

    def __init__(self, id, name):    
        self.id = id
        self.name = name           

        Student.numofStudent = Student.numofStudent + 1 # increament 'numofStudent , when a new student is cerated.

    # definig setters and getters mnethods for the attributes name and id:
    
    # For ids:
    @property
    def getid(self):              # id getter  
        return self._id

    @getid.setter                 # id setter
    def setid(self, newvalue):
        if newvalue >= 0:
            self._id = newvalue
        else:
            print('id cannot be negative.')
    
    # For names:
    @property
    def getname(self):             # name getter
        return self._name

    @getname.setter                # name setter
    def setname(self, newname):
        if newname == '':
            print('name cannot be empty.')
        else:
            self._name = newname

    # string representation method of the student object:
    def __str__(self):     
        return (f'Student id: {self.id:>10} \t name: {self.name:>10}')
   

# Function to create a list of student objects from the student list of dictionaries: 
def makeStudent(student_dict_list):

    students_list = []   # to hold student objects   

    # making list of student objects by calling 'Student' class and pass the parameters 'id', 'name':
    # using a given list of student dictinonaries:

    for student_dict in student_dict_list:  # iterate over student dictionaries 

        # creating student objects (Student(id, name)):
        student_obj = Student(student_dict['id'], student_dict['name'])  # creates a new student object
        
        # append the student object to the 'students_list':
        students_list.append(student_obj)  

    return students_list

# Function to delete a student object form with a given ID number:
def deleteOneStudent(slist, did):
    
    # making a new list of students excluding the student that has id = did:  
    new_list = list(filter(lambda student: student.id != did, slist))

    # checking if the original list 'slist' is changed:
    if len(new_list) != len(slist):  # if True, means the selected student by id is deleted

        # update the original list in place:
        slist[:] = new_list

        # since one student is deleted , decrease the the number of student objects here:
        Student.numofStudent = Student.numofStudent - 1
        
        # printing the user feedback after the delete:
        print('\nThe student with ID', did, 'was successfully deleted.')

    else:   # if the id was not found( same length for both list )
        print('\nstudent with ID equal to', did, 'was not found.')    

  
    
def main():

    student_dict_list = [{'id': 1001, 'name': 'John'},
                         {'id': 1002, 'name': 'James'},
                         {'id': 1003, 'name': 'Mark'},
                         {'id': 1004, 'name': 'Matthew'},
                         {'id': 1005, 'name': 'Arnold'}]

    slist = makeStudent(student_dict_list)

    print(f'\n**** Total number of students: {Student.numofStudent}')
    for s in slist:
        print(s)

    # Delete one object

    did = 1003

    deleteOneStudent(slist, did)

    print(f'\n**** Total number of students: {Student.numofStudent}')
    for s in slist:
        print(s)


if __name__ == '__main__':
    main()



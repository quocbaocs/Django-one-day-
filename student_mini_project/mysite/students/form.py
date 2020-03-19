from .models import Student

class StudentForm():

    def __init__(self, request=None, dbModel=None):
        self.studentNo = ''
        self.studentName =''
        self.address = ''

        if request:
            self.studentId = request.POST['studentId']
            self.studentNo = request.POST['studentNo']
            self.studentName = request.POST['studentName']
            self.address = request.POST['address']
        elif dbModel:
            self.studentId = dbModel.id
            self.studentNo = dbModel.studentNo
            self.studentName = dbModel.studentName
            self.address = dbModel.address
    
    def validate(self):
        errorList = []
        if not self.studentNo:
            errorList.append('Student number is required')
        
        if not self.studentName:
            errorList.append('Student name is required')
        
        if not self.address:
            errorList.append('Address is required')
        
        return errorList
        
    def save(self):
        student = Student()
        student.id = int(self.studentId) if self.studentId else None
        student.studentNo = self.studentNo
        student.studentName = self.studentName
        student.address = self.address
        student.save() 
# class_struct_student.py

class Student:
    SUBJECT = 3

    def __init__(self, name, subject):
        self.name = name
        self.subject = []
        for x in subject:
            self.subject.append(x)
        self.total = 0
        self.average = 0.0
        self.grade = ' '

        self.calculate()

    def calculate(self):
        for x in self.subject:
            self.total += x

        self.average = self.total / self.SUBJECT

        if self.average >= 90:
            self.grade = 'Excellent'
        elif self.average < 60:
            self.grade = 'Fail'
        else:
            self.grade = ' '

    def printStudentInfo(self):
        print('{0:<10}'.format(self.name), end='')
        for x in self.subject:
            print('{:<3}'.format(x), end='')

        print('{0:<5} {1:6.2f} {2:<10}'.format(self.total, self.average, self.grade))


class ControlScoreTable:
    STUDENT = 10

    def __init__(self):
        self.students = []
        return

    def inputStudentInfo(self, student):
        self.students.append(student)
        return

    def printScoreTable(self):
        for s in self.students:
            s.printStudentInfo()

        return


class ViewScoreTable:
    MAX = 10
    count = 0

    def __init__(self):
        self.controlScoreTable = ControlScoreTable()
        return

    def ViewMenu(self):
        self.inputStudentInfo()
        self.printScoreTable()
        return

    def inputStudentInfo(self):
        print('\n')
        name = input('Input name : ')

        while name != 'end' and self.count <= self.MAX:
            self.count = self.count + 1
            subject = []
            for x in range(Student.SUBJECT):
                input_subject = int(input('Input subject[' + str(x + 1) + '] : '))
                subject.append(input_subject)

            student = Student(name, subject)
            self.controlScoreTable.inputStudentInfo(student)

            print('\n')
            name = input('Input name: ')
        return

    def printScoreTable(self):
        self.controlScoreTable.printScoreTable()
        return


if __name__ == '__main__':
    viewScoreTable = ViewScoreTable()
    viewScoreTable.ViewMenu()




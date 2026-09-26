class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        length = len(self.marks)
        sum = 0
        for i in self.marks:
            sum+=i
        avg = sum / length
        return avg

s1 = Student("XYZ",[90,99,97])
print(f"{s1.avg():.2f}")
from time import time

class SdtGrade:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def get_name(self):
        return self._name
    
    def put_eng(self, score):
        self._eng = score

    def put_math(self, score):
        self._math = score

    def put_kor(self,score):
        self._kor = score
        
    def get_avg(self):
        return (self._eng + self._math + self._kor) / 3

if __name__ == '__main__':
    start_time = time()
    lines_eng = open("English.txt").readlines()
    lines_math = open("Math.txt").readlines()
    lines_kor = open("Korean.txt").readlines()
    myclass = []

    for line in lines_eng:
        line_split = line.split()
        name = line_split[0]
        eng_score = int(line_split[1])

        student = SdtGrade(name)
        student.put_eng(eng_score)
        myclass.append(student)
        
           
    for line in lines_math:
        line_split = line.split()
        name = line_split[0]
        math_score = int(line_split[1])

        for student in myclass:
            if student.get_name() == name:
                student.put_math(math_score)
                break

    for line in lines_kor:
        line_split = line.split()
        name = line_split[0]
        kor_score = int(line_split[1])

        for student in myclass:
            if student.get_name() == name:
                student.put_kor(kor_score)
                break

    for student in myclass:
        avg = student.get_avg()
        print(f"{student.get_name()}: {avg:.2f}")


    end_time = time()
    print('Run time:', end_time-start_time)

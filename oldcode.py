from time import time

if __name__ == '__main__':
    start_time = time()
    
    lines_eng = open("English.txt").readlines()
    lines_math = open("Math.txt").readlines()
    lines_kor = open("Korean.txt").readlines()

    for line_eng in lines_eng: 
       eng_name = line_eng.split()[0]
       eng_score = int(line_eng.split()[1])

       for line_math in lines_math:
           math_name = line_math.split()[0]
           math_score = int(line_math.split()[1])

           for line_kor in lines_kor:
               kor_name = line_kor.split()[0]
               kor_score = int(line_kor.split()[1])

               if eng_name == math_name == kor_name:
                  average = (eng_score + math_score + kor_score) / 3
                  print(f"{eng_name}: {average:.2f}")


    end_time = time()
    print('Run time:', end_time-start_time)



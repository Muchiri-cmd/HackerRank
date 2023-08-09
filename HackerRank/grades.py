if __name__ == '__main__':
    records=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])#add student records
        scores.append(score)#append scores in scores list 2 get 2nd lowest
        
    #find the 2nd lowest grade
    grades=sorted(list(set(scores)))
    second_l=grades[1]#second lowest grade
    
    #get which records have the grade and print names
    students=[record[0]for record in records if record[1]==second_l]
            
    for student in sorted(students):
        print(student)
           
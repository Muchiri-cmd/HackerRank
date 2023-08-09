if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        scores=student_marks[query_name]
        average=sum(scores)/len(scores)
        print("{:.2f}".format(average))
    else:
        print("student not found")
    
    
    
    
    
    """loops through dictionary and checks for queried name
    for k,v in student_marks.items():
        if k==query_name:
            average=sum(v)/len(v)
            
    print("{:.2f}".format(average))"""
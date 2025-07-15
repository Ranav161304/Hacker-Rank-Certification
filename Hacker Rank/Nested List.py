if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Extract all scores and find the second lowest
    scores = sorted({student[1] for student in students})
    second_lowest = scores[1]
    
    # Collect names of students with the second lowest score
    result = [student[0] for student in students if student[1] == second_lowest]
    
    # Sort names alphabetically and print each on a new line
    for name in sorted(result):
        print(name)

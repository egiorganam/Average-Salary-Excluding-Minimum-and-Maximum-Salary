salary = [4000, 3000, 1000, 2000]

def average(salary):
    salary.sort()
    salary.pop(0)
    salary.pop()

    average = sum(salary) // len(salary)
    print(average)


average(salary)
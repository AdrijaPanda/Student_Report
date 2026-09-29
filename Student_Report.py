name = input("enter name")
math = int(input("enter marks of math"))
python = int(input("enter marks of python"))
envs = int(input("enter marks of envs"))
english = int(input("enter marks of english"))
print("total marks : ", math + python + envs + english )
total = math + python + envs + english 
percentage = (total/400)*100
print (" percentage:", percentage)
highest = math
if python>highest:
    highest= python
if envs>highest:
    highest=envs
if english>highest:
    highest=english
print("highest:", highest)
lowest = math
if python<math:
    lowest=python
if envs<python:
    lowest=envs
if english < envs:
    lowest = english
print("lowest:",lowest)
if percentage >= 90:
    grade = "S"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "C"
else:
    grade = "D"
if percentage >=50:
    result="Pass"
else:
    result="Fail"

print("----STUDENT'S PERFORMANCE REPORT----")
print("NAME OF THE STUDENT:",name)
print("Math:",math)
print("PYTHON:",python)
print("EVVS:",envs)
print("ENGLISH:",english)
print("TOTAL:",total)
print("PERCENTAGE:",percentage)
print("HIGHEST:",highest)
print("LOWEST:",lowest)
print("GRADE:",grade)
print("RESULT:",result)

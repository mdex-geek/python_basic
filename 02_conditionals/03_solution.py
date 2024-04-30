score =190

if score >100:
    print("verify your grade one again")
    exit()

if score >=90:
    grade = "A"
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'c'
elif score >= 60:
    grade = "d"
else:
    grade ="f"

print(grade)
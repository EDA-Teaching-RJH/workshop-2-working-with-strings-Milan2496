#Grade Calculator

grade = int(input("What is your score out of 100"))


if grade > 100 or grade < 0:
    print("Invalid answer")
else:
    if grade > 89:
        print("Grade A")
    elif grade > 79:
        print("Grade B")
    elif grade > 69:
        print("Grade C")
    elif grade > 59:
        print("Grade D")
    else:
        print("Fail")
    
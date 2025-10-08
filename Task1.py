students={"Alice":50,"Riya":98,"Sanjay":96,"Shiv":88}
studentname=str(input("Enter  the student's name:"))

if (studentname in students):
    print(f"{studentname}'s mark is:{students[studentname]}")

else:
    print("Student not found.")
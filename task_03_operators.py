print("Student Marks Calculator:")

bangla = float(input("Enter Bangla marks: "))
english = float(input("Enter English marks: "))
math = float(input("Enter Math marks: "))


total_marks = bangla + english + math
average_marks = total_marks / 3


is_passed = average_marks >= 40


print("\nResults:")
print(f"Total Marks   = {total_marks}")
print(f"Average Marks = {average_marks:.2f}") 

if is_passed:
    print("Status: Pass")
else:
    print("Status: Fail")
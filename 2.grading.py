# 2.grading.py
# โปรแกรมคำนวณเกรดจากคะแนนกลางภาคหรือปลายภาค
score = float(input("entet_your_score"))

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("c")
elif score >= 50:
    print("D")
else:
    print("F")
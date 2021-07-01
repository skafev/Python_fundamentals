def grades(number):
    if 2 < number < 3:
        return "Fail"
    if 3 <= number < 3.5:
        return "Poor"
    if 3.5 <= number < 4.5:
        return "Good"
    if 4.5 <= number < 5.5:
        return "Very Good"
    if 5.5 <= number < 6:
        return "Excellent"


number = float(input())
print(grades(number))
""" Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
of the number of students, and the mean and median tuition values. """

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(list_universities):
    student_enrollment = []
    university_tuition = []
    for i in range(len(list_universities)):
        student_enrollment.append(list_universities[i][1])
        university_tuition.append(list_universities[i][2])
    return student_enrollment, university_tuition


def mean(a_list):
    return sum(a_list)/len(a_list)

def median(a_list):
    a_list.sort()
    if len(a_list) % 2 != 0:
        return a_list[len(a_list)//2]
    else:
        left = a_list[(len(a_list)+1)//2]
        right = a_list[(len(a_list)-1)//2]
        return mean(list(left, right))

enrollment = enrollment_stats(universities)

print("*" * 30, end="\n")

print(f"Total students: {' ' * 2}{sum(enrollment[0]):,}")
print(f"Total tuition:  ${' ' * 1}{sum(enrollment[1]):,}")

print("\n")

print(f"Student mean: {' ' * 2}{mean(enrollment[0]):,.2f}")
print(f"Student median:{' ' * 1}{median(enrollment[0]):,}")

print("\n")

print(f"Tuition mean:   ${' ' * 1}{mean(enrollment[1]):,.2f}")
print(f"Tuition median: ${' ' * 1}{median(enrollment[1]):,}", end="\n\n")
print("*" * 30)
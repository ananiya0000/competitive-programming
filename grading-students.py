#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code 
    gradesfinal=[]
    for i in grades:
        if(i<38):
            gradesfinal.append(i)
        else:
            grade=i/5
            grade=(math.ceil(grade))*5
            gradeDifference=grade-i
            if(gradeDifference<3):
                gradesfinal.append(grade)
            else:
                gradesfinal.append(i)
    return gradesfinal
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

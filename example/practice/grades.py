# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:18:53 2021
@author: rbilo
short little python program that calculates your CSc110 grades
"""

grades_percentage = [0.45, 0.35, 0.05, 0.1, 0.05]
grades_name = ["exams", "regular PA's", "small PA's", "video quizzes", "prep problems"]

index = 0
final = 0
for i in range(len(grades_name)):
    input_grade = float(input("enter your % grade for " + grades_name[index] + ": "))
    temp = input_grade * grades_percentage[index]
    final += temp
    index += 1
    
    
final = format(final, '0.3f')
print("\nYour final grade is:", final + "%")





"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MAX_SCORE = 100
MIN_SCORE = 0

score = float(input("Enter score: "))
while score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
    score = float(input("Enter score again: "))

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")
# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 1: Debugging
# Due Date: 25 Oct 2020
# Matt Ryan is the quarterback for the Atlanta Falcons. The following statistics are from their first win of the
# season versus the Minnesota Vikings. Matt Ryan was named NFC Offensive Player of the Week with a Passer Rating
# of 136.6
# 85% of the grade for this assignment will be determined by finding and correcting the 2 syntax and 1 runtime errors.
# The other 15% will be from finding and correcting the 1 semantic error.

passCompletions = 30
passAttempts = 40
passYards = 371
passTouchdowns = 4
passInterceptions = 0

print("Matt Ryan had a completion percentage of", passCompletions/passAttempts*100, "%")
print("Matt Ryan averaged", passYards/passCompletions, "yards per completion")

a = (passCompletions/passAttempts - 0.3) * 5
b = (passYards/passAttempts - 3) * 0.25
c = (passTouchdowns/passAttempts) * 20              # Had to change from 10 to 20
d = 2.375 - (passInterceptions/passAttempts * 25)
passerRating = (a + b + c + d) / 6 * 100

print("Matt Ryan had a passer rating of", passerRating)



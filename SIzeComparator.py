from random import randint
from fractions import Fraction

objectDict = {}
objectDict["The Effiel Tower"] = 324
objectDict["The Sphnix"] = 20
objectDict["The Leaning Tower of Pisa"] = 56
objectDict["The Great Wall Of China"] = 21000
objectDict["The Colossaeum"] = 48
objectDict["The Statue of Liberty"] = 93
objectDict["Stonehenge"] = 4
objectDict["The Burj Khalifa"] = 828
objectDict["The Terracotta Army"] = 189
objectDict["The Moai"] = 10
objectDict["The Taj Mahal"] = 73
objectDict["Mount Everest"] = 8848
objectDict["The Petronas Twin Towers"] = 452
objectDict["The Angel of the North"] = 20
objectDict["The Christ the Redeemer statue"] = 30
objectDict["The Empire State Building"] = 443


measurement = int(input("Please input a measurement in meters :"))

indextoIntroduce = randint(0,9)
objectToIntroduce = list(objectDict)[indextoIntroduce]
isBigger = False
difference = Fraction(measurement, objectDict[objectToIntroduce])


if objectDict[objectToIntroduce] < measurement:
    isBigger = True

#if objectDict[objectToIntroduce] < measurement:
#    difference = Fraction(measurement, objectDict[objectToIntroduce])
#else:
#    isBigger = True
#    difference = Fraction(objectDict[objectToIntroduce], measurement )


print("The measurement you have entered is", measurement, "meters.")
print("{} meters is {} meters{}than {}".format(measurement, difference, " longer " if isBigger else " shorter ", objectToIntroduce))
print("{} is {} meters".format(objectToIntroduce, objectDict[objectToIntroduce]))
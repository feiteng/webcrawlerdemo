import checkDuplicates_moss
import sys

try:
    input = sys.argv
    arg1 = int(input[1])
    arg2 = int(input[2])
    arg3 = input[3]
    checkDuplicates_moss.contest_duplicate(arg1, arg2, arg3)
except:
    print('Incorrect Input.. %s' % input)


import fetchContest
import sys

try:
    input = sys.argv
    arg1 = int(input[1])
    arg2 = int(input[2])
    fetchContest.fetchContestPage(arg1, arg2)
except:
    print('Incorrect Input.. %s' % input)

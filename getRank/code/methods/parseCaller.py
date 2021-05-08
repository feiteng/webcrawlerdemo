import os
import fetchContest_Code
import fetchContest_JSON
import JPLAG
import sys


contest = 236
pages = 500

dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(dir)


# print("contest = %d .. pages = %d" % (contest, pages))

try:
	input = sys.argv
	contest = int(input[1])
	pages = int(input[2])

	print("contest = %d .. pages = %d" % (contest, pages))

	fetchContest_JSON.fetchContestPage(contest, pages, CNRegion= False, biweeklyContest = False)
	print('Finished fetching JSON..')
	fetchContest_Code.parseJSON(contest)
	print('Finished fetching submission..')
	questionList = []
	# ContestSubmission = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/'
	ContestSubmission = dir + '/Contest submission/'
	contestPath = ContestSubmission + '/' + str(contest) + '/cpp'

	for folder in os.scandir(contestPath):
		questionList.append(folder.name)

	JPLAG.jplag(contest)
	print('Finished JPLAG..')

	# updateScriptFile = 'C:/Users/lifeiteng/projects/visualizer/getRank/code/update_indexMD.py'
	updateScriptFile = dir + '/code/update_indexMD.py'
	exec(open(updateScriptFile).read())


except Exception as err:
	print(err)

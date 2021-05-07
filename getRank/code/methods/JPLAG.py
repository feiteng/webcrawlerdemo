import os

Contest_SubmissionFolder = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/'

def jplag(contest):
    try:
        str_contest = str(contest)
        contest_submission_folder = Contest_SubmissionFolder + str_contest
        questionList = []
        for folder in os.scandir(contest_submission_folder + '/cpp'):
            questionList.append(folder.name)

        # questionList = [str(q) for q in questionList]
        languageList = ['java', 'cpp', 'python3']
        languageRef = ['java19', 'c/c++', 'python3']

        changeDirectory = 'cd C:/Users/lifeiteng/projects/visualizer/getRank && '

        command1 = 'java -jar jplag-2.12.1-SNAPSHOT-jar-with-dependencies.jar -l '
        resultFolder = ' -r ./JPLAGResult/' + str_contest + '/'
        sourceFolder = ' -s "Contest submission/'

        for question in questionList:
            for i in range(0, 3):
                eachCommand = command1 + languageRef[i] + resultFolder + languageList[i] + 'Result/' + question + sourceFolder + str_contest + '/' + languageList[i] + '/' + question + '"'
                # print(changeDirectory + eachCommand)
                os.system(changeDirectory + eachCommand)
    except Exception as err:
        print("err msg... %s" % err)
        pass


# contestNames = []
# for folder in os.scandir(Contest_SubmissionFolder):
#     # path = os.path.abspath(folder) + '/'
#     # print(path)
#     if folder.is_dir() and folder.name != '.git':
#         contestNames.append(folder.name)

# for c in contestNames:
#     jplag(c)
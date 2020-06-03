import os


def jplag(contest, questionList):
    str_contest = str(contest)
    questionList = [str(q) for q in questionList]
    languageList = ['java', 'cpp', 'python']
    languageRef = ['java19', 'c/c++', 'python3']

    changeDirectory = 'cd C:/Users/lifeiteng/projects/visualizer/getRank && '

    command1 = 'java -jar jplag-2.12.1-SNAPSHOT-jar-with-dependencies.jar -l '
    resultFolder = ' -r ./JPLAGResult/' + contest + '/'
    sourceFolder = ' -s "Contest submission/'

    for question in questionList:
        for i in range(0, 3):
            eachCommand = command1 + languageRef[i] + resultFolder + languageList[i] + 'Result/' + question + \
                          sourceFolder + str_contest + '/' + languageList[i] + '/' + question + '"'
            # print(changeDirectory + eachCommand)
            os.system(changeDirectory + eachCommand)

jplag('191', [1574,1575,1576,1577])
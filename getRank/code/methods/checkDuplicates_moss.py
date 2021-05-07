# check duplicate files within same folder

import os
import mosspy


def contest_duplicate(contest, QuestionList):
    folder = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/' + str(contest) + '/'

    # coding_languages = ['python3', 'cpp', 'java']
    coding_languages = ['python3']
    # coding_languages = ['csharp','golang','javascript','python','rust','scala']
    # QuestionList = [1549,1550]
    userid = 65431

    for coding_language in coding_languages:
        folderPath = folder + coding_language
        if not os.path.exists(folderPath):
            continue
        for question in QuestionList:
            languageFolder = folder + coding_language + '/' + str(question)
            files = os.listdir(languageFolder)
            numberOfFiles = len(files)
            m = mosspy.Moss(userid, coding_language)
            print('Number of %s files = ... %d ' % (coding_language, numberOfFiles))
            for i in range(numberOfFiles):
                try:
                    file1name = files[i]
                    file1Location = languageFolder + '/' + file1name
                    m.addFile(file1Location)
                except Exception as err:
                    print(err)
                    pass
            print("now sending to moss...")
            url = m.send()
            print ("Report Url: " + url)

contest_duplicate('191', [1577])
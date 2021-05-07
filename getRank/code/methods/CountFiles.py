import os

def contestFileCount(contest):
    folder = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/' + str(contest) + '/'

    data = {}
    language = {}
    question = {}
    submissionDetails = {}
    namedict = {}
    for codingLanguage in os.listdir(folder):
        try:
            languageFolder = folder + codingLanguage + '/'
            data[codingLanguage] = {}
            for questionNumber in os.listdir(languageFolder):
                questionFolder = languageFolder + questionNumber
                for eachSubmission in os.listdir(questionFolder):
                    fileDetail = eachSubmission.split("_")
                    rank = int(fileDetail[0])
                    name = fileDetail[1].split(".")[0]
                    namedict[rank] = name
                    if rank not in submissionDetails: submissionDetails[rank] = {}
                    submissionDetails[rank][questionNumber] = codingLanguage
                count = len(os.listdir(questionFolder))
                data[codingLanguage][questionNumber] = count
                if codingLanguage not in language: language[codingLanguage] = 0
                if questionNumber not in question: question[questionNumber] = 0
                language[codingLanguage] += count
                question[questionNumber] += count
        except Exception as err:
            print(err)
            pass


    print(language)
    print(question)
    print("\t\t", end = '')
    for q in question:
        print("%s\t" % str(q), end = '')
    print()
    for codingLanguage in data:
        print("%s\t\t" % codingLanguage, end = '')
        for question in data[codingLanguage]:
            print("%d\t" % data[codingLanguage][question], end = '')
        print()


    # for rank in sorted(submissionDetails.keys()):
    #     print("%s\t%s\t" % (rank, namedict[rank]), end='')
    #
    #     for language in submissionDetails[rank].keys():
    #         print("%s\t" % submissionDetails[rank][language], end = '')
    #     print()


contestFileCount('CN-191')
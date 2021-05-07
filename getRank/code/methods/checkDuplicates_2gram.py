# check duplicate files within same folder
# use 2-gram method

import os

def ngram(string1):
    # string1.replace(" ", "")
    # print(string1)
    size = len(string1)
    gramSet = set()
    for i in range(size - 1):
        gramSet.add(string1[i:i+2])
    return  gramSet

def calculateSimilarity(string1, string2):
    set1 = ngram(string1)
    set2 = ngram(string2)
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    prob = 0.0
    try:
        prob = 1.0 * len(intersection) / len(union)
    except:
        prob = 0.0
    return prob



def contest_duplicate(contest):
    folder = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/' + str(contest) + '/'

    coding_languages = ['python3', 'cpp', 'java']
    QuestionList = [1562, 1563]#, 1545]
    userid = 1532

    for coding_language in coding_languages:
        for question in QuestionList:
            languageFolder = folder + coding_language + '/' + str(question)
            files = os.listdir(languageFolder)
            numberOfFiles = len(files)
            for i in range(numberOfFiles):
                file1name = files[i]
                file1Location = languageFolder + '/' + file1name
                file1Rows = open(file1Location, 'r')
                file1Content = ''.join([line for line in file1Rows])
                maxSimilarity = 0
                mostSimilarAccount = ""
                for j in range(i + 1, numberOfFiles):
                    file2name = files[j]
                    file2Location = languageFolder + '/' + file2name
                    file2Rows = open(file2Location, 'r')
                    file2Content = ""
                    file2Content = ''.join([line for line in file2Rows])
                    similarity = calculateSimilarity(file1Content, file2Content)
                    if similarity > maxSimilarity:
                        maxSimilarity = similarity
                        mostSimilarAccount = file2name
                if maxSimilarity > 0.9:
                    print("language = %s question = %s %s\t%s\t%f" % (coding_language, question, file1name, mostSimilarAccount, maxSimilarity))


contest_duplicate('CN-191')
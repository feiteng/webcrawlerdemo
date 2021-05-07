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

file1 = "template1"
file2 = "template2"

maxSimilarity = 0

file1Rows = open(file1, 'r')
file1Content = ''.join([line for line in file1Rows])


file2Rows = open(file2, 'r')
file2Content = ''.join([line for line in file2Rows])

similarity = calculateSimilarity(file1Content, file2Content)
print("%f" % (maxSimilarity))
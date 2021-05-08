import os
import requests
import json


# for each contest
# loop through each page, will get this json
# {
# time: 1587875867.2136621,
# is_past: true,
# submissions: [],
# questions: [],
# total_rank: [],
# user_num: 11684
# }



def fetchContestPage(contest, page = 500, CNRegion = False, biweeklyContest = False):

    urlOne = "https://leetcode.com/contest/api/ranking/warm-up-contest/?pagination=%d"
    urlOld = "https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-%s/?pagination=%d"
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%s/?pagination=%d"
    CNurl = "https://leetcode-cn.com/contest/api/ranking/weekly-contest-%s/?pagination=%d&region=local"
    url62 = "https://leetcode.com/contest/api/ranking/weekly-contest-by-app-academy/?pagination=%d"
    biweeklyURL = 'https://leetcode.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d'
    CNBiweeklyURL = 'https://leetcode-cn.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d&region=local'

    if contest == '16A' or contest == '16B' or contest == '18A' or contest == '18B': url = urlOld
    elif contest == 1: url = urlOne
    elif contest == 62: url = url62
    elif contest <= 57: url = urlOld

    if biweeklyContest: url = biweeklyURL
    if CNRegion: url = CNurl
    if CNRegion and biweeklyContest: url = CNBiweeklyURL
    data = {}
    # curl rank
    start, end = 1, page

    submissionURL = "https://leetcode.com/api/submissions/%d"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

    codingSuffix = {"cpp":"cpp",
                    "java":"java",
                    "python3":"py",
                    "python":"py",
                    "csharp":"cs",
                    "javascript":"js",
                    "golang":"go",
                    "rust":"rs"
    }

    print("processing... %s CNRegion = %s BiweeklyContest = %s" % (str(contest), CNRegion, biweeklyContest ))
    contestName = str(contest)
    if biweeklyContest: contestName = 'biweekly-' + contestName
    if CNRegion: contestName = 'CN-' + contestName
    # outputLocation = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest JSON/' + contestName + '/'
    dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    outputLocation = dir + '/Contest JSON/' + contestName + '/'
    user_num = 0

    for i in range(start, end + 1):

        if(i % 10 == 0): print('on page %d' % i)
        if contest == 1 or contest == 62: curURL = url % i
        else: curURL = url % (str(contest), i)

        try:
            # if file exists pass
            if not os.path.exists(outputLocation):
                os.makedirs(outputLocation)
            outputFile = outputLocation + str(i) + '.json'
            if os.path.exists(outputFile): continue            

            r = requests.get(curURL)
            str_response = r.json()
            user_num = str_response['user_num']

            if i > user_num / 25 + 1: break
            if(len(str_response) < 1): break

            
            
            with open(outputFile, 'a') as outputFile_:
                json.dump(str_response, outputFile_)
        except Exception as err:
            print(err)
            pass
    return True


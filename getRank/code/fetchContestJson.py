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



def fetchContestPage(contest, page, CNRegion = False, biweeklyContest = False):

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
    outputLocation = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest JSON/' + contestName + '/'
    # genUserLocation = 'C:/Users/lifeiteng/projects/visualizer/getRank/User Information/'

    for i in range(start, end + 1):

        if contest == 1 or contest == 62: curURL = url % i
        else: curURL = url % (str(contest), i)

        try:
            r = requests.get(curURL)
            str_response = r.json()
            if(len(str_response) < 1): break

            if not os.path.exists(outputLocation):
                os.makedirs(outputLocation)
            outputFileLocation = outputLocation + str(i) + '.json'
            with open(outputFileLocation, 'a') as outputFile:
                json.dump(str_response, outputFile)
            #
            # submissions = str_response['submissions']
            # total_rank = str_response['total_rank']
            #
            # N = len(total_rank)
            # print("processing page.. %d .. responses = %d" % (i, N))
            #
            # for user in range(N):
            #
            #     line = total_rank[user]
            #
            #     submission = submissions[user]
            #     data_region = line['data_region']
            #     username = line['username']
            #     userrank = line['rank']
            #
            #     for k in submission:
            #         kth_submission = submission[k]
            #         submission_id = kth_submission['submission_id']
            #         submissionRequestURL = submissionURL
            #         if data_region == 'CN':
            #             submissionRequestURL = submissionURLCN
            #         submissionRequestURL = submissionRequestURL % submission_id
            #         submissionResponse = requests.get(submissionRequestURL)
            #         submissionResponse = submissionResponse.json()
            #         coding_content =  submissionResponse['code']
            #         coding_language = submissionResponse['lang']
            #         fileLocation = outputLocation + coding_language + '/' + str(k)
            #         if not os.path.exists(fileLocation):
            #             os.makedirs(fileLocation)
            #
            #         # save as contest - code language - [username][code content]
            #         filename = fileLocation + '/' + str(userrank) + '_' + username + '.' + codingSuffix[coding_language]
            #         file = open(filename, 'w')
            #         file.write(coding_content)
            #         file.close()
        except Exception as err:
            print(err)
            pass

fetchContestPage(191, 4, CNRegion= False, biweeklyContest = False)
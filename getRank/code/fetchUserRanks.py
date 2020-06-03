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



def fetchContestPage_user(contest, page):

    urlOne = "https://leetcode.com/contest/api/ranking/warm-up-contest/?pagination=%d"
    urlOld = "https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-%s/?pagination=%d"
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%s/?pagination=%d"
    url62 = "https://leetcode.com/contest/api/ranking/weekly-contest-by-app-academy/?pagination=%d"

    if contest == '16A' or contest == '16B' or contest == '18A' or contest == '18B': url = urlOld
    elif contest == 1: url = urlOne
    elif contest == 62: url = url62
    elif contest <= 57: url = urlOld

    data = {}
    # curl rank
    start, end = 1, page

    submissionURL = "https://leetcode.com/api/submissions/%d"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

    print("processing... %s " % str(contest))
    outputLocation = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/' + str(contest) + '/'
    genUserLocation = 'C:/Users/lifeiteng/projects/visualizer/getRank/User Information/'

    for i in range(start, end + 1):
        print('processing page.. %d' % i)
        if contest == 1 or contest == 62: curURL = url % i
        else: curURL = url % (str(contest), i)

        try:
            r = requests.get(curURL)
            str_response = r.json()
            if(len(str_response) < 1): break

            submissions = str_response['submissions']
            total_rank = str_response['total_rank']

            N = len(total_rank)

            for user in range(N):

                line = total_rank[user]

                submission = submissions[user]
                data_region = line['data_region']
                username = line['username']
                userrank = line['rank']
                userFile = genUserLocation + username + '.json'
                userData = {}
                # reads and dumps user ranking
                try:
                    with open(userFile, 'r') as file:
                        userData = json.load(file)
                except:
                    pass
                userData[contest] = userrank
                with open(userFile, 'w') as file:
                    json.dump({int(x) : userData[x] for x in userData.keys()}, file, sort_keys = True)

        except Exception as err:
            print(err)
            pass

# for i in range(1, 188):
#     fetchContestPage_user(i, 10)
fetchContestPage_user(187, 5)
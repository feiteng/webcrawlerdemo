import requests
import subprocess
import json
import argparse

# Get user's rank of contest.
# Can also get user's score and finish time if needed

def fetchRanking(contest,page):

    """
    # Get kwargs
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", help="contest id")
    parser.add_argument("page", help="rank total page")
    kwargs = parser.parse_args()
    contest = int(kwargs.contest)
    page = int(kwargs.page)
    """
    urlOne = "https://leetcode.com/contest/api/ranking/warm-up-contest/?pagination=%d"
    urlOld = "https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-%s/?pagination=%d"
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%s/?pagination=%d"
    url62 = "https://leetcode.com/contest/api/weekly-contest-by-app-academy/?pagination=%d"
    if contest == '16A' or contest == '16B' or contest == '18A' or contest == '18B': url = urlOld
    elif contest == 1: url = urlOne
    elif contest <= 57: url = urlOld
    elif contest == 62: url = url62



    data = {}
    # curl rank
    start, end = 1, page
    contestantCount = 0
    print("processing... %s " % str(contest))
    for i in range(start, end + 1):
        if contest == 1 or contest == 62: curURL = url % i
        else: curURL = url % (str(contest), i)

        try:
            r = requests.get(curURL)
            str_response = r.json()
            if(len(str_response) < 1): break
            total_rank = str_response['total_rank']
            # print(total_rank)
            if (len(total_rank) < 1): break
            contestantCount += len(total_rank)
            submissions = str_response['submissions']
            N = len(total_rank)
            for i in range(N):
                line = total_rank[i]
                submission = submissions[i]
                username = line['username']
                # print(username)
                rank = line['rank']
                score = line['score']
                # if(score == 0): break
                data[username] = [rank, score, len(submission)]
        except:
            # print(curURL)
            pass
    return data

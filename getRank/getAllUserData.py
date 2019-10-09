import json
import os
import argparse
from FetchRanks import fetchRanking
# from pprint import pprint


userfile = 'user.json'
rankfile = 'percentile.json'
contestFile = 'contest.json'

if os.path.isfile(userfile):
    with open(userfile, 'r') as f:
        json_str = json.load(f)
        userData = json.loads(json_str)
else: userData = {}

# if os.path.isfile(rankfile):
#     with open(rankfile, 'r') as f:
#         json_str = json.load(f)
#         percentileData = json.loads(json_str)
# else:
percentileData = {}
contestCountData = {}
numberofQuestionsData = {}


def update(contest):
    results = fetchRanking(contest, 500)
    count = {}
    totalCandidate = len(results)
    next = 0
    nextRatio = 0.00
    step = totalCandidate / 100
    maxscore = -1
    if str(contest) not in percentileData:
        percentileData[str(contest)] = {}
        numberofQuestionsData[str(contest)] = {}
    for key in results:
        if maxscore < 0: maxscore = results[key][1]
        if key not in userData: userData[key] = {}
        userData[key][str(contest)] = results[key][0]
        questions = results[key][2]
        if questions not in count: count[questions] = 0
        count[questions] += 1
        # ratio = count / totalCandidate

        # if next == count:
        #     formatedratio = "{0:.2f}".format(1.0 - nextRatio)
        #     # print(formatedratio)
        #     if nextRatio <= 1.00:
        #         percentileData[str(contest)][formatedratio] = results[key][2]
        #     next = (int)(next + step)
        #     nextRatio += 0.01
        # count += 1
    for k in count:
        percentileData[str(contest)][k] = count[k]
    contestCountData[contest] = totalCandidate

for contest in range(1, 158):
    if contest == 16:
        update('16A')
        update('16B')
    elif contest == 18:
        update('18A')
        update('18B')
    else: update(contest)



userDataJson = json.dumps(userData)
percentileDataJson = json.dumps(percentileData)
numberofQuestionsDataJson = json.dumps(numberofQuestionsData)
contestCountDataJson = json.dumps(contestCountData)

with open(userfile, 'w') as f:
    json.dump(userDataJson, f)
with open(rankfile, 'w') as f:
    json.dump(percentileDataJson, f)
with open(contestFile, 'w') as f:
    json.dump(contestCountDataJson, f)



import time
import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import argparse
from FetchRanks import fetchRanking

# from pprint import pprint


contestFile = 'contest.json'
rankfile = 'percentile.json'
userFile = 'user.json'

with open(contestFile, 'r') as f:
    json_str = json.load(f)
    contestData = json.loads(json_str)

with open(userFile, 'r') as f:
    json_str = json.load(f)
    userData = json.loads(json_str)    

with open(rankfile, 'r') as f:
    json_str = json.load(f)
    rankData = json.loads(json_str)

# maxi = 0
# for test in contestData:
#     maxi = max(maxi, contestData[test])


# print(user)



colors = ['#6c757d', '#28a745', '#17a2b8', '#ffc107', '#dc3545', '#007bff']
numberofContest = len(contestData)

map = {}
for contest in rankData:
    for rank in rankData[contest]:
        if rank not in map: map[rank] = []
        # print(rankData[contest][rank])
        map[rank].append(rankData[contest][rank])

num = len(map['0'])
y_offset = [0] * num # for x in range(0, num)]
index = [x for x in range(1, num + 1)]


start = 1
for rowv in range(start, 7):
    row = str(rowv)
    if row not in map: continue
    while len(map[row]) < num: map[row].insert(0, 0)
    plt.bar(index, map[row], 1, y_offset, color = colors[rowv])
    # print(pp1)
    # print(type(pp1))
    y_offset = [y_offset[i] + map[row][i] for i in range(len(y_offset))]


username = 'CatherineZz'
user = userData[username]
userx = [str(i) for i in range(1, num + 4)]
usery = [0] * (num + 3)

for contest in user:
    userrank =  user[contest]
    # userx.append(contest)
    contestval = (int)(contest)
    usery[contestval] = y_offset[contestval] - userrank
    # print(contest)
    # print(userrank)

contestList = [i for i in range(1, num + 3)]
# contestList.append(['16A', '16B', '17','18A','18B'])
# contestList.append([str(i) for i in range(19, num)])

prev = 0
for i in range(2, num + 3):
    if usery[i] == 0: usery[i] = usery[i - 1]
    # prev = usery[i]

plt.step(userx, usery, where = 'post')

plt.ylabel("Number of Participants")
plt.xlabel("Leetcode Contest")
plt.xticks([x for x in range(0, num, 10)])
legend = (username, 'Solved 1', 'Solved 2', 'Solved 3', 'Solved 4')
if start == 0: legend = (username, 'Solved 0', 'Solved 1', 'Solved 2', 'Solved 3', 'Solved 4')
plt.legend(legend)
plt.show()


#
#
#
#
#
# def getColor(val):
#     # val2d = "{0:.2f}".format(val)
#     # val = (float)(val2d)
#     # colors = plt.cm.BuPu(np.linspace(0, 0.01, 1))
#     # return  colors[val]
#     # red = (int) (255 * val)
#     red = (int) (225 * (1 - val))
#     return '#%02X%02X%02X' % (red, 255, 255) #green, red // 10 + 100)
#
# map = {}
# color = {}
# xaxis = [x for x in range(1, 155)]
# # xaxis = [90, 91]
# for contest in percentData:
#     # print(contest)
#     # xaxis.append(contest)
#     for percentile in percentData[contest]:
#         if percentile not in map: map[percentile] = []
#         if percentile not in color: color[percentile] = []
#         val = percentData[contest][percentile]
#
#         map[percentile].append(val * 100)
#         color[percentile].append(getColor(val))
#
#
# for percentile in np.arange(1.0, 0.1, -0.1):
#     p = "{0:.2f}".format(percentile)
#     plt.bar(xaxis, map[p], color = color[p])
#
# plt.xlabel("Leetcode Contests")
# # plt.yticks([x * 100 for x in np.arange(0.1, 1.1, 0.1)])
#

#
# plt.show()

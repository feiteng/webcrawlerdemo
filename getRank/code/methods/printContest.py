
import time
import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import argparse
from FetchRanks import fetchRanking
from FindUser import findUserName

# from pprint import pprint

def printContest(username, start = 1):

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
    # index = [x for x in range(1, num + 1)]



    contestList = [str(i) for i in range(1, 16)]
    tmplist = ['16A', '16B', '17','18A','18B']
    for i in tmplist: contestList.append(i)
    for i in range(19, num - 1): contestList.append(str(i))
    # print(contestList)
    # print(len(contestList))
    xaxis = [i for i in range(num)]
    # print(xaxis)

    for rowv in range(start, 7):
        row = str(rowv)
        if row not in map: continue
        while len(map[row]) < num: map[row].insert(0, 0)
        # print(len(xaxis))
        # print(len(map[row]))
        plt.bar(xaxis, map[row], 1, y_offset, color = colors[rowv])
        # print(pp1)
        # print(type(pp1))
        y_offset = [y_offset[i] + map[row][i] for i in range(len(y_offset))]


    # username = 'Lynn'
    if username not in userData:
        users = findUserName(username)
        username = users[0]
        print(users)
        for name in users:
            print(userData[name])
    try:
        user = userData[username]
        # userx = [str(i) for i in range(1, num + 4)]
        userDict = {}

        for contest in user:
            userrank =  user[contest]
            userDict[contest] = userrank
        # print(userDict)
        usery = [] # * len(contestList)
        prev = 0
        count = 0


        for i in contestList:
            if i not in userDict: usery.append(prev)
            else: usery.append(max(0,y_offset[count] - userDict[i]))
            prev = usery[-1]
            count += 1
            # print(i)
            # print(userDict[i])


        plt.step(xaxis, usery, where = 'mid', color = 'k')
        legend = (username, 'Solved 1', 'Solved 2', 'Solved 3', 'Solved 4')
        if start == 0: legend = (username, 'Solved 0', 'Solved 1', 'Solved 2', 'Solved 3', 'Solved 4')
    except Exception as err:
        print(err)
        legend = ('Solved 1', 'Solved 2', 'Solved 3', 'Solved 4')
        if start == 0: legend = ('Solved 0', 'Solved 1', 'Solved 2', 'Solved 3', 'Solved 4')
        pass
    plt.ylabel("Number of Participants")
    plt.xlabel("Leetcode Contest")
    plt.xticks([x for x in range(0, num, 10)])
    plt.legend(legend)
    # plt.savefig( 'c:/users/lifeiteng/project/visualizer/getRanks/img/' + username + '_contest')
    figure = plt.gcf() # get current figure
    figure.set_size_inches(19.2, 10.8)
    plt.savefig('./img/' + username + '_contest', )
    plt.close()

printContest('obihai')
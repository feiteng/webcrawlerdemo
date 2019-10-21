
import time
import datetime
import collections
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import json
import os
import argparse
from FetchRanks import fetchRanking
from FindUser import findUserName
from printPercentile import printPercentile
from printContest import printContest
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

maxi = 0
freq = {}
for username in userData:
    # print(username)
    # print(userData[username])
    freq[username] = len(userData[username])
    if(freq[username] > 100):
        printContest(username, 0)
        print('done..' + username)
        # print(username)
    maxi = max(maxi, freq[username])


# print(maxi)
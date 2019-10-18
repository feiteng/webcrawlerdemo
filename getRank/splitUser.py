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


contestFile = 'contest.json'
rankfile = 'percentile.json'
userFile = 'user.json'

with open(userFile, 'r') as f:
    json_str = json.load(f)
    userData = json.loads(json_str)

count = 0
tcount = 0
size = len(userData)
names = {}

for username in userData:
    names[username] = userData[username]
    count += 1
    if count == 11000:
        usernamesJson = json.dumps(names)
        filname = 'usersplit_' + str(tcount) + '.json'
        with open(filname, 'w') as f:
            json.dump(usernamesJson, f)
        count = 0
        tcount += 1
        names = {}

usernamesJson = json.dumps(names)
filname = 'usersplit_' + str(tcount) + '.json'
with open(filname, 'w') as f:
    json.dump(usernamesJson, f)
count = 0
tcount += 1

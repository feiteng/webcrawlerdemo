import matplotlib.pyplot as plt
import numpy as np
import json

userFile = 'user.json'

with open(userFile, 'r') as f:
    json_str = json.load(f)
    userData = json.loads(json_str)

def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(m): dp[i + 1][0] = i + 1
    for j in range(n): dp[0][j + 1] = j + 1
    for i in range(m):
        for j in range(n):
            # print("" + str(i) + "_" + str(j))
            if s1[i] == s2[j]: dp[i + 1][j + 1] = dp[i][j]
            else: dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j + 1])

    return dp[m][n]

def findUserName(username):
    # edit distance
    len = 100
    re = []
    for str_name in userData:
    # for str_name in ['daruba', 'aruba1']:
    #     print(str_name)
        d = editDistance(username, str_name)
        # print(d)
        # print(str_name)
        if d == len:
            re.append(str_name)
        if d < len:
            len = d;
            re = []
            re.append(str_name)
            # print(d)
            # print(str_name)
    return re

# print(findUserName('aruba'))
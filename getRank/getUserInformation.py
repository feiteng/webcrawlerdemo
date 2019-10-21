from bs4 import BeautifulSoup
import time
import requests
import subprocess
import json
import re
import argparse


def getSubmission(username):
    url = "https://leetcode.com/" + username
    r = requests.get(url)
    # print(r.status_code)
    count = 0
    waittime = 1

    while r.status_code != 200:
        if waittime > 30: break
        if(r.status_code == 429):
            time.sleep(waittime) #'Too many requets..' + username)
            waittime <<= 1
        if(r.status_code == 404):
            print('Incorrect Information..' + username)
            return  ''
    if waittime > 30: return ''
    return r.text
#     # print(username)
#     text = r.text
#     soup = BeautifulSoup(text, 'html.parser')
#     information = soup.find_all(class_='badge progress-bar-success')
#     # print(len(information))
#     # print(information)
#     # print()
#     data = []
#     # try:
#     for info in information:
#         info = str(info)
#         # print(info)
#         trimmed = re.sub(r"<.*>", "", info)
#         trimmed = re.sub(' ', '', trimmed)
#         trimmed = re.sub('\n', '', trimmed)
#         data.append(trimmed)
#         # print(trimmed)
#     # print(data)
#     try:
#         res = data[2]
#         if len(data) >= 8: res = data[4]
#         # print('user = %s, submission = %s' % (username, res))
#         return res
#     except:
#         print('Cannot Get' + username)
#         time.sleep(5)
#         pass
#
#
# 	# infoList = []
# 	# for info in information:
# 	# 	print(info)
# 	# 	print()
# 	# 	infoList.append(info)
# 	# for into in infoList:
# 	# 	print(info)
# 	# 	print()
#
# 	# print(len(infoList))
# 	# response = r.json()
#
# 	# print(response)
#
#
# # getSubmission('qjjjjjj')
# # getSubmission('Reidddddd')
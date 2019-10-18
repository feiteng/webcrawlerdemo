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
    if r.status_code == 404:
        print('incorrect name..' + username)
        return []
    while r.status_code != 200:
        print('retrying..' + username)
        time.sleep(5)
        r = requests.get(url)
    # print(username)
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    information = soup.find_all(class_='badge progress-bar-success')
    # print(len(information))
    # print(information)
    # print()
    data = []
    # try:
    for info in information:
        info = str(info)
        # print(info)
        trimmed = re.sub(r"<.*>", "", info)
        trimmed = re.sub(' ', '', trimmed)
        trimmed = re.sub('\n', '', trimmed)
        data.append(trimmed)
        # print(trimmed)
    # print(data)
    try:
        res = data[2]
        if len(data) >= 8: res = data[4]
        # print('user = %s, submission = %s' % (username, res))
        return res
    except:
        print('Cannot Get' + username)
        time.sleep(5)
        pass
	

	# infoList = []
	# for info in information: 
	# 	print(info)
	# 	print()
	# 	infoList.append(info)
	# for into in infoList:
	# 	print(info)
	# 	print()

	# print(len(infoList))
	# response = r.json()
	
	# print(response)


getSubmission('qjjjjjj')
# getSubmission('Reidddddd')
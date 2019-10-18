import time
import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import argparse
from FetchRanks import fetchRanking
from getUserSubmissions import getSubmission

# from pprint import pprint


contestFile = 'contest.json'
rankfile = 'percentile.json'
userFile = 'user.json'
userSubmissionFile = 'userSubmission.json'

with open(userFile, 'r') as f:
    json_str = json.load(f)
    userData = json.loads(json_str)    

print(len(userData))

submit = {}
count = 0
for username in userData:
	detail = getSubmission(username)
	submit[username] = detail #[success, total]
	count += 1
	# if count % 100 == 0: print(count)
	print(str(count) + '_' + username)
	# time.sleep(.1)



userSubmitJson = json.dumps(submit)

with open(userSubmissionFile, 'w') as f:
    json.dump(userSubmitJson, f)

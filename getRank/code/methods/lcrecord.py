import urllib
from bs4 import BeautifulSoup
import urllib.request
import collections
import csv
import os
import random
import time 


def getRecentSubmissionbyLCId(username, q):
    url = "https://leetcode.com/" + username + "/"
    print("Getting submission: " + username) 
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    headers = {'User-Agent': user_agent, }

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html, features="lxml")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = list(filter(None, chunks))

    index = text.index("Most recent submissions")
    submissions = text[index + 1:index + 81]


    result = set()
    it = iter(submissions)
    for status, lan, title, time in zip(it, it, it, it):
        if status == "Accepted" and title in q:
            result.add(title)

    return result


def readResultsFromFile(filename):
    if os.path.exists(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    user = row[0]
                    print(user)
                    for col in range(2, len(row)):
                        if row[col] == 'True':
                            ans[user].add(questions[col])
 
def readContest2(filename):
    if os.path.exists(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    user = row[0]
                    contest2res[user] = int(row[1])
                    line_count += 1


def readContest1(filename):
    if os.path.exists(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    user = row[0]
                    contest1res[user] =int(row[1])
                    line_count += 1


def writeResultToFile(filename):
    cnt = 0
    for name in username.keys():
        cnt += 1
        if cnt %10 == 0:
            time.sleep(65)
        ans[username[name]] |= (getRecentSubmissionbyLCId(name, q))
    import csv
    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)
        writer.writerow(["Name"] + ["Completed #"] + q)
        writer.writerow([" ", " "] + ["Q" + str(x) for x in range(1, len(q) + 1)])  

        #all_guess = set()
        for name, done in ans.items():
            i = 0
            qq = q[::]
            random.shuffle(qq)
            guess = qq[i%len(qq)]
            # while guess not in done or guess in all_guess:
            #     i += 1
            #     guess = qq[i%len(qq)]
            #     if i == 10:
            #         guess = qq[0]
            #         break
            # all_guess.add(guess)
            completed_number = 0
            completed_number += contest1res.get(name, 0)
            completed_number += contest2res.get(name, 0)
            completed_number += len(done)
            writer.writerow([name] + [str(completed_number)] + [do in done for do in q])


def getUsernameandId():
# I have deleted all others username, but you can add more for testing purpose
    username = {
            
				"xianglaniunan":"Little Lee"
				
                }


    return username
def getQuestionList(filename):
    q = []
    if os.path.exists(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                q.append(row[0])
            return q


q = getQuestionList("q.txt")
print(q)
filename = "weeklyResults.csv"
contest1filename = "rescontest1.csv"
contest2filename = "rescontest2.csv"
ans = collections.defaultdict(set)
contest1res = {}
contest2res = {}

questions = {}
for index, question in enumerate(q):
    questions[index + 2] = question
username = getUsernameandId()
  
readResultsFromFile(filename)

readContest1(contest1filename)

writeResultToFile(filename)

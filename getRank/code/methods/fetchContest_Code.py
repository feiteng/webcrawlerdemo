import os
import requests
import json


# for each contest
# loop through each page, will get this json
# {
# time: 1587875867.2136621,
# is_past: true,
# submissions: [],
# questions: [],
# total_rank: [],
# user_num: 11684
# }

def parseJSON(contest):

    codingSuffix = {"cpp":"cpp",
                    "java":"java",
                    "python3":"py",
                    "python":"py",
                    "csharp":"cs",
                    "javascript":"js",
                    "golang":"go",
                    "rust":"rs"
    }


    contestName = str(contest)
    dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    submissionURL = "https://leetcode.com/api/submissions/%d"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

    print("processing... %s " % contestName)

    # JSON_Location = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest JSON/' + contestName + '/'
    JSON_Location = dir + '/Contest JSON/' + contestName + '/'
    outputLocation = dir + '/Contest Submission/' + contestName + '/'
    processedJSON = outputLocation + 'processed.JSON'
    processedID = {}
    try:
        with open(processedJSON) as file:
            processedID = json.load(file)
    except Exception as err:
        print(err)
        pass
    for i in range(1, 42):
        try:
            JSONFile = JSON_Location + str(i) + '.JSON'
            str_response = {}
            with open(JSONFile) as file:
                str_response = json.load(file)
        except Exception as err:
            print(err)
            break

        submissions = str_response['submissions']
        total_rank = str_response['total_rank']

        N = len(total_rank)
        for user in range(N):

            line = total_rank[user]

            submission = submissions[user]
            data_region = line['data_region']
            username = line['username']
            userrank = line['rank']
            for k in submission:
                print("Processing page.. %d user.. %d submission.. %s"  % (i, user, k))
                try:
                    uniqueID = str(userrank) +  '_' + username + '_' + str(k)
                    if uniqueID in processedID: continue
                    processedID[uniqueID] = 1
                    kth_submission = submission[k]
                    submission_id = kth_submission['submission_id']
                    submissionRequestURL = submissionURL
                    if data_region == 'CN':
                        submissionRequestURL = submissionURLCN
                    submissionRequestURL = submissionRequestURL % submission_id
                    submissionResponse = requests.get(submissionRequestURL)
                    submissionResponse = submissionResponse.json()
                    coding_content =  submissionResponse['code']
                    coding_language = submissionResponse['lang']
                    fileLocation = outputLocation + coding_language + '/' + str(k)
                    if not os.path.exists(fileLocation):
                        os.makedirs(fileLocation)

                    # save as contest - code language - [username][code content]
                    filename = fileLocation + '/' + str(userrank) + '_' + username + '.' + codingSuffix[coding_language]
                    if os.path.exists(filename): continue
                    file = open(filename, 'w', encoding='utf-8')
                    file.write(coding_content)
                    file.close()
                except Exception as err:
                    print(err)
                    break
            with open(processedJSON, 'w') as outputFile:
                json.dump(processedID, outputFile)


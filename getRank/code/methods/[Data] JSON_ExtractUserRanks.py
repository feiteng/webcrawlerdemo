import os, json, collections

contest_JSON_folder = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest JSON'
user_data_folder = 'C:/Users/lifeiteng/projects/visualizer/getRank/user data'
userFile = user_data_folder + '/user.json'

user_Dict = collections.defaultdict(dict)
# with open(userFile) as json_file:
#     user_Dict = json.load(json_file)
# pp = pprint.PrettyPrinter(indent=4)
#
for folder in os.scandir(contest_JSON_folder) :
    folderName = folder.name
    contest = folderName
    print('now on %s contest..' % contest)
    folderDir = contest_JSON_folder + '/' + folderName
    for JSONFile in os.scandir(folderDir):
        try:
            fileDir = folderDir + '/' + JSONFile.name
            submission_data = {}
            with open(fileDir, 'r') as j:
                submission_data = json.load(j)
            total_rank = submission_data['total_rank']
            for line in total_rank:
                # line = total_rank[item]
                user_name = line['username']
                # user_slug = line['user_slug']
                user_rank = line['rank']
                # user_slug_Dict[user_name] = user_slug
                user_Dict[user_name][contest] = user_rank
        except Exception as err:
            print(err)
            pass

with open(userFile, 'w') as outputFile:
    json.dump(user_Dict, outputFile)
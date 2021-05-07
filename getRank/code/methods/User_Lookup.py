import mysql.connector, json, csv

userFile = 'C:/Users/lifeiteng/projects/visualizer/getRank/user data/user.json'


with open(userFile) as json_file:
    user_data = json.load(json_file)



# text = []

        # text.append(row)

user_name = '66brother'

for contest in user_data[user_name]:
    rank = user_data[user_name][contest]
    print('%s %s %d' % (user_name, contest, rank))

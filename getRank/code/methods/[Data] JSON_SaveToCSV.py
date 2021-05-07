import mysql.connector, json, csv

userFile = 'C:/Users/lifeiteng/projects/visualizer/getRank/user data/user.json'


with open(userFile) as json_file:
    user_data = json.load(json_file)

# text = []

        # text.append(row)

userFileCSV = 'C:/Users/lifeiteng/projects/visualizer/getRank/user data/user.csv'

idx = 1
with open(userFileCSV, 'w', newline = '', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for user_name in user_data:
        for contest in user_data[user_name]:
            rank = user_data[user_name][contest]
            # print('%s %d %d' % (user_name, contest, rank))
            writer.writerow([idx, user_name, contest, rank])
            idx += 1

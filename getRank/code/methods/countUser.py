import mysql.connector, json

userFile = 'C:/Users/lifeiteng/projects/visualizer/getRank/user data/user.json'
sql = "INSERT INTO usertable (username, contest, ranking) VALUES (%s, %s, %s)"

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='leetcodeuser',
#                                          user='root',
#                                          password='1234')
#
with open(userFile) as json_file:
    user_data = json.load(json_file)
print(len(user_data))
#     for user_name in user_data:
#         for contest in user_data[user_name]:
#             rank = user_data[user_name][contest]
#             val = (user_name, contest, rank)
#
#             cursor = connection.cursor()
#             try:
#                 cursor.execute(sql, val)
#                 connection.commit()
#                 # print(cursor.rowcount)
#             except Exception as err:
#                 print(err)
#
# except Exception as err:
#     print(err)

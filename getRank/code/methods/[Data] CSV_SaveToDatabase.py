import mysql.connector, json

userFile = 'C:/Users/lifeiteng/projects/visualizer/getRank/user data/user.json'
sql = "INSERT INTO table2 (username, properties) VALUES (%s, %s)"

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='leetcodeuser',
                                         user='root',
                                         password='1234')

    with open(userFile) as json_file:
        user_data = json.load(json_file)
    for user_name in user_data:
        print('running user.. %s' % user_name)
        j = json.dumps(user_data[user_name])
        val = (user_name, j)
        # for contest in user_data[user_name]:
        #     rank = user_data[user_name][contest]
        #     val = (user_name, contest, rank)

        cursor = connection.cursor()
        try:
            cursor.execute(sql, val)
            connection.commit()
            # print(cursor.rowcount)
        except Exception as err:
            print(err)

except Exception as err:
    print(err)

import requests
import browser_cookie3

# cj = browser_cookie3.chrome()
# print(type(cj))

postCookie = {
    'csrftoken' : 'pGi9tTUAP6iqZEqf0u5Lx2TM9tbyhrkL5MOnyLoFWzOsoYornVmXMRGFEQxPZDER',
    'leetcode_session' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI0NTUyNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjEwODNiMDYxMzE0MjBkNzFlZWM3NzA5OTYxN2QwNDkxYzEzZjFmYjYiLCJpZCI6MTI0NTUyNSwiZW1haWwiOiJuaW1pbmcxMjAxQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiQ2hlYXRlckJ1c3RlciIsInVzZXJfc2x1ZyI6ImNoZWF0ZXJidXN0ZXIiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvY2hlYXRlcmJ1c3Rlci9hdmF0YXJfMTU4ODcyODY1NC5wbmciLCJyZWZyZXNoZWRfYXQiOjE1OTg1NTA0ODIsImlwIjoiMTAwLjM1LjIxNS4yMyIsImlkZW50aXR5IjoiZWYzMDRiODAzNGVjNGFlM2I0NDlmZjNhYWFlMDQ5ZjYiLCJzZXNzaW9uX2lkIjoxMDk0NjgsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0._lIOkpno_kvFxjYWb-kyJz9gdr7iUYR_bPbsv1lP6_U'
}
# for cookie in cj:
#     if cookie.domain == 'leetcode.com' and cookie.name == 'csrftoken':
#         # print(cookie.domain)
#         csrftoken = cookie.value

print('### csfr token = ' + str(csrftoken))

code = '\t\treturn [0]'
submitPayLoad = {
    #  'csrfmiddlewaretoken': csrftoken,
    # 'lang': "python3",
    # 'question_id': "1",
    # 'typed_code': 'class Solution:    def twoSum(self, nums: List[int], target: int) -> List[int]:\n' + code

    "question_id":"1",
     "lang":"python3",
     "typed_code":"class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        " + code
}

headers = { 'origin' : 'https://leetcode.com',
            'referer':  'https://leetcode.com/problems/two-sum/submissions/',
        }
submitURL = 'https://leetcode.com/problems/two-sum/submit/'
post = requests.post(submitURL, headers = headers, data = submitPayLoad, cookies = postCookie)
print(post.status_code)
print(post.text)


# payload = {
#     'csrfmiddlewaretoken': csrftoken,
#     'login': 'niming1200@gmail.com',
#     'password': '123456',
#     'recaptcha_token' : '03AGdBq27xRZu9pPrZxgEedb_QcSwJN5W_6GgfJSRIYx2ee91BzOh9IRjleN6FK1DdbWmjdDRpkDgBA6Hd52PU0NRMQsnwM_uMoSAyyeZ4wgDfQ_qF4Fx4sJDZCwyYOTTpLknhpwKSKNqGPs3eHgwN0PvCkqAf8v-NZz1SDbUi4qPUWTvCj_ztmnkSndA9vUxRsWhV3BiRuap4mNwqyX2g2UZolJMUs7wy30u94VXngeWPp4ZtSYX3D56nMcL42SDgvuwxMJBY1Asby2Dj7jPQfqmDjOkqy_WL1ZTIlmWdLErAi-lr9ruG0q07s5OqSlYA9NJHFrTffftW_uwpoLZlorwuH48_tq6M_UEhnC4t5rON1rwr8Sd62pOo-gtwxsUyBLiuzXGRcI5CanuUL8u3-kQF4pLrnWUN1Q'
# }
#
# loginURL = 'https://leetcode.com/accounts/login/'
#
# headers = { 'origin' : 'https://leetcode.com',
#             'referer':  loginURL,
#             'Cookie' : 'csrftoken=' + str(csrftoken) + ';'
#         }
#
# p = requests.post(loginURL, headers = headers, data=payload)
# print(p.status_code)
# print(p.text)
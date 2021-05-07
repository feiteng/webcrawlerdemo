import requests
import browser_cookie3

# cj = browser_cookie3.chrome()
# print(type(cj))

csrf_token = 'pGi9tTUAP6iqZEqf0u5Lx2TM9tbyhrkL5MOnyLoFWzOsoYornVmXMRGFEQxPZDER'
postCookie = {
    'csrftoken' : csrf_token,
    'LEETCODE_SESSION' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI0NTUyNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjEwODNiMDYxMzE0MjBkNzFlZWM3NzA5OTYxN2QwNDkxYzEzZjFmYjYiLCJpZCI6MTI0NTUyNSwiZW1haWwiOiJuaW1pbmcxMjAxQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiQ2hlYXRlckJ1c3RlciIsInVzZXJfc2x1ZyI6ImNoZWF0ZXJidXN0ZXIiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvY2hlYXRlcmJ1c3Rlci9hdmF0YXJfMTU4ODcyODY1NC5wbmciLCJyZWZyZXNoZWRfYXQiOjE1OTg1NTA0ODIsImlwIjoiMTAwLjM1LjIxNS4yMyIsImlkZW50aXR5IjoiZWYzMDRiODAzNGVjNGFlM2I0NDlmZjNhYWFlMDQ5ZjYiLCJzZXNzaW9uX2lkIjoxMDk0NjgsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0._lIOkpno_kvFxjYWb-kyJz9gdr7iUYR_bPbsv1lP6_U'
}

# for cookie in cj:
#     if cookie.domain == 'leetcode.com' and cookie.name == 'csrftoken':
#         # print(cookie.domain)
#         csrftoken = cookie.value



code = '\t\treturn [0]'
submitPayLoad = {
     'csrfmiddlewaretoken': csrf_token,
     "question_id":"1",
     "lang":"python3",
     "typed_code":"class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n" + code
}

headers = { 'origin' : 'https://leetcode.com',
            'referer':  'https://leetcode.com/problems/two-sum/submissions/',
        }
submitURL = 'https://leetcode.com/problems/two-sum/submit/'

session = requests.session()
post = session.post(submitURL, headers = headers, data = submitPayLoad, cookies = postCookie)

print(post.status_code)
print(post.text)
import requests
import browser_cookie3

leetcode_cookies = browser_cookie3.chrome(domain_name='leetcode.com')
cookieDict = {}
for cookie in leetcode_cookies:
    cookieDict[cookie.name] = cookie.value

url = 'https://leetcode.com/problems/two-sum/submit/'
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer' : 'https://leetcode.com/'}
submitPayLoad = {
     'csrfmiddlewaretoken': cookieDict['csrftoken'],
     "question_id":"1",
     "lang":"python3",
     "typed_code":"class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n" #+ code
}

with requests.Session() as session:
    page = session.get(url)
    p = session.post(url, data = submitPayLoad, cookies = cookieDict, headers = HEADERS)
    print(p)
    print(p.status_code)
    print(p.text)
    # pageCookies = page.cookies._cookies
    # for key in pageCookies:
    #     print(key)
    #     pageCookies2 = pageCookies[key]
    #     for key2 in pageCookies2:
    #         print(key2)
    #         print(pageCookies2[key2])
    #     print("....")

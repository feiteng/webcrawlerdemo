import requests
import browser_cookie3


payload = {
    'login': 'li.feiteng@gmail.com',
    'password': '1234',
}

loginURL = 'https://leetcode.com/accounts/login/'
tokenURL= 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdBpsIUAAAAAKAYWjZfIpn4cJHVIk_tsmxpl7cz&co=aHR0cHM6Ly9sZWV0Y29kZS5jb206NDQz&hl=en&v=QVh-Tz10ahidjrORgXOS1oB0&size=invisible&cb=r63cbbcljthd'
recaptchaURL = 'https://www.google.com/recaptcha/api2/reload?k=6LdBpsIUAAAAAKAYWjZfIpn4cJHVIk_tsmxpl7cz'


headers = { 'origin' : 'https://leetcode.com',
            'referer':  tokenURL # loginURL
        }
s = requests.session()
p = s.post(recaptchaURL,
           data =
           {}
           )
print(p)
print(p.status_code)
print(p.text)
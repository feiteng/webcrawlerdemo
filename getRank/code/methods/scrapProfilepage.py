import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'C:/Users/lifeiteng/projects/lcRecord/chromedriver.exe'

def getRecentSubmissionbyLCId(username, q):

    url = "https://leetcode.com/" + username + "/"
    print("Getting submission: " + username)

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(url)

    accumulated_wait_time = 0
    found = False
    result = set()
    while not found and accumulated_wait_time < 30:
        try:
            class_name = 'css-9ykukq'
            testItem = driver.find_element_by_class_name(class_name)
            search = driver.find_elements_by_class_name(class_name)
            found = True
            break
        except Exception as err:
            STEP = 2
            time.sleep(STEP)
            accumulated_wait_time += STEP
            pass

    if not found:
        print("Waited too long for username... %s" % username)
    else:
        # print('Total wait time.. %d' % accumulated_wait_time)
        for submission in search:
            submission_info = submission.text
            split = submission_info.splitlines()
            title = split[0]
            status = split[3]

            if status == "Accepted" and title in q:
                result.add(title)

    return result



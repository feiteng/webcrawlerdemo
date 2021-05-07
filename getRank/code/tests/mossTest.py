import mosspy


userid = 12345

coding_language = 'java'

m = mosspy.Moss(userid, coding_language)

file1 = "template1"
file2 = "template2"
m.addFile(file1)
m.addFile(file2)
url = m.send()
print ("Report Url: " + url)
m.saveWebPage(url, "submission/report.html")


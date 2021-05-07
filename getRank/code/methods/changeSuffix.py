import os

Contest_SubmissionFolder = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest submission/'

codingSuffix = {"cpp":"cpp",
                    "java":"java",
                    "python3":"py",
                    "python":"py",
                    "csharp":"cs",
                    "javascript":"js",
                    "golang":"go",
                    "rust":"rs"
}

for folder in os.scandir(Contest_SubmissionFolder):
    contestFolder = Contest_SubmissionFolder + folder.name
    for codingLanguageFolder in os.scandir(contestFolder):
        if not codingLanguageFolder.is_dir(): continue
        codingLanguage = codingLanguageFolder.name
        folder = contestFolder + '/' + codingLanguage
        for eachFolder in os.scandir(folder):
            submissionFolder = folder + '/' + eachFolder.name
            for fileFolder in os.scandir(submissionFolder):
                try:
                    fileName = fileFolder.name
                    if fileName.endswith(codingSuffix[codingLanguage]): continue
                    file = submissionFolder + '/' + fileName
                    newFileName = submissionFolder + '/' + fileName + '.' + codingSuffix[codingLanguage]
                    filecontent = ''
                    with open(file) as f:
                        filecontent = f.read()
                    with open(newFileName, 'w') as f:
                        f.write(filecontent)
                        f.close()
                    os.remove(file)
                except Exception as err:
                    print(err)
                    pass
    print('finished folder ... %s' % folder)

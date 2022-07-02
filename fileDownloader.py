from traceback import print_tb
import requests
import os
import json

contents = "{}"

# parentDir = "D:/MCA_STUDY_MATERIAL/Amdocs_Learning/Spring Framework/"
parentDir = "D:/MCA_STUDY_MATERIAL/Amdocs_Learning/"

workingDir = parentDir
fileParentDir = ""

with open("course download links.json", 'r') as file:
    contents = file.read()

urlsData = json.loads(contents)

# getting the first key
for topDir in urlsData.keys():
    # print(topDir)
    topDirPath = os.path.join(parentDir, topDir)
    if(not os.path.isdir(topDirPath)):
        os.mkdir(topDirPath)
        print(f"{topDirPath} is created")
    
    print(f"Using {topDirPath}")
    workingDir = topDirPath

    for childContents in urlsData[topDir].items():
        
        childContentsPath = os.path.join(topDirPath, childContents[0])
        if not os.path.isdir(childContentsPath):
            os.mkdir(childContentsPath)
            print(f"Created '{childContentsPath}' directory")
        for contents in childContents[1].items():
            fileName = f"{contents[0]}.mp4"
            if contents[1] != "":
                finalPath = os.path.join(childContentsPath, fileName)
                if os.path.isfile(finalPath):
                    print(f"Skipping \"{fileName}\" (file already exist)")
                    continue
                
                print(f"Downloading \"{fileName}\" Into \"{finalPath}\"")
                data = requests.get(contents[1])
                
                with open(finalPath, 'wb') as video:
                    video.write(data.content)
                print(f"Downloaded \"{fileName}\" Into \"{finalPath}\"")



"""
with open("course download links.txt", 'r') as file:
    contents = file.readlines()

# print (contents)    

videoParentDir = ""
isCommented = False
for line in contents:
    if isCommented:
        if(line.strip() == "--" or line.strip().startswith("--")):
            print("ending commented section")
            isCommented = False
            continue
        
        print("escaping comment section")
        continue
    if(line.strip() == "--" or line.strip().startswith("--")):
        print("commented section")
        isCommented = True


    if line.startswith('>'):
        dirName = line.replace('>', '')
        dirName = dirName.strip()
        path = os.path.join(parentDir, dirName)
        videoParentDir = path
        # try:
        #     os.mkdir(path)
        # except FileExistsError as e:
        #     print('')

    if line.startswith('{'):
        if videoParentDir == "":
            pass
        else :
            videoParentDir = videoParentDir + "/"
        videoFileName = line.replace("{", '').strip()
        # videoFileName = "{"+videoFileName+"}"
       
        videoList = videoFileName.split("<")
        
        filename = f"{videoList[0]}.mp4"
        print(filename)
        # data = requests.get(videoList[1])
        # finalPath = os.path.join(videoParentDir, filename)
        # print(finalPath)
        # with open(finalPath, 'wb') as video:
        #     video.write(data.content)

"""
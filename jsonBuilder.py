import json
import re
from bs4 import BeautifulSoup 

def union(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3



with open("techademyHtml.html", encoding='utf8') as fp: 
    soup = BeautifulSoup(fp, 'html.parser') 
# elem = soup.findAll('span', {'class': 'MuiTypography-root MuiCardHeader-subheader jss1144 MuiTypography-body2 MuiTypography-colorTextSecondary MuiTypography-displayBlock'})
elem = soup.findAll('div', {'class':'mat-tooltip-trigger ng-star-inserted title'})
title = soup.findAll('div', {'class':'title'})

allTitles = []
mainTitle = []
subTitles = []

for element in title:
    inner_text = element.text
    name = inner_text.replace("\n", "");
    allTitles.append(name)

for element in elem:
    inner_text = element.text
    name = inner_text.replace("\n", "");
    subTitles.append(name)

mainTitle = union(allTitles, subTitles)


finalJson = {}
key = ""
subDict = dict()
for title in allTitles:
    res = re.sub(r'[^\w\s]', '-', title)
    res = res.strip()

    if res in mainTitle:
        if res in finalJson:
            subDict[res] = ""
            continue

        finalJson[key] = subDict.copy()
        subDict = dict()
        key = res
        finalJson[key] = {}
        continue

    subDict[res] = ""

print(finalJson)

json_object = json.dumps(finalJson, indent = 4) 

with open("D:/MCA_STUDY_MATERIAL/Amdocs_Learning/courseDownloadJson.json", 'w') as f:
    f.write(json_object) 
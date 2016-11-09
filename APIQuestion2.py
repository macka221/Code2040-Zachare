#TODO: Add Comments
import requests as request
import json


tokenVal = "d2f2bccb39ae22ad239c31197251640f"
needle = ""
haystack = []

haystackURL = "http://challenge.code2040.org/api/haystack"
validateURL = "http://challenge.code2040.org/api/haystack/validate"
inDict = {"token":tokenVal, "needle":needle, "haystack":haystack}

def getData():
    inAPI = request.post(haystackURL, json=inDict)
    tempStr = str(inAPI.content)

    tempStr = tempStr[2:-1]
    newDict = json.loads(tempStr)
    return newDict
    
def findNeedle(dict1):
    DictValues = newDict["haystack"]
    sentinal = True
    j = 0
    while sentinal:
        if DictValues[j] == newDict['needle']:
            sentinal = False
        j+=1
        
    outDict = {"token":tokenVal, "needle":j - 1}
    outAPI = request.post(validateURL, json=outDict)
    return outAPI.content


dict1 = getData()
print(findNeedle(dict1))

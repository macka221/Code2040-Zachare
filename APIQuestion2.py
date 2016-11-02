#TODO: Add Comments and structurize
import requests as request
import json


tokenVal = "d2f2bccb39ae22ad239c31197251640f"
needle = ""
haystack = []
haystackURL = "http://challenge.code2040.org/api/haystack"
validateURL = "http://challenge.code2040.org/api/haystack/validate"
inDict = {"token":tokenVal, "needle":needle, "haystack":haystack}

inAPI = request.post(haystackURL, json=inDict)
tempStr = str(inAPI.content)

tempStr = tempStr[2:-1]
newDict = json.loads(tempStr)
DictValues = newDict["haystack"]
sentinal = True
j = 0


while sentinal:
    if DictValues[j] == newDict['needle']:
        sentinal = False
    j+=1

outDict = {"token":tokenVal, "needle":j - 1}
outAPI = request.post(validateURL, json=outDict)
print(outAPI.content)

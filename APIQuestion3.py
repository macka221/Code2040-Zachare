#TODO: Add Comments
import requests as request
from json import loads as load


tokenVal = "d2f2bccb39ae22ad239c31197251640f"
prefixURL = "http://challenge.code2040.org/api/prefix"
validateURL = "http://challenge.code2040.org/api/prefix/validate"
prefix = ""
array = []
inDict = {"token":tokenVal, "prefix":prefix, "array":array}

def recieveAPI():
    inAPI = request.post(prefixURL, json=inDict)

    tempStr = str(inAPI.content)
    tempStr = tempStr[2:-1]
    newDict = load(tempStr)
    DictArray = newDict['array']
    newPrefix = newDict['prefix']
    return newPrefix

def matchPrefix(newPrefix):
    newArray = []
    prefixSize = len(newPrefix)
    sentinal = True

    for i in DictArray:
        if i[:prefixSize] != newPrefix:
            newArray.append(i)
            
        outDict = {'token':tokenVal, 'array':newArray}
        outAPI = request.post(validateURL, json=outDict)
    return outAPI.content

data = recieveAPI()
print(matchPrefix(data))

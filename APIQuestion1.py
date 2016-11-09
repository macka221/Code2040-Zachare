#TODO: Add Comments and structurize
import requests as request

endpoint = "http://challenge.code2040.org/api/reverse"
validateUrl = "http://challenge.code2040.org/api/reverse/validate"
tokenVal = "d2f2bccb39ae22ad239c31197251640f"
stringVal = ""

def gatherString():
    recieve_string = {"token": tokenVal, "string":""}

    inAPI = request.post(endpoint, json=recieve_string)
    temp = str(inAPI.content)
    stop = len(temp) - 1
    testAPI = temp[2:stop]
    return testAPI

def reverseString(string)
    i = 1
    while i <= len(string):
        stringVal = stringVal + string[-i]
        i += 1

    outString = {"token": tokenVal, "string":stringVal}
    outAPI = request.post(validateUrl, json=outString)
    return outAPI.content

data = gatherString()
print(reverseString(data))

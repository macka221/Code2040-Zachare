#TODO: Add Comments and structurize
import requests as request

endpoint = "http://challenge.code2040.org/api/reverse"
validateUrl = "http://challenge.code2040.org/api/reverse/validate"
tokenVal = "d2f2bccb39ae22ad239c31197251640f"
stringVal = ""

recieve_string = {"token": tokenVal, "string":""}

inAPI = request.post(endpoint, json=recieve_string)
temp = str(inAPI.content)
stop = len(temp) - 1
testAPI = temp[2:stop]

i = 1
while i <= len(testAPI):
    stringVal = stringVal + testAPI[-i]
    i += 1

outString = {"token": tokenVal, "string":stringVal}
outAPI = request.post(validateUrl, json=outString)

print(outAPI.content)
input()

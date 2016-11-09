#TODO: Add Comments
from json import loads as load
import requests as request
import datetime
import dateutil.parser as parser


tokenVal = "d2f2bccb39ae22ad239c31197251640f"
datestampURL = "http://challenge.code2040.org/api/dating"
validateURL = "http://challenge.code2040.org/api/dating/validate"
datestamp = ''
interval = ''

def recieveDict():
  inDict = {'token':tokenVal, 'datestamp':datestamp, 'interval':interval}

  inAPI = request.post(datestampURL, json=inDict)
  tempStr = str(inAPI.content)
  tempStr = tempStr[2:-1]
  return tempStr

def addTime(tempStr):
  newDict = load(tempStr)
  tempDate = newDict['datestamp']
  date = parser.parse(tempDate)
  seconds = datetime.timedelta(seconds=newDict['interval'])
  newTempDate = date + seconds
  newDate = newTempDate.isoformat()
  Date = newDate[:-6]
  Date = Date + tempDate[-1]

  outDict = {'token':tokenVal, 'datestamp':Date}
  outAPI = request.post(validateURL, json=outDict)
  return outAPI.content

data = recieveDict()
print(addTime(data))

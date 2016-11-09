#TODO: Add Comments and Structurize the code
import requests as request

tokenVal = "d2f2bccb39ae22ad239c31197251640f"
githubVal = "https://github.com/macka221/Code2040-Zachare"
def requestAPI():
  body = {"token":tokenVal, "github":githubVal}
  url ="http://challenge.code2040.org/api/register"
  API = request.post(url,json=body)
  return API.content

print(requestAPI())

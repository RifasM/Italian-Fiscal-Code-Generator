from re import findall
import httplib2
import json, os
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

try:
    os.remove("credentials.storage")
except:
    pass

CLIENT_SECRET = 'client_secrets.json'
SCOPE = 'https://www.googleapis.com/auth/userinfo.profile'
STORAGE = Storage('credentials.storage')

# Start the OAuth flow to retrieve credentials
def authorize_credentials():
# Fetch credentials from storage
    credentials = STORAGE.get()
# If the credentials doesn't exist in the storage location then run the flow
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
        http = httplib2.Http()
        credentials = run_flow(flow, STORAGE, http=http)
    return credentials
credentials = authorize_credentials()

"""with open("credentials.storage", "r") as j:
    jd = json.dumps(json.load(j))
    name = findall("\"name\":\s\"(.*)\",\s\"picture\"", jd)
    picture = findall("\"picture\":\s\"(.*)\",\s\"given_name\"", jd)
    print(str(name)[2:-2])
    print(str(picture)[2:-2])"""
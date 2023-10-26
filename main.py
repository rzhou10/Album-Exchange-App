from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import json

# Initializing a GoogleAuth Object 
gauth = GoogleAuth()

# client_secrets.json file is verified 
# and it automatically handles authentication 
gauth.LocalWebserverAuth()

# GoogleDrive Instance is created using 
# authenticated GoogleAuth instance 
drive = GoogleDrive(gauth)

# Initialize GoogleDriveFile instance with file id
with open('configs.json') as f:
    file_id = json.load(f)

file_obj = drive.CreateFile({'id': file_id["sheet_id"]})
file_obj.GetContentFile('FILE_NAME.xls', 
		mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

dataframe = pd.read_excel('FILE_NAME.xls')
# Send to results.json
responses_to_json = dataframe.to_json(orient='records')

responses_to_json_dict = json.loads(responses_to_json)

with open('results.json', 'w') as json_file:
    json.dump(responses_to_json_dict, json_file)
print(responses_to_json_dict)

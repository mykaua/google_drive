#!/bin/env python

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload
import os
from datetime import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'
PATH_TO_FILE = '/Users/slevincalebra/Documents/Epam.kdbx'
FOLDER_ID = '1evXMGO5Az8SO2Thy2H3guVHU-CvQ0Dbn' # google drive folder id

def main():
    #credentials
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
#    results = service.files().list(
#        pageSize=100, fields="nextPageToken, files(id, name)").execute()
#    items = results.get('files', [])


#    if not items:
#        print('No files found.')
#    else:
#        print('Files:')
#        for item in items:
#            print(u'{0} ({1})'.format(item['name'], item['id']))

 # Upload file to google Drive
    folder_id = FOLDER_ID
    file_metadata = {'name': 'password.kdbx', 'parents': [folder_id]}
    media = MediaFileUpload(PATH_TO_FILE , mimetype='application/octet-stream', resumable=True)
    upload_file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
#    print ('File ID: %s' % upload_file.get('id'))

# OS X notification
    date = datetime.now().time()
    notify_text = ' Password has been updloaded to google drive ' + str(date)
    notify_title = 'Password uploaded'
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(notify_text, notify_title))
# delete files older than 3 month
#    delete_file = service.files().delete(fileId='1wPiyX49j0nKn7ysHD9JZBMZ4FiVlcazg').execute()

if __name__ == '__main__':
    main()

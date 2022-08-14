#!/usr/bin/env python3

import os
#import requests
import httplib2
import argparse
from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage
from datetime import datetime
from pprint import pprint

SCOPES = 'https://www.googleapis.com/auth/tasks.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Tasks test script'

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

def get_credentials():
    ''''''
    this_dir = os.path.dirname(os.path.abspath(__file__))
    credential_dir = os.path.join(this_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'tasks-readonly.json')
    

# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:49:28 2024

@author: Udit
"""

import os.path

import pygsheets
from google.auth.environment_vars import CREDENTIALS
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import Constants
from Constants import constant


class GoogleSheet:
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    sheet = ""

    def __init__(self, sheet_id, sheet_name):
        self.worksheet = None
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        creds = None
        # The file token.json stores the user's access and refresh tokens,
        # and is created automatically when the authorization flow completes
        # for the first time.
        if os.path.exists(constant.TOKEN):
            creds = Credentials.from_authorized_user_file(
                constant.TOKEN, constant.SCOPES
            )
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS, constant.SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(constant.TOKEN, "w") as token:
                token.write(creds.to_json())
        self.creds = creds
        self.open_sheet_using_pygsheets()
        self.open_worksheet()

    def open_sheet_using_google_client(self):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            # Call the Sheets API
            self.sheet = (
                service.spreadsheets()
                .values()
                .get(spreadsheetId=self.sheet_id, range=f"{self.sheet_name}")
                .execute()
            )

        except HttpError as err:
            print(err)

    def open_sheet_using_pygsheets(self):
        try:
            self.sheet = pygsheets.authorize(
                client_secret=constant.CREDENTIALS
            ).open_by_key(constant.SPREADSHEET_ID)

        except HttpError as err:
            print(err)

    def open_worksheet(self):
        self.worksheet = self.sheet.worksheet_by_title(self.sheet_name)
        print(self.worksheet.title)
        print(self.worksheet.rows)
        print(self.worksheet.cols)

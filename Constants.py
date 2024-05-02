# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:02:58 2024

@author: Udit
"""

from Assets.security_codes import spreadsheet_id, scopes

ASSETS = "Assets"


class GoogleApi:
    # If modifying these scopes, delete the file token.json.
    SCOPES = scopes

    TOKEN = f"{ASSETS}/token.json"
    CREDENTIALS = f"{ASSETS}/credentials.json"

    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = spreadsheet_id
    SUMMARY_SHEET = "Summary_OSV"
    TRANSACTION_SHEET = "Transactions_OSV"
    SUMMARY_RANGE = "A1:Q1"
    TRANSACTION_RANGE = "A1:P1"


class ListedCompanies:
    NSE = f"{ASSETS}/nse_listed_companies.csv"
    NSE_CODE = "ISIN NUMBER"
    NSE_SYMBOL = "SYMBOL"

    BSE = f"{ASSETS}/BSE_list_companies.csv"
    BSE_CODE = "ISIN No"
    BSE_SYMBOL = "Security Id"

    BSE_ZERO = f"{ASSETS}/BSE_listed_companies_t0.csv"
    BSE_ZERO_CODE = "ISIN No"
    BSE_ZERO_SYMBOL = "Security Id"
    A = "A"


class Groww:
    GROWW_REPORT = f"{ASSETS}/report.xlsx"
    STOCK_NAME = "Stock name"
    REALISED_TRADES = "Realised trades"
    UNREALISED_TRADES = "Unrealised trades"
    JSON_FILE = f"{ASSETS}/transactions.json"
    MAX_TRANSACTIONS = 5000
    MAX_COMPANIES = 6000


class Constants:
    classList = [GoogleApi, ListedCompanies, Groww]

    def __init__(self):
        # Set constants from separate classes as attributes
        for cls in self.classList:
            for key, value in cls.__dict__.items():
                if not key.startswith("__"):
                    self.__dict__.update(**{key: value})

    def __setattr__(self, name, value):
        raise TypeError("Constants are immutable")


constant = Constants()

# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:06:06 2024

@author: Udit
"""
from Constants import constant
from googleapi import GoogleSheet
from groww import GrowwReport


class PortfolioManager:

    def __init__(self):
        # self.groww_report = GrowwReport()
        self.transaction_sheet = GoogleSheet(
            constant.SPREADSHEET_ID, constant.TRANSACTION_SHEET
        )
        # self.summary_sheet = GoogleSheet(
        #     constant.SPREADSHEET_ID, constant.SUMMARY_SHEET
        # )


PortfolioManager()

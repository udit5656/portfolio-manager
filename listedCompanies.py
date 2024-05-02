# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:54:19 2024

@author: Udit
"""
import csv
from openpyxl import load_workbook
from Constants import constant


def add(c, x):
    return chr(ord(c) + x)


class Exchange:
    def __init__(self, file_name, code, symbol):
        self.companies = {}
        self.code = code
        self.symbol = symbol
        self.file_name = file_name
        self.sheet = None
        self.csvFile = None

    def read_csv_file(self):
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            code_idx = None
            symbol_idx = None
            for row in csv_reader:
                company = [x.strip() for x in row]
                if code_idx is None:
                    code_idx = company.index(self.code)
                    symbol_idx = company.index(self.symbol)
                    continue
                self.companies[company[code_idx]] = company[symbol_idx]

    def get_col(self, title):
        for currCol in range(1, constant.MAX_TRANSACTION):
            cell_value = self.sheet.get(row=1, col=currCol).value
            if cell_value == title:
                return currCol
        raise Exception(f"No cell in {self.file_name} with title: {title}")

    def read_excel_file(self):
        self.sheet = load_workbook(filename=self.file_name).active
        code_col = self.get_col(self.code)
        symbol_col = self.get_col(self.symbol)
        for row in range(1, constant.MAX_COMPANIES):
            if self.sheet[f"A{row}"] is None:
                break
            curr_code = self.sheet[f"{add(constant.A, code_col)}{row}"]
            curr_symbol = self.sheet[f"{add(constant.A, symbol_col)}{row}"]
            self.companies[curr_code] = curr_symbol

    def print_companies_list(self):
        print(self.companies)


class Exchanges:
    exchanges = []

    def __init__(self):
        nse = Exchange(constant.NSE, constant.NSE_CODE, constant.NSE_SYMBOL)
        nse.read_csv_file()

        bse = Exchange(constant.BSE, constant.BSE_CODE, constant.BSE_SYMBOL)
        bse.read_csv_file()

        bse_zero = Exchange(
            constant.BSE_ZERO, constant.BSE_ZERO_CODE, constant.BSE_ZERO_SYMBOL
        )
        bse_zero.read_csv_file()

        self.exchanges.append(nse.companies)
        self.exchanges.append(bse.companies)
        self.exchanges.append(bse_zero.companies)

    # code here represents ISIN
    def find_symbol(self, code):
        for idx, companies in enumerate(self.exchanges):
            if code in companies.keys():
                return companies[code]
        raise Exception(f"Symbol not found in for {code}")

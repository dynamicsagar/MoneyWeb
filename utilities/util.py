"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import xlrd as xlrd
import utilities.custom_logger as cl
import logging

from xlutils.copy import copy


class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alpha_numeric(self, length, type='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, charCount=10):
        """
        Get a unique name
        """
        return self.get_alpha_numeric(charCount, 'lower')

    def get_unique_name_list(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Parameters:
            listSize: Number of names. Default is 5 names in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.get_unique_name(itemLength[i]))
        return nameList

    def verify_list_match(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verify_list_contains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def insert_data(self, userEmail):
        """
        Insert user email id.
        Parameters:
                :param userEmail: enter registered email id
        """
        sheet_loc = "./testdata/datasheet.xls"
        try:
            import os.path
            if os.path.isfile(sheet_loc):
                wb = xlrd.open_workbook(sheet_loc)
                sheet = wb.sheet_by_index(0)
                rowNum = sheet.nrows
                rb = xlrd.open_workbook(sheet_loc)
                wb = copy(rb)
                sheet = wb.get_sheet(0)
                sheet.write(rowNum, 0, userEmail)
                wb.save(sheet_loc)
                self.log.info("Successfully inserted all the values in the sheet")
            else:
                import xlwt as xw
                wb = xw.Workbook()
                sheet1 = wb.add_sheet('Sheet 1')
                sheet1.write(0, 0, 'User email')
                wb.save(sheet_loc)
                wb = xlrd.open_workbook(sheet_loc)
                sheet = wb.sheet_by_index(0)
                rowNum = sheet.nrows
                rb = xlrd.open_workbook(sheet_loc)
                wb = copy(rb)
                sheet = wb.get_sheet(0)
                sheet.write(rowNum, 0, userEmail)
                wb.save(sheet_loc)
                self.log.info("Successfully inserted all the values in the sheet")
        except:
            self.log.info("Unable to insert values into xls")

    def get_data(self, userName=''):
        # Give the location of the file
        loc = "./testdata/datasheet.xls"

        # To open Workbook
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        rowNum = sheet.nrows
        for i in range(rowNum):
            if userName in sheet.cell_value(i, 0):
                print(sheet.cell_value(i, 0))
                print('hello')
                return sheet.cell_value(i, 0)
        self.log.info("No value found: " + userName)

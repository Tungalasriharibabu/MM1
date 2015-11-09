import os
import sys
import string
from Selenium2Library.locators import TableElementFinder
from robot.libraries.BuiltIn import BuiltIn
import time
import csv
import xlsxwriter
import xlwt
import xlrd
from time import gmtime, strftime
import time
import datetime
import thread

class TableData:
    
          def __init__(self):
            pass   
          def table_get_column_no(self, table_locator, columnName):
            """Returns the column number of the column matching 'columnName' from the table located at 'table_locator'."""
            #try:
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            selenium.wait_until_element_is_visible(table_locator,time.sleep(10))
            colCount = int(selenium.get_matching_xpath_count(table_locator+'/div[contains(@class,"dgrid-header dgrid-header-row")]/table[contains(@id,"-header")]/tr/th'))
            print "colCount:"+str(colCount)
            for iCounter in range(1,colCount+1):
                curColName = selenium._get_text(table_locator+'//div[contains(@class,"dgrid-header dgrid-header-row")]/table[contains(@id,"-header")]/tr/th['+str(iCounter)+']')
                if (curColName.replace(' ','').strip().lower()==columnName.replace(' ','').strip().lower()):
                    print "column name matched at "+str(iCounter)
                    return iCounter
            return 0
        
      
          
          def get_columnvalues(self,table_locator,columnName,icount):
                selenium = BuiltIn().get_library_instance('Selenium2Library')
                columnNo = int(self.table_get_column_no(table_locator,columnName))
                list1=[]
                for iRow in range(4,15):
                    list2=selenium.get_text('//span[contains(text(),"Available Students")]//following::div//div//table//th[5]//following::div['+str(iRow)+']//table//td['+str(columnNo)+']')
                    list1.append(list2)
                return list1
            
          def get_cell_value(self, table_locator, columnNo, RowNo):
               selenium = BuiltIn().get_library_instance('Selenium2Library')
               cellvalue=selenium.get_text('//span[contains(text(),"Available Students")]//following::div//div//table//th[5]//following::div['+str(columnNo)+']//table//td['+str(RowNo)+']')
               print cellvalue

          def select_value_in_table(self, table_locator, columnNo, RowNo):
              selenium = BuiltIn().get_library_instance('Selenium2Library')
              selenium.click_element('//span[contains(text(),"Available Students")]//following::div//div//table//th[5]//following::div['+str(columnNo)+']//table//td['+str(RowNo)+']')

          def click_on_element(self,elementLocator,timeout="60s"):
              selenium = BuiltIn().get_library_instance('Selenium2Library')
              selenium.wait_until_page_contains_element(elementLocator,timeout)
              selenium.click_element(elementLocator)

          def verify_element_visible(self,locator):
              selenium = BuiltIn().get_library_instance('Selenium2Library')
              bStatus = selenium._is_visible(locator)
              if(str(bStatus) != str(True)) and (str(BuiltIn().get_variable_value("${BROWSER}"))!="ie"):
                selenium.capture_page_screenshot()
              return bStatus

          def wait_for_element_visible(self,locator,timeout=None,messgae=''):
                  
                    if(timeout == None):
                        timeout = "30s"
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    for iCounter in range(1,3):
                            selenium.wait_until_page_contains_element(locator,timeout)
                            selenium.wait_until_element_is_visible(locator,timeout)
                    return true
                
          def get_length_of_list(self, actuallist):
                    if len(actuallist)==0:
                        raise AssertionError('Actual is empty')
                    return len(actuallist)

          def csvfile(self,csvfilepath):
            with open(csvfilepath, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                 print ', '.join(row)
                 return ', '.join(row)
                
          def createxmlfile(self,path,sheetname):
              workbook = xlsxwriter.Workbook(path)
              worksheet = workbook.add_worksheet(sheetname)
              workbook.close()

          def copyxmldata(self,sourcepath,Designationpath):
                fname = "C:\Users\sriharibabu.t\Desktop\hari.xls"
                bk = xlrd.open_workbook(fname)
                shxrange = range(bk.nsheets)
                sh = bk.sheet_by_name("Sheet1")
                nrows = sh.nrows
                ncols = sh.ncols
                row_list = []

                workbook = xlwt.Workbook()
                sheet = workbook.add_sheet('Test')

                for i in range(0,nrows):
                    row_data = sh.row_values(i)
                    col_data=sh.col_values(i)
                    row_list.append(row_data)
                    for index, value in enumerate(row_data):
                     sheet.write(i, index, value)

                workbook.save('C:\Users\sriharibabu.t\Desktop\output.xls')

          def create_csv_file_using_ms_excel_file(self,csvfilepath,excelfilepath,sheetName=None):
            """Returns the row Data of the given text in the MS Excel file """
            workbook = xlrd.open_workbook(excelfilepath)
            snames=workbook.sheet_names()
            opFile=open(str(csvfilepath), "wb");
            writer = csv.writer(opFile)
            tList=[]
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(excelfilepath,sheetName)==False:
                return -1
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows 
            headersList=[]
            for rowno in range(0,noofrows):
                tempList=[]
                dictVar={}
                rowValues=worksheet.row_values(rowno)
                rowValues = [str(x) for x in rowValues]
                if rowno==0:
                     headersList=rowValues
                for ind in range(0,len(rowValues)):
                        val=self.get_unique_test_data(rowValues[ind])

                        tempList.append(val)
                        if rowno!=0:
                            dictVar[str(headersList[ind])]=str(val)
                         
                writer.writerow(tempList)
                if rowno!=0:
                        tList.append(dictVar)
                        print dictVar
            opFile.close()
            return tList

          def get_unique_test_data(self,testdata):
            testdata=str(testdata)
            timestamp=self.get_timestamp()
            testdata=testdata.replace("unique",timestamp)
            return testdata
        
          def get_timestamp(self):
                    uniqueNumber = strftime("%Y%m%d%H%M%S", gmtime())
                    uniqueTimeStamp=str(uniqueNumber)
                    uniqueId=uniqueTimeStamp
                    x=uniqueId[-5:]
                    uniqueIds=x
                    mmMailFormat=uniqueIds
                    return mmMailFormat
                
          def convert_to_the_dictionary(self, item):
            return dict(item)

          def validate_the_sheet_in_ms_excel_file(self,filepath,sheetName):
              workbook = xlrd.open_workbook(filepath)
              snames=workbook.sheet_names()
              sStatus=False        
              if sheetName==None:
                  return True
              else:
                  for sname in snames:
                      if sname.lower()==sheetName.lower():
                          wsname=sname
                          sStatus=True
                          break
                  if sStatus==False:
                      print "Error: The specified sheet: "+str(sheetName)+" doesn't exist in the specified file: "+str(filepath)
              return sStatus

          def get_row_values_into_list(self,path,rowNo):
                    file_Reader = csv.reader(open(path))
                    rowNumber=0
                    lines=[]
                    for row in file_Reader:
                        rowNumber=rowNumber+1
                        if rowNumber==int(rowNo):
                            lines=row
                            break

                    return lines
            
          def create_csv_file_using_ms_excel_file_uniqe(self,csvfilepath,excelfilepath,rowNumber,sheetName=None):
            workbook = xlrd.open_workbook(excelfilepath)
            snames=workbook.sheet_names()
            opFile=open(str(csvfilepath), "wb");
            writer = csv.writer(opFile)
            tList=[]
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(excelfilepath,sheetName)==False:
                  return -1
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows 
            headersList=[]
            for rowno in range(0,noofrows):
                tempList=[]
                dictVar={}
                dictvar1={}
                rowValues=worksheet.row_values(rowno)
                rowValues = [str(x) for x in rowValues]
                if rowno==0:
                     headersList=rowValues
                for ind in range(0,len(rowValues)):
                       
                        val=self.get_unique_test_data(rowValues[ind])  
                        tempList.append(val)
                        if rowno!=0:
                              dictVar[str(headersList[ind])]=str(val)
                writer.writerow(tempList)
                for ind in range(0,len(rowValues)):
                       rowValues=worksheet.row_values(int(rowNumber))  
                       val=self.get_unique_test_data(rowValues[ind])  
                       if rowno!=0:
                        dictvar1[str(headersList[ind])]=str(val)
                if rowno!=0:
                        tList.append(dictVar)
            opFile.close()
            return dictvar1

  

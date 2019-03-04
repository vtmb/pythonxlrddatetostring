#! /usr/local/bin/python3.7

import xlrd


def xlrdDateValueToStringRepresentation(myFloatdate: float, myWorkbook: xlrd.Book):
    myDate = xlrd.xldate_as_datetime(myFloatdate, myWorkbook.datemode)
    myDateString = "{0}.{1}.{2}".format(myDate.day, myDate.month, myDate.year)
    return myDateString


workbook = xlrd.open_workbook("testtabelle.xls")

sheet = workbook.sheet_by_index(0)

headers = []

values = []

for x in range(0, 4):
    headers.append(sheet.cell(1, x).value)


for x in range(0, 4):
    values.append(sheet.cell(2, x).value)


print("headers:")
print(headers)

print("values")
print(values)

birthdate = values[3]


print("my birthdate as float {0}".format(birthdate))

testdate = xlrd.xldate_as_datetime(birthdate, workbook.datemode)

print(testdate)

dateAsString = "{0}.{1}.{2}".format(
    testdate.day, testdate.month, testdate.year)

print(dateAsString)

print("testing date to string function")

stringdate = xlrdDateValueToStringRepresentation(birthdate, workbook)
print(stringdate)

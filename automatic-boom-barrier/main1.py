# # # # # with open("weather_data.csv") as data_file:
# # # # #     data = data_file.readlines()
# # # # #     print(data)
# # # #
# # # # import csv
# # # #
# # # # with open("weather_data.csv") as data_file:
# # # #     data = csv.reader(data_file)
# # # #     print(data)
# # # #     for row in data:
# # # #         print(row)
# # # ## #
# # # import csv
# # #
# # # with open("weather_data.csv") as data_file:
# # #     data = csv.reader(data_file)
# # #     temperature = []
# # #     for row in data:
# # #         print(row[1])
# #
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# # import pandas
# #
# # data = pandas.read_csv("data.csv")
# # print(data)
# # print(data["temp"])
#
#
# # Writing to an excel
# # sheet using Python
# import xlwt
# from xlwt import Workbook
#
# # Workbook is created
# wb = Workbook()
#
# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Sheet 1')
#
# sheet1.write(1, 0, 'ISBT DEHRADUN')
# sheet1.write(2, 0, 'SHASTRADHARA')
# sheet1.write(3, 0, 'CLEMEN TOWN')
# sheet1.write(4, 0, 'RAJPUR ROAD')
# sheet1.write(5, 0, 'CLOCK TOWER')
# sheet1.write(0, 1, 'ISBT DEHRADUN')
# sheet1.write(0, 2, 'SHASTRADHARA')
# sheet1.write(0, 3, 'CLEMEN TOWN')
# sheet1.write(0, 4, 'RAJPUR ROAD')
# sheet1.write(0, 5, 'CLOCK TOWER')
#
# wb.save('xlwt example.xls')
#
#
import cv2
import pytesseract
import time
import threading
import xlwt  # Import the xlwt library for Excel file writing

# ... (rest of your code)

# Create an Excel workbook and add a worksheet
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("DetectedPlates")

# Write headers to the Excel worksheet
worksheet.write(0, 0, "Timestamp")
worksheet.write(0, 1, "Plate Number")
worksheet.write(0, 2, "Event")

# ... (rest of your code)

def save_to_excel(data):
    row = worksheet.nrows  # Get the current number of rows in the worksheet
    worksheet.write(row, 0, data[0])  # Timestamp
    worksheet.write(row, 1, data[1])  # Plate Number
    worksheet.write(row, 2, data[2])  # Event
    workbook.save("detected_plates.xls")  # Save the Excel file

# ... (rest of your code)

# Inside the detect_plate function:
# Replace the save_to_csv calls with save_to_excel calls

# ... (rest of your code)

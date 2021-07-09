# import serial
import csv
import time
import pandas as pd
from random import randint
import time

# ser = serial.Serial('COM3', baudrate=19200)

x_value = 0
a = 0
b = 0
c = 0
d = 0
fieldnames = ['x_value', 'a', 'b', 'c', 'd']

with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
with open('data2.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
with open('data3.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        x_value += 1
        # getdata = str(ser.readline())
        # y = getdata[1:]
        # n1 = y.replace("\\r\\n","")
        # n2 = n1.replace("'","")
        # data = list(n2.split(','))
        # info = {
        #     "x_value": x_value,
        #     "a": data[0],
        #     "b": data[1],
        #     "c": data[2],
        #     "d": data[3],
        # }
        info = {
            "x_value": x_value,
            "a": randint(0,400),
            "b": randint(0,400),
            "c": randint(0,400),
            "d": randint(0,400)
        }
        csv_writer.writerow(info)
    with open('data2.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info2 = {
            "x_value": x_value,
            "a": randint(0,400),
            "b": randint(0,400),
            "c": randint(0,400),
            "d": randint(0,400)
        }
        csv_writer.writerow(info2)
    with open('data3.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info2 = {
            "x_value": x_value,
            "a": randint(0,400),
            "b": randint(0,400),
            "c": randint(0,400),
            "d": randint(0,400)
        }
        csv_writer.writerow(info2)
        time.sleep(4)
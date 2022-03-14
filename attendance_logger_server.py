# Title: Attendance logger
# By: Dr Basel Barakat
# Date: 11 March 2022
# Institute: University of Sunderland
# Course: CET237 Programing Virtual Networks
# All rights reserved

#importing the libraries
# socket is used for network programming
import socket
# csv is used for saving the data in spreadsheer
import csv 
# datetime is used to get the current time
import datetime

# Define the IP address and port number
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7777  # Port to listen on (non-privileged ports are > 1023)

# Define the name of the file to save the data on
filename = 'attendance.csv'

# File saving function
def file_saver(data,a_or_w):

    # convert the binary to string
    data=str(data)

    # check if this is the first run of the code 
    if a_or_w =='w':

        # Save to the file
        with open(filename, a_or_w) as file:
            file.write(data+"\n")

    else:

        #Record time
        time_in = str(datetime.datetime.now()) 
        
        #join the time and the data
        data_to_rec = time_in +','+ data

        #Save to the file
        with open(filename, a_or_w) as file:
            file.write(data_to_rec+"\n")
    


def server_with_save():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file_saver(data.decode(),'a')
                conn.sendall(data+ b' confirmed ')


file_saver('Time'+','+'Name'+','+'ID','w')

while True:
    server_with_save()
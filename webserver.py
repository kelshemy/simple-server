from fileinput import filename
from socket import *
import os
serverPort = 80
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("127.0.0.1",serverPort))
serverSocket.listen(1)
while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(4096).decode()
        split = sentence.split("\r\n")[0].split(" ")[1]; #this gets the second value in the get header
        cwd = os.getcwd() #gets the current working directory
        fileName = cwd + split 
        
        # HTTP/1.1 STATUS# OK/NOT FOUND\r\n Content-Type: text/html; charset=UTF-8\r\n\r\n
        response = "HTTP/1.1 "
        try: # send back 200 
            with open(fileName, "r") as f: 
                fileContents = f.readlines() #reads the contents within the file
                fileContents = "".join(fileContents) 
                response += "200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
                response += fileContents
                connectionSocket.send(response.encode())
        except IOError: #send back 404 
            response += "404 NOT FOUND\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html> <h1> 404 NOT FOUND</h1></html>\r\n"
            connectionSocket.send(response.encode())
        connectionSocket.close()
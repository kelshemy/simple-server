from functools import cache
from socket import *
serverPort = 8000
with socket(AF_INET,SOCK_STREAM) as serverSocket: #creates the socket
    serverSocket.bind(("127.0.0.1",serverPort)) #binds ip address to the port
    serverSocket.listen(1) #listens for requests
    cache = {} #empty list
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        split = sentence.split("\r\n")[0].split(" ")[1][1:]
        split = split.removeprefix("http://") #removes https
        split = split.removeprefix("www.") #removes www. 
        index  = split.find("/") 
        part1 = split[:index] #gets the site 
        part1 = part1.lstrip().rstrip()
        part2 = split[index:] #gets the file within the site

        if split in cache: #if it has already been stored in cache, it will get the response immediately rather than going through the server
            print("Found in cache!")
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + cache[split]
            connectionSocket.send(response.encode())
            connectionSocket.close()
        else:
            try:
                ip = gethostbyname(part1) #gets the ip address of the site
                request = "GET {} HTTP/1.0\r\n\r\n".format(part2)
                ipSocket = socket(AF_INET,SOCK_STREAM) #creates a socket for the ip address of the site
                ipSocket.connect((ip, 80)) #connects the ip of the site to port 80
                ipSocket.send(request.encode()) 
                ipResponse = ""
                while True:
                    partOfResponse = ipSocket.recv(512).decode() #it decodes every 512 bytes that are received
                    ipResponse += partOfResponse #adds the decoded part to whatever is already present
                    if len(partOfResponse) < 512: 
                        break #if less than 512 then it stops because there is no more to be decoded
                ipResponse = ipResponse.split("\r\n\r\n")[1] # part of http response that contains the file
                connectionSocket.send("HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n{}".format(ipResponse).encode())
                cache[split] = ipResponse

            except gaierror:
                print("Unable to resolve hostname {}. If favicon.ic, just ignore".format(part1))
            connectionSocket.close()
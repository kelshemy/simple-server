## Simple HTTP Server and Proxy

### Version
- Windows 11
- Python 3.10
- Brave Browser 

Brave Browser runs on Chromium so it should be able to work on other browsers that also utilize Chromium such as Google Chrome. 

### Overview
For **part 1**, I used 127.0.0.1/HelloWorld.html to view the server in the browser.

For **part 2**, I used 127.0.0.1:8000//http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html to view in the browser.

For **part A**, I ran webserver.py on 127.0.0.1 and on port 80, while for **part B**, I ran proxyserver.py on 127.0.0.1 and on port 8000. 

These were the urls I used to test webserver.py:
- 127.0.0.1/HelloWorld.html to produce a 200 OK 
- 127.0.0.1/HelloWorld1234.html to produce a 404 ERROR

These were the urls that I tested with proxyserver.py:
- 127.0.0.1:8000//http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html
- 127.0.0.1:8000//http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
- 127.0.0.1:8000//http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html
- 127.0.0.1:8000//http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html

**Note**: While testing the proxyserver.py, I went to Inspect Element and then Network and then clicked on disable cache. I did this because sometimes the cache would interfere when I am testing if a url was stored in the cache previously or not. 

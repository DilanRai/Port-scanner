import socket
import sys
import pyfiglet
from datetime import datetime

banner=pyfiglet.figlet_format("Port Scanner")
print(banner)

#target=input("please enter host to scan:")
target="localhost"# you can use ip address or domain name or localhost or hostname or google.com or any other website or server you want to scan or you can use your own ip address.
host= socket.gethostbyname(target)

file =open("port-scanner.txt", "w")# use a file to save the results(existing will be there). w for write mode(exitsing one will desapire) . r for read mode 

date=datetime.date(datetime.now())
t1=datetime.now()

print("start time : {}".format(t1.strftime("%H:%M:%S")))
file.write("start time : {}\n\n".format(t1.strftime("%H:%M:%S")))
try:

    for port in range(1, 1025):# 1 to 65535 is the range of ports to scan
        #AF_INET MEANS IP4 ADDRESS. AF_INET6 MEANS IP6 ADDRESS
        #SOCK_STREAM MEANS TCP PROTOCOL. SOCK_DGRAM MEANS UDP PROTOCOL
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)  # Set a timeout for the socket connection
        result=sock.connect_ex((host, port))  # connect_ex returns an error indicator
        if result == 0:
            try:
                print("Port no :{} open Protocol service Name: {}".format(port, socket.getservbyport(port, "tcp")))
                file.write("\nPort no :{} open Protocol service Name: {}".format(port, socket.getservbyport(port, "tcp")))
            except socket.error:
                print("Port no :{} open Protocol service Name: {}".format(port, "Unknown"))
                file.write("\nPort no :{} open Protocol service Name: {}".format(port, "Unknown"))

except socket.gaierror:
    print("hostname could not resolved. Existing")
    file.write("\n\nhostname could not resolved. Existing")
    sys.exit()
except socket.error:
    print("couldn't connect to server. Existing")
    file.write("\n\ncouldn't connect to server. Existing")
    sys.exit()

t2=datetime.now()
print("end time : {}".format(t2.strftime("%H:%M:%S")))
file.write("\n\nend time : {}".format(t2.strftime("%H:%M:%S")))

total_time= t2 - t1
print("Total time:{}".format(total_time))
file.write("\n\ntotal time : {}".format(total_time))

file.close()
print("results saved in port-scanner.txt")
# Note: This script scans ports 1 to 1024 on the specified host and saves the results in a text file.
# You can change the target variable to scan a different host.
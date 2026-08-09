# Basic Network Sniffer

## Project Overview
I developed this Basic Network Sniffer using Python as part of my CodeAlpha Cyber Security Internship.
A network sniffer is a program that captures the data packets moving through a network and displays useful information about them.
Whenever we use the internet, our computer continuously sends and receives packets. These packets contain information about the communication between devices.
In this project, I used Python and Scapy to capture these packets and analyze some basic information from them.
The program displays details such as:
Source IP address
Destination IP address
Protocol used
Packet size
Packet capture time
Payload information
After capturing the packets, the program also gives a protocol summary, which shows how many packets were captured using TCP, UDP, ICMP, and other protocols.
## Objective
The main objective of this project is to understand how network packets are captured and analyzed using Python.
Through this project, I wanted to learn how to:
Capture network traffic.
Read information from captured packets.
Identify different network protocols.
Find the source and destination IP addresses.
Calculate the size of packets.
Access the data carried inside packets.
Count packets based on their protocols.
Display the captured information in a simple format.
## Technologies Used
- Python 3:
I used Python to write the complete program and implement the packet-capturing and analysis logic.
- Scapy:
I used the Scapy Python library for working with network packets.
Scapy allows us to capture packets and access different parts of a packet, such as IP information, protocol information, and raw data.
- Command Prompt:
I used Windows Command Prompt to run the Python program and display the captured packet information.
- Windows:
The project was developed and tested on a Windows system.
## How the Project Works
The project works in a simple sequence.
First, the program starts and displays the name of the project.
Then it starts capturing network packets.
For this project, I configured it to capture 20 packets.
While the program is running, normal network activity generates packets. The program captures these packets and examines them one by one.
For every packet, it tries to find useful information such as:
Time
Source IP
Destination IP
Protocol
Packet Size
Payload
After all 20 packets are processed, the program displays a summary showing how many packets belonged to each protocol.
## The basic working can be represented as:
Start Program
      ↓
Capture Packets
      ↓
Analyze Packets
      ↓
Extract Information
      ↓
Display Packet Details
      ↓
Count Protocols
      ↓
Display Protocol Summary
Packet Capture
The first major part of the project is packet capturing.
When I run the program, it displays:
BASIC NETWORK SNIFFER

Capturing 20 packets...
Generate some normal network traffic.
At this point, the program waits for network packets.
I can generate normal network traffic by using the internet or other network activity. The program captures the packets generated during this process.
Once a packet is captured, the program processes it and displays its information.
Information Displayed for Each Packet
For every packet, the program displays information similar to:
Packet #1
Time          : 17:33:10
Source IP     : 172.64.146.215
Destination   : 192.168.0.105
Protocol      : UDP
Packet Size   : 632 bytes
Packet Number
The packet number tells us the order in which the packet was captured.
For example:
Packet #1
Packet #2
Packet #3
This makes it easier to identify individual packets.
Time
The time tells us when the packet was captured.
Source IP
The source IP address tells us where the packet came from.
In simple terms:
Source IP = Sender
Destination IP
The destination IP address tells us where the packet is going.
In simple terms:
Destination IP = Receiver
So we can understand the communication as:
Source → Destination
Sender → Receiver
## Protocol
The protocol tells us what type of network communication the packet is using.
For example:
TCP
UDP
ICMP
In our output, we can see:
Protocol : UDP
Packet Size
Packet size tells us how much data the complete packet contains, measured in bytes.
For example:
Packet Size : 632 bytes
Understanding Protocols
The program checks different protocols in the captured packets.
### TCP — Transmission Control Protocol
TCP stands for Transmission Control Protocol.
TCP is a connection-oriented and reliable protocol. Before sending data, it establishes a connection between the sender and receiver.
TCP makes sure that data reaches the destination correctly and in the proper order. If some data is lost during transmission, TCP can retransmit it.
For example, TCP is commonly used for:
Web communication such as HTTPS
File transfers
Email communication
SSH connections
A simple example is:
Sender
   ↓
Establish Connection
   ↓
Send Data
   ↓
Receiver
   ↓
Acknowledgement
So, we can remember TCP as:
TCP = Reliable and connection-oriented communication
### UDP — User Datagram Protocol
UDP is a connectionless protocol. It does not establish a connection before sending data.
Because it has less overhead than TCP, UDP can be faster, but it does not provide the same delivery guarantees as TCP.
If a UDP packet is lost, UDP itself does not retransmit that packet.
UDP is commonly used for applications where speed is important, such as:
DNS
Online gaming
Live streaming
Voice and video communication
A simple representation is:
Sender
   ↓
Send Data
   ↓
Receiver
There is no connection establishment or acknowledgement mechanism like TCP.
So, we can remember UDP as:
UDP = Fast and connectionless communication
UDP : 20
### ICMP — Internet Control Message Protocol.
ICMP is mainly used for network error reporting, diagnostics, and control messages.
It is not normally used to transfer application data like TCP or UDP.
One common example is the ping command.
When we use:
ping google.com
ICMP messages can be used to check whether a destination is reachable and to measure the response time.
So, we can remember ICMP as:
ICMP = Network diagnostics and control messages
### Other:
If a packet doesn't match the protocols being specifically checked by our program, it is counted under Other.
Understanding Payload
One important part of this project is understanding the payload.
A packet contains different types of information.
### We can think of it like this:
Packet
│
├── Header
│     Information used for communication
│
└── Payload
      Data carried by the packet

For example, the header can contain information about the source, destination, and protocol.
The payload contains the actual data carried by the packet.
In our program, we check whether a packet contains a Raw layer. If it does, we can access its data.
The code we used is:
payload = bytes(packet["Raw"].load)
Here:
packet["Raw"] accesses the Raw layer.
.load gets the data stored in that layer.
bytes() converts the data into bytes.
So this code basically allows the program to access the raw data carried by the packet.
Not every packet contains a Raw layer, so the program checks for it before trying to access it.
Protocol Summary
After processing all the packets, the program displays a protocol summary.
### For example:
'''
==============================
       PROTOCOL SUMMARY
==============================

TCP   : 0
UDP   : 20
ICMP  : 0
Other : 0

Total packets captured: 20

Capture completed!'''
This summary gives us a quick idea about the type of traffic that was captured.
Instead of checking every packet individually, we can look at the summary and immediately understand how many packets belonged to each protocol.
The result depends on the network traffic captured during that particular run.
How Protocol Counting Works
While processing each packet, the program keeps separate counters for the protocols.
For example:
TCP counter
UDP counter
ICMP counter
Other counter
Whenever a packet is identified as a particular protocol, its counter is increased.
After all the packets have been processed, these counters are displayed in the protocol summary.
For example, if 20 packets are identified as UDP packets:
UDP : 20
## Final Output
After fixing the errors, the program successfully started capturing packets.
The output looked like:
BASIC NETWORK SNIFFER

Capturing 20 packets...
Generate some normal network traffic.

Packet #1
Time          : 17:33:10
Source IP     : 172.64.146.215
Destination   : 192.168.0.105
Protocol      : UDP
Packet Size   : 632 bytes
The program continues displaying the captured packets and finally gives the protocol summary.
## What I Learned From This Project
While working on this project, I learned both programming and networking concepts.
I learned how to use Python for a practical cybersecurity project.
I also learned how network packets contain different types of information and how this information can be accessed programmatically.
Some of the main concepts I learned are:
Network packets
Source and destination IP addresses
TCP
UDP
ICMP
Packet size
Packet headers
Payload
Packet capturing
Protocol counting
Basic network traffic analysis
I also improved my Python debugging skills by fixing errors such as IndentationError and SyntaxError.
## Conclusion
This project helped me understand the basics of network traffic monitoring and packet analysis using Python.
By creating the Basic Network Sniffer, I was able to capture packets, extract important information from them, identify protocols, and generate a simple summary of the captured traffic.
Although this is a basic implementation, it gave me a practical understanding of how packet analysis works and how Python can be used in cybersecurity.

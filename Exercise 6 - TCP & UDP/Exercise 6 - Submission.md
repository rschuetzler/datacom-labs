Exercise 6: TCP & UDP
==========================
Name:

Date:

Questions
-------------------

1. What are the IP addresses of Alice and Bob?

| VM name | IP address |
|---------|------------|
| VM1     |            |
| VM2     |            |
| VM3     |            |


### UDP short message

1. What are the source and destination ports of the UDP datagram?
2. What are the source and destination IP addresses of the message?
3. How many UDP packets did it take to send your short message (hint: only count packets
   captured that list UDP as the protocol)?
4. How many bytes was the message?
5. How many total bytes (from all packets) were required to transmit this message (add up
   the "length" of all UDP packets)?
6. How many bytes of data were sent (hint: click the packet in Wireshark and look at the
   "Data" section).

### TCP short message
1. What are the source and destination IP addresses of the message?
2. What are the source and destination ports of the TCP datagram?
3. How many TCP packets did it take to send your short message (hint: only count packets
   captured that list TCP as the protocol)?
4. How many bytes was the message?
5. How many total bytes (from all packets) were required to transmit this message (add up
   the "length" of all TCP packets)?
6. How many bytes of data were sent (hint: find the message in Wireshark and look at the
"Data" section).

### TCP & UDP long messages

1. The `netcat` program can be used to transfer the contents of files between
   machines. You transferred a large file to the stdout (aka the terminal) on Alice's
   computer using the `netcat [ip] [port] < filename.txt` syntax on Bob. If you had typed
   `netcat -l [port] > filename.txt` on Alice, that output would have gone into a
   file. Would TCP or UDP be better used for a file transfer like this? and why?
2. What 

### Critical thinking

1. What are two important differences between TCP and UDP when sending short messages?
2. Why would someone choose to use TCP to send short messages (e.g. NTP for time
synchronization, IRC for chat)?
3. Name a service that uses UDP, and explain why.


__Brainstorming__

1. Why don't you have to close netcat manually when you use TCP to send a long file?
2. How many packets did UDP take to send the message? What about TCP?

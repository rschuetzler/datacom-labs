Exercise 5: TCP & UDP
==========================
Name:

Date:

Questions
-------------------

1. What are the IP addresses of Alice and Bob?

| VM name | IP address |
|---------|------------|
| Alice   |            |
| Bob     |            |


### UDP short message

2. What are the source and destination ports of the UDP datagram?
3. What are the source and destination IP addresses of the message?
4. How many UDP packets did it take to send your short message (hint: only count packets
   captured that list UDP as the protocol)?
5. How many bytes was the message?
6. How many total bytes (from all packets) were required to transmit this message (add up
   the "length" of all UDP packets)?
7. How many bytes of data were sent (hint: click the packet in Wireshark and look at the
   "Data" section).

### TCP short message
8. What are the source and destination IP addresses of the message?
9. What are the source and destination ports of the TCP datagram?
10. How many TCP packets did it take to send your short message (hint: only count packets
   captured that list TCP as the protocol)?
11. How many bytes was the message?
12. How many total bytes (from all packets) were required to transmit this message (add up
   the "length" of all TCP packets)?
13. How many bytes of data were sent (hint: find the message in Wireshark and look at the
"Data" section).

### TCP & UDP long messages

14. The `netcat` program can be used to transfer the contents of files between
   machines. You transferred a large file to the stdout (aka the terminal) on Alice's
   computer using the `netcat [ip] [port] < filename.txt` syntax on Bob. If you had typed
   `netcat -l [port] > filename.txt` on Alice, that output would have gone into a
   file. Would TCP or UDP be better used for a file transfer like this, and why?

### Critical thinking

15. What are two important differences between TCP and UDP when sending short messages?
16. Why would someone choose to use TCP to send short messages (e.g. IRC for chat
   or SMTP for short emails)?
17. Name a service that uses UDP, and explain why.


__Brainstorming__

18. Why don't you have to close netcat manually when you use TCP to send a long file?
19. How many packets did UDP take to send the message? What about TCP?

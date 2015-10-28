NSLookup to Query Domain Name System Information
==================================================

NSLookup is a tool for querying the Domain Name System (DNS). It is found on Windows, Linux, and OSX. This exercise is designed for Windows, but the commands should work on Linux and OSX as well.

Prerequisites
----------------------
  - No software prerequisites. 
  - Some familiarity with the Domain Name System and Internet Protocol is expected.

Introduction
---------------------

Your computer uses the Domain Name System (DNS) to translate a domain name (such as google.com) into an IP address (such as 10.0.1.1).

Basic NSLookup Commands
-------------------------

First, you should make sure you have a DNS server listed in your IP configuration.

In Windows, run the following command:

```
> ipconfig /all
```

```
> nslookup google.com
```

This will query the DNS esrver configured on this computer.


```
> nslookup google.com
```

Note that in the output, there will be the text "non-authoritative answer." Most likely, this means that the DNS information was cached on the resolving DNS server.


Interactive Mode
------------------------

Run the following command to enter interactive mode.

```
> nslookup
```

The output will show the default DNS server and its IP address.

Now, you can run commands without typing "nslookup."

```
> google.com
```

To see all of the DNS records, use the 'ls' command.

```
> ls google.com
```

The 'ls' command attempts a zone transfer. You will receive an error because zone transfers between Google's DNS servers and your own DNS servers.

Using the 'Set' Command
--------------------------

```
> set type='ns'

```
Only shows nameservers.

Ouputting Files
------------------------

You can use the '>' command to send the command output to a file. In the following example, the output of the command will be written to the file 'google.txt.' Note that if you do not specify a folder, the file will be written to the folder where you ran the original 'nslookup' command.

```
> google.com > google.txt
```

In this demo, I ran 'nslookup' while I was in C:\Users\Jim. So the previous command created C:\Users\Jim\google.txt. The easiest way to change your output directory is to quit the interactive mode (using the `quit` command), changing folders, and running `nslookup` again.

Open the file in a text editor to view the output.

Changing the Server
-------------------------

```
> server 8.8.8.8
```

8.8.8.8 is a public DNS server maintained by google.


```
> www.gogle.com
```

```
> set typeall
```

Learning More
-----------------
In interactive mode, enter a question mark and press enter to see help.

```
> ?
```

Challenge
---------------------

Use NSLookup to find the requested information below. Sample commands are listed after this section, but try to complete it without looking at the answers.

1. Determine the mail server DNS records for yahoo.com.
2. Compare your default DNS server settings for yahoo.com with Google's DNS server (8.8.8.8). Are there any differences?

Appendix - Challenge Commands
-------------------------------

1. Mail server DNS records for yahoo.com.

```
> set type=mx
> yahoo.com
```

2. Comparing differences

It might be easiest to output the commands to separate files and compare the resulting text.

```
> quit
> nslookup
> yahoo.com > localdns-yahoo.txt
> server 8.8.8.8
> yahoo.com > googledns-yahoo.txt
> quit
```

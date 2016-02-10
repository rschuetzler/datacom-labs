---
header-includes:
- \usepackage{xcolor}
- \definecolor{Light}{gray}{0.90}
- \let\OldTexttt\texttt
- \renewcommand{\texttt}[1]{\OldTexttt{\colorbox{Light}{#1}}}
---
Lab Exercise: TCP and UDP
==========================

Internet Protocol (IP) addressing helps to identify the location of machines on a network and facilitates routing messages between machines. 

Prerequisites
--------------------------
Before starting this lesson, you should have a basic understanding of the following terms:

* TCP
* UDP
* Ports

### Install Wireshark

1. Go to https://www.wireshark.org/download.html and download the appropriate version of Wireshark for your _host_ operating system
2. Run the installer to install both Wireshark and the packet capture driver (`winpcap` for Windows)

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Explain the differences between TCP and UDP
2. Use Wireshark to view and analyze TCP and UDP data streams
3. Use `netcat` to send messages on a network


Steps
--------------------------

In this section, the "host" refers to your computer. "Guest" refers to the virtual machine running inside your computer.

### Step 1: Initialize VMs

* Create a new folder on your computer for this exercise.
* Copy the `Vagrantfile`, `bootstrap.sh`, and `dangerous.txt` from the lab materials to the directory
* Open a command prompt and navigate to the folder.
    * (Remember Start > cmd [enter], `cd`, `md`)
* Run `> vagrant up` to initialize the virtual machines for this lab.
    * The two machines you'll be using here are named `alice` and `bob`.
    * This step may take a little bit as software is installed for this lab.
* Open a second command prompt and navigate to the same directory. You'll need connections
  to both Alice and Bob simultaneously.

### Step 2: Gather information

* In one command prompt, connect to Alice with `> vagrant ssh alice`. From the other,
  connect to Bob with `> vagrant ssh bob`.
* Determine the IP address of the `eth1` interface of each VM. Record the IP addresses in
  the assignment submission, and keep them handy. You'll need them soon.


### Step 3: Examining short messages in UDP
* Before executing any commands at this stage, review the entire section. Once you start
  `tshark`, you'll have a limited amount of time to complete the other steps, so you want
  to be ready for them. It may even be wise to try running the `netcat` commands on each
  machine to make sure you understand them, then do it again with `tshark` running to get
  the packet capture.
* Start wireshark (with `tshark` on Alice)
* `tshark` is a version of Wireshark designed to run on the command line. 
    * The following is the command to run the `tshark` program in the background so we can
    	complete the other commands. You should change the `duration:[number]` option to a
    	number of seconds. This is how long (in seconds) `tshark` will run before
    	automatically stopping and saving the capture to a file. Give yourself plenty of
    	time, but not so long that you have to wait a long time for the program to finish
    	its job.
    * `-f "not broadcast and not multicast"` filters all packets that are not send directly
      to the computer doing the capture. 
    * `-i eth1` tells tshark to capture packets on the `eth1` interface, which in this
      case is the network interface connecting Alice and Bob. Use `ifconfig` or `tshark
      -D` to get a list of possible network interfaces.
    * The `-a duration:30` option tells tshark to run for 30 seconds before automatically
    	finishing its capture (adjust this time as necessary to give yourself enough time
    	to finish typing all of the `netcat` commands before the capture quits).
    * The `-w /vagrant/udp.pcap` option tells tshark to save the output of the capture to
    	the file `/vagrant/udp.pcap`.
    * The `-Q` option tells tshark to do its capture quietly, without any output to the
    	terminal. This is important due to the next command...
    * `&` at the end of any Linux command tells it to run in the background. This will allow
    	us to execute other commands while the capture is running.

```
$ tshark -f "not broadcast and not multicast" -i eth1 -a duration:30 -w /vagrant/udp-short.pcap -Q &
```

* Use `netcat` to set up listening on a UDP port on Alice.
    * `-u` tells netcat we'll be using UDP.
    * `-l 4242` tells netcat to listen on port 4242.

```
$ netcat -ul 4242
```

* Use netcat to send a UDP message to Alice from Bob
  * Enter the following command at Bob's command prompt to open a connection to Alice,
  substituting Alice's IP address where indicated (remove the `<>`).
```
$ netcat -u <Alice's eth1 IP Address> 4242
```
* Once the connection has started, type a brief message (1 or 2 sentences) and hit Enter
  to send.
* After the message is sent, hit CTRL+C on Bob to end the `netcat` connection. Switch over
  to Alice and type Ctrl+C again to stop listening. Wait for your `tshark` session to end
  (at whatever time limit you set).

#### Examining UDP in Wireshark

On your host computer, open up a file browser (e.g. Windows Explorer) and find the
directory you created for this lab. There you should find a file named `udp.pcap`. This
file should contain all of the packets sent between Alice and Bob while your tshark
session was running. Open that file in Wireshark.

* Answer the questions in the submission file regarding your short UDP message.

### Step 4: Examining TCP

Now we will send a short message (the same short message as before) using TCP instead of
UDP.

* Start `tshark` again, changing the name of the output file to
  `/vagrant/tcp-short.pcap`. This is important, because you may want to review the UDP and
  TCP files to answer some of the questions in the submission.
* On Alice, run `$ netcat -l 4242` to start listening on port 4242
* On Bob, run `$ netcat <Alice's eth1 ip address> 4242` to open a connection
    * Type your short message and hit Enter to send.
    * Type Ctrl-C to end your connection. This will also close `netcat` on Alice.
* Wait for your `tshark` session to end.
* Open `tcp-short.pcap` in Wireshark on your host computer and use it to answer the
questions in the submission file.

### Step 5: Longer messages

In this section we will use netcat to send the contents of a text file as if we had typed
it. This will let us see how UDP and TCP handle sending and receiving longer messages.

* Open the `dangerous.txt` file you copied from the lab documents. It should contain the
  entire contents of the short story "The Most Dangerous Game" by Richard Connell. As long
  as it's in the same directory as your Vagrantfile, can access it on your Linux VMs at
  `/vagrant/dangerous.txt`.

#### UDP

* Start `tshark`, outputting to the file `/vagrant/udp-long.pcap`.
* Start `netcat` on Alice listening for a UDP message (`-u`) on port 4242.
* On Bob, send the contents of the `dangerous.txt` file over UDP with the following
command:

```
$ netcat -u 192.168.100.10 4242 < /vagrant/dangerous.txt
```

* You should see the contents of the file appear in Alice's terminal.
* Press Ctrl-C on both VMs to stop netcat, then wait for your tshark session to end.
* Open `udp-long.pcap` in Wireshark on your host, and use it to answer the questions in
the submission document

#### TCP

* Start `tshark` with the filename `/vagrant/tcp-long.pcap` as the output.
* Start `netcat` on Alice listening for a _TCP_ message on 4242.
* On Bob, send the contents of `dangerous.txt` over TCP to Alice
* Wait for your `tshark` session to end, then open `tcp-long.pcap` in Wireshark on your
host.
* Answer the questions in the submission file

### Step X: Cleanup (Optional)

After submitting your work, you can destroy any boxes you used.

* Run "`$ exit`" to leave the SSH session. You will be back at your regular command prompt.
* Run "`> vagrant destroy`" to turn off the machine and delete it completely from your system. Answer "y" to confirm deletion.

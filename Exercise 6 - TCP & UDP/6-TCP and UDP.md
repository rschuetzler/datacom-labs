Exercise 6: TCP and UDP
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

1. 

Steps
--------------------------

In this section, the "host" refers to your computer. "Guest" refers to the virtual machine running inside your computer.

### Step 1: Initialize VMs

* Create a new folder on your computer for this exercise.
* Copy the `Vagrantfile` and `dangerous.txt` from the lab materials to the directory
* Open a command prompt and navigate to the folder.
    * (Remember Start > cmd [enter], `cd`, `md`)
* Run `> vagrant up` to initialize the virtual machines for this lab.
    * The two machines you'll be using here are named `alice` and `bob`.
    * This step may take a little bit as software is installed for this lab.
* Open a second command prompt and navigate to the same directory. You'll need connections
  to both Alice and Bob simultaneously.

### Step 2: Gather information

* In one command prompt, connect to Alice with `vagrant ssh alice`. From the other,
  connect to Bob with `vagrant ssh bob`.
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
    * `-f "not broadcast and not multicast` filters all packets that are not send directly
      to the computer doing the capture. 
    * `-i eth1` tells tshark to capture packets on the `eth1` interface, which in this
      case is the network interface connecting Alice and Bob. Use `ifconfig` or `tshark
      -D` to get a list of possible network interfaces.
    * The `-a duration:30` option tells tshark to run for 30 seconds before automatically
    	finishing its capture (adjust this time as necessary to give yourself enough time
    	to finish typing all of the `netcat` commands).
    * The `-w /vagrant/udp.pcap` option tells tshark to save the output of the capture to
    	the file `/vagrant/udp.pcap`.
    * The `-Q` option tells tshark to do its capture quietly, without any output to the
    	terminal. This is important due to the next command...
    * `&` at the end of any Linux command tells it to run in the background. This will allow
    	us to execute other commands while the capture is running.

```
tshark -f "not broadcast and not multicast" -i eth1 -a duration:10 -w /vagrant/udp.pcap -Q &
```

* Use `netcat` to set up listening on a UDP port on Alice.
    * `-u` tells netcat we'll be using UDP.
    * `-l 4242` tells netcat to listen on port 4242.

```
netcat -ul 4242
```

* Use netcat to send a UDP message to Alice from Bob
  * Enter the following command at Bob's command prompt to open a connection to Alice,
  substituting Alice's IP address where indicated (remove the `<>`).
```
netcat -u <Alice's eth1 IP Address> 4242
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


  

### Step : Examining TCP

* Start new capture (new name)
* Use netcat to listen on TCP on VM1
* Send TCP message from VM1 --> VM2
* Stop capture

### Step X: Cleanup (Optional)

After submitting your work, you can destroy any boxes you used.

* Run "`$ exit`" to leave the SSH session. You will be back at your regular command prompt.
* Run "`> vagrant destroy`" to turn off the machine and delete it completely from your system. Answer "y" to confirm deletion.

Submission
----------------------
Create a Word document with the following:

Heading:

  - Name
  - Date
  - Course
  - Exercise 2

Questions

1. What is an IP address?
2. What command line tools would you use on Linux and Windows to display network configurations? List each tool, the operating system on which it's found, and a sentence or two about what it does.
3. Each network adapter in a computer can have different network settings. Describe a situation in which you would want different network settings for two adapters on the same computer. (~100 words)

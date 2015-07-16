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

### Step 1: Setup and Connect to a Linux Guest

* Create a new folder on your computer for this exercise.
* Open a command prompt and navigate to the folder.
    * (Remember Start > cmd [enter], cd, md)
* In the command prompt, run `vagrant init ubuntu/trusty64`
* Run `vagrant ssh` to connect to the machine.

### Outline

* Figure out device IP addresses for VM1 and VM2

### Step : Examining UDP
* Before executing any commands at this stage, 
* Start wireshark (with `tshark` on VM1)
	* `tshark` is a version of wireshark designed to run on the command line. 
	* The following is the command to run the `tshark` program in the background so we can
		complete the other commands. You should change the `duration:[number]` option to a
		number of seconds. This is how long (in seconds) `tshark` will run before
		automatically stopping and saving the capture to a file. Give yourself plenty of time,
		but not so long that you have to wait a long time for the program to finish its job.
	* The `-a duration:10` option tells tshark to run for 10 seconds before automatically
		finishing its capture
	* The `-w /vagrant/udp.pcap` option tells tshark to save the output of the capture to
		the file `/vagrant/udp.pcap`
	* The `-q` option tells tshark to do its capture quietly, without any output to the
		terminal. This is important due to the next command...
	* `&` at the end of any Linux command tells it to run in the background. This will allow
		us to execute other commands while the capture is running.

```
tshark -a duration:10 -w /vagrant/udp.pcap -q &
```

* Use netcat to set up listening on a UDP port on VM1
  * `netcat -ul 4242`
* Use netcat to send a UDP message to VM1 from VM2
* Stop capture



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

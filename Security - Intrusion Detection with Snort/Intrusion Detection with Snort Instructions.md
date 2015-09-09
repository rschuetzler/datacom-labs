Intrusion Detection with Snort Instructions
=============================================

Learning Objectives
----------------------
By the end of this lesson, you will be able to

1. Install Snort on CentOS
2. Ensure that Snort is working

Prerequisites
-------------------------
Vagrant installed and properly configured

Snort Overview
--------------------------
Snort is an open source application that can inspect packets on the network. Similar to how antivirus detects malware signatures in the bits of executables, Snort can detect network attack signatures in the packets going over the wire. Snort can trigger events that can prevent damage to the network. Because of its interfaces with other systems, Snort is considered both an Intrusion Detection System (IDS) and Intrusion Prevention System (IPS).

Installing Snort
------------------------------
In this exercise, you will install snort on CentOS. CentOS is basically the free and open version of Red Hat Enterprise Linux. CentOS is a common Linux distribution for servers.

### Create the Linux Virtual Machine

1. Create a new folder on your system.
2. Open a command prompt and navigate to your new folder.
3. Run `> vagrant init puppetlabs/centos-7.0-64-puppet`
  - Type the commands instead of copying and pasting to avoid any errors with the character encoding of the dash.
4. Run `> vagrant up` to bring up the virtual machine.
  - If this is the first time you've used this box, it will download automatically.
5. Run `> vagrant ssh` to connect to the machine.

### Install Snort Packages

The following steps install data acquisition (DAQ) modules and Snort.

1. Run `$ sudo yum install https://snort.org/downloads/snort/daq-2.0.6-1.centos7.x86_64.rpm`
  - Note that with Ubuntu, you install packages using `apt-get install`. CentOS uses `yum` to install packages.
  - Enter "y" when prompted to proceed.
2. Run `$ sudo yum install https://snort.org/downloads/snort/snort-2.9.7.5-1.centos7.x86_64.rpm`.
  - Enter "y" when prompted to proceed.

### Update Snort Rules

1. Run `$ wget https://snort.org/rules/community`
  - wget is a utility to download files from the command line.
2. Run `$ sudo tar -xvf community -C /etc/snort/rules`
  - This will extract the Snort rules and put them in the proper directory.
3. Register for an account on snort.org to obtain the latest rules.
  - You must register at snort.org.
  - Afer registering, access your account settings and find your "Oinkcode."
  -Your Oinkcode will look something like the following: fbee8de6567e63ed48fdc1ee750fae417c1607c4.
4. Run 

```
$ wget https://snort.org/rules/snortrules-snapshot-2975.tar.gz?oinkcode=<oinkcode>
```
  - Note that updated rules might be available. Check the download instructions on snort.org to verify the correct file name.
5. Run `$ sudo tar -xvfz snortrules-snapshot-<version>.tar.gz -C /etc/snort/rules`
6. Run `$ cat /etc/snort/rules/protocol-ftp.rules` and examine what the rule file looks like.

### Edit /etc/snort/rules.conf

1. Replace the following variables in /etc/snort/rules.conf with these values:
  - The program vi is installed by default. Run `$ sudo vi /etc/snort/rules.conf` to edit the file with vi. Vi is powerful, but it has a steeper learning curve.
  - CentOS does not come with nano by default. It is easier to use, but not as powerful as vi. You can install it by running `$ sudo yum install nano`, then run `$ sudo nano /etc/snort/rules.conf`.
  
```
var RULE_PATH /etc/snort/rules
ipvar HOME_NET 10.0.2.0/24
ipvar EXTERNAL_NET !$HOME_NET
var SO_RULE_PATH /etc/snort/so_rules
var PREPROC_RULE_PATH /etc/snort/preproc_rules
var WHITE_LIST_PATH /etc/snort/rules
var BLACK_LIST_PATH /etc/snort/rules
```

### Modify Filesystem Permissions

Failure to run these commands will result in errors.

1. Run `$ sudo mkdir -p /usr/local/lib/snort_dynamicrules`
2. Run `$ sudo chown -R snort:snort /usr/local/lib/snort_dynamicrules`
3. Run `$ sudo chmod -R 700 /usr/local/lib/snort_dynamicrules`

### Verify Instalation

1. Run `$ sudo snort -v`
  - This will just output the captured packets to the console.
2. View the output for a few moments to become familiar with the output.
3. Press control + C to cancel the capture. Summary statistics will be displayed.
4. Run `$ mkdir log` to create a folder to hold logs.
5. Run `$ sudo snort -dev -l ./log` to start logging packets.
  - After about 20 seconds, press control + C to stop logging.
6. Run `$ cd log` to navigate to the log folder.
7. Run `$ ls` to list files. A log file should be listed.
  - By default, if no log directory is specified, /var/log/snort will be used.

### Basic Intrusion Detection

1. Run `$ sudo snort -d -c /etc/snort/snort.conf`
  - This will create a log file called "alert" in /var/log/snort.
2. 
  
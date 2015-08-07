Exercise 5: Domain Name System (DNS)
==========================

The Domain Name System (DNS) is one of the most critical parts of the Internet. Companies also setup and configure their own DNS servers so that they can route intranet traffic. In this exercise, you will setup a DNS server in Linux.

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Define the different types of DNS server (root, TLD, authoritative, resolving)
2. Explain how caching is used in DNS and the consequences of caching.
3. Configure an authoritative DNS server.
4. Configure a client to connect to a specific DNS server.

<!---
Things I (Ryan) would like to add:
* Hosts file
--->

Steps
--------------------------

### Step 1: Load the Preconfigured Vagrant File

Previously, when you ran "`vagrant init ubuntu/Trusty64`", Vagrant automatically generated a file named "`Vagrantfile`" (with no extension). This file contains the configuration options for your virtual machine. For this exercise, a Vagrantfile has already been created.

* Copy the Vagrantfile for this exercise to a folder.
* Open a command prompt and navigate to the folder where you saved the Vagrantfile.
* Run `vagrant up` to bring up the machines.
    * Note that because two machines are defined in the Vagrantfile, any Vagrant command that does not target a specific machine will automatically target all machines.

Note that *two* virtual machines will be created. The machines are named "alice" and "bob."

### Step 2: Check Network Settings

* Run `> vagrant ssh alice` to connect to the first machine.
* Open a new command prompt, navigate to the folder with your Vagrantfile, and run `> vagrant ssh bob` to connect to the second machine.
* Run `$ ifconfig` to check the IP address and subnet of each machine.
* Note that there are two ethernet connections. This lab will focus on `eth1`. This is a bridged connection that allows multiple guests virtual machines to communicate with each other. For the purposes of this exercise, you can pretend that `eth0` doesn't exist.

### Step 3: Setup Bob as an Authoritative DNS Server

BIND9 is a popular software package for DNS on Linux. In can operate in 3 modes: 1) caching, 2) primary master, and 3) secondary master. As a caching nameserver, BIND9 just remembers DNS information provided from other sources. As a primary master, BIND9 reads DNS information from a configuration file on the machine and resolves IP addresses. As as secondary master, BIND9 resolves DNS information from another authoritative machine. In this example we will setup Bob as a primary master. That means that machines can query Bob for authoritative DNS information.

Consider the example of the website google.com. If your computer has never connected to google.com, and your ISP has not cached google.com's IP address, you need to do a full DNS lookup. The steps would look like this.

1. Your computer uses the DNS protocol to query the resolving DNS server configured for your network.
2. The resolving DNS server checks its cache for google.com, cannot find it, so it queries the root DNS server for the `.com` top level domain (TLD).
3. The root nameserver gives the IP address for a `.com` TLD and sends it to the resolving nameserver.
4. The resolving nameserver queries the `.com` TLD and asks for google.com's authoritative nameserver.
5. The resolving nameserver queries google.com's authoritative nameserver for the IP address.
6. The resolving nameserver sends the IP address for google.com back to your computer.

* Run `> vagrant ssh bob`
* Run `bob$ sudo apt-get update && sudo apt-get install bind9`
    * This will download and install the bind9 software.
    * Answer `y` when prompted to install.
* Run `bob$ cat /etc/bind/named.conf.local`
    * This will print the DNS configuration. Currently, nothing is configured. The only lines in the configuration file are commented out (using two forward slashes).
* Run `bob$ sudo cp /etc/bind/db.local /etc/bind/db.networkclass.com`
    * This will create a template we can use to modify a valid DNS configuration file. The `db.local` file contains information for resolving `localhost.`
* Run `bob$ sudo nano /etc/bind/db.networkclass.com`
    * `nano` is a text editor that is fairly easy to use. More powerful text editing programs like `vi` and `emacs` exist, but they have steeper learning curves. If you are going to work with Linux professionally, you must learn `vi` basics. But for now, `nano` will work fine.
* Make the following changes to `db.networkclass.com`:
    * Change `localhost. root.localhost.` to `ns.networkclass.com. root.networkclass.com.`
    * Change `localhost.` to `ns.networkclass.com`
    * Change `127.0.0.1` to `192.168.100.25`
    * Add the line `ns  IN  A   192.168.100.25`
    * Add the line `www IN  A   192.168.100.24`
* Type Control+O, [enter] to save the file, and Control+X to exit.
* Create a reverse zone file by running the command `bob$ sudo cp /etc/bind/db.127 /etc/bind/db.192`
* Run `bob$ sudo nano /etc/bind/db.192`
    * Change `localhost. root.localhost.` to `ns.networkclass.com. root.networkclass.com.`
    * Change `@ IN  NS  localhost.` to `@ IN  NS  ns.networkclass.com`
    * Change `1.0.0 IN  PTR  localhost.` to `25  IN  PTR ns.networkclass.com.`
    * Add `24   IN  PTR www.networkclass.com.`
    * Save the files as before and exit.
    * Note that "25" and "24" refer to the last number in the IP address of the server (e.g. 192.168.100.25).
* You have now created two configuration files, but bind9 is not looking for them, yet. Edit the `named.conf.local` file to point to these new configuration files.
* Run `bob$ sudo nano /etc/bind/named.conf.local`
* Add the following to the file:

```
// Forward zone
zone "networkclass.com" {
  type master;
  file "/etc/bind/db.networkclass.com";
};
//reverse zone
zone "100.168.192.in-addr.arpa" {
  type master;
  file "/etc/bind/db.192";
};
```

* Run `bob$ sudo service bind9 restart` to restart the bind9 service to reload the configuration files.
    * If you see a message ending with "...fail!" then you probably missed a semicolon or misconfigured one of the files. Double check that you have them exactly right. Bind9 is not forgiving. Fix your configuration files until you see "...done." when restarting bind9.
* Run `bob$ named-checkzone networkclass.com /etc/bind/db.networkclass.com`
    * You should see "OK"
* Run `bob$ named-checkzone 100.168.192.in-addr.arpa. /etc/bind/db.192`
    * You should see "OK"
* Run `bob$ nslookup www.networkclass.com 192.168.100.25` to run a DNS query on the machine.
* Run `bob$ nslookup ns.networkclass.com 192.168.100.25` to query the nameserver.
* Run a reverse lookup with `bob$ nslookup 192.168.100.24 192.168.100.25`
    * You should see that www.networkclass.com resolves to that IP address.
* Run a reverse lookup with `bob$ nslookup 192.168.100.25 192.168.100.25`
    * You should see that ns.networkclass.com resolves to that IP address.

### Step 4: Configure Alice to Point to Bob's DNS

TODO

### Step 5: Cleanup (Optional)

After submitting your work, you can destroy any boxes you used.

* Run "`$ exit`" on Bob and Alice to leave the SSH sessions.
* Run "`> vagrant destroy`" to turn off the machines and delete them completely. Answer "y" to confirm deletion.

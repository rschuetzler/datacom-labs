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

Webmin is a web interface to administer various aspects of your system. For this lab we will use Webmin to configure DNS in Bind9. While it is possible to configure DNS entirely through the command line, the process is tedious and unforgiving. Small typos will break your configuration. It is available through third-party repositories which were added to your VM when it booted. Instructions for setting up Webmin on your own server are available [here](https://www.digitalocean.com/community/tutorials/how-to-install-webmin-with-ssl-on-ubuntu-14-04).

* Run `> vagrant ssh bob`
* Run `bob$ sudo apt-get install bind9 webmin`
    * This will download and install the bind9 software and webmin.
    * Answer `y` when prompted to install.
* Run `bob$ cat /etc/bind/named.conf.local`
    * This will print the DNS configuration. Currently, nothing is configured. The only lines in the configuration file are commented out (using two forward slashes).
* Run `bob$ ifconfig` and verify the IP address for eth1
* On your host computer, open a web browser and navigate to `https://192.168.100.25:10000`. Webmin runs a web server on port 10000.
    * You will likely get a warning that your connection is not private, or that there is an error with the certificate. In this case it is safe to ignore this error. The webmin server uses a self-signed certificate to encrypt your communications. This is not trusted by your host OS, so it displays the warning. Bypass the error and continue to 192.168.100.25
* Sign into webmin with the username and password `vagrant`.
* Under "Servers" in the menu on the left, select "BIND DNS Server". You will then see a large list of options and actions you can run on BIND.
* We will create two DNS Zones: first the forward zone, then the reverse zone. The forward zone converts names to IP addresses, while the reverse zone converts IP addresses back to names.
* Create the forward zone
    * Under "Existing DNS Zones," select "Create master zone."
    * Ensure that Zone type is Forward
    * For Domain name, enter "example.com"
    * For master server, enter "ns.example.com"
    * For email address, enter "admin@example.com"
    * Check the box to "Add NS record for master server?"
    * Click Create
* Add records to the master zone
    * On the "Edit Master Zone" screen, click "Address (0)". This is where we will add our A records for our subdomains.
    * For Name, put "ns"
    * For Address, put 192.168.100.25. This is the IP address of Bob's computer, which is the DNS _name server_.
    * Click Create.
    * Do the same for the subdomain www, with the address 192.168.100.24
    * Make sure you click Create before moving on.
	* Click "Return to record types" at the bottom of the page.
* Add a reverse DNS Zone
    * Click "Return to zone list" at the bottom of the record types page.
    * Under Existing DNS Zones, click "Create master zone."
    * Zone type: Reverse
    * Domain name/Network: 192.168.100
    * Master server: ns.example.com
    * Click "Create"
* Add reverse DNS records to the zone
    * Click "Reverse Address (0)"
    * Create two reverse lookup records
        * Address: 192.168.100.24, hostname: www.example.com
        * Address: 192.168.100.25, hostname: ns.example.com
* Click "Return to zone list"
* Click "Apply Configuration" in the top right corner of the screen
* Check to see if your configuration is working
    * Run `bob$ nslookup www.example.com 192.168.100.25` to run a DNS query on the machine.
    * Run `bob$ nslookup ns.example.com 192.168.100.25` to query the nameserver.
    * Run a reverse lookup with `bob$ nslookup 192.168.100.24 192.168.100.25`
        * You should see that www.example.com resolves to that IP address.
    * Run a reverse lookup with `bob$ nslookup 192.168.100.25 192.168.100.25`
        * You should see that ns.example.com resolves to that IP address.

### Step 4: Configure Alice to Point to Bob's DNS

Now we will set up Alice to use Bob as her DNS server. Currently Alice is configured to use herself as a DNS server. 

* First test the existing configuration. Run `alice$ nslookup www.example.com` or `alice$ nslookup ns.example.com` to see the IP addresses that resolve for those domains.
* Record the results of those `nslookup` commands in the submission sheet
* Make Bob the DNS server by modifying the last line of `/etc/dhcp/dhclient.conf` with the command `alice$ nano /etc/dhcp/dhclient.conf` to say:

```
supersede domain-name-servers 192.168.100.25;
```

* Restart Alice's computer to force the networking changes to take effect. This is done with the command: `alice$ sudo shutdown -r now`. This will disconnect you from Alice and restart the VM.
* Reconnect to Alice and test the new DNS settings. Run `alice$ nslookup ns.example.com` and `alice$ nslookup www.example.com` to see what the DNS server is, and what addresses are returned.

### Step 5: HOSTS file

In addition to DNS, you can manually set up host records for your local machine to make it easier to access commonly visited servers. The easiest way is to add a record to your hosts file (`/etc/hosts` on Linux/Mac, `C:\Windows\System32\drivers\etc\hosts` on Windows). This is usually the first place your computer checks for host names (before even going to DNS), so records in your hosts file can be used to override DNS.

* First, try to ping Bob from Alice by typing `alice$ ping bob`. What is the result? Why?
* On Alice, open the hosts file with `alice$ nano /etc/hosts`
* On the last line, add a line with Bob's IP address and the word "bob":

```
192.168.100.25  bob
```

* Save and close the file, now try to `ping bob`. What is the result now?
* Try to ping `google.com`. What is the result? What is Google's IP address?
* Now edit the hosts file again to include the following line:

```
127.0.0.1  www.google.com
```
* Save and close the hosts file and ping google.com one more time. What IP address is pinged when you do this?

### Step 6: Cleanup (Optional)

After submitting your work, you can destroy any boxes you used.

* Run "`$ exit`" on Bob and Alice to leave the SSH sessions.
* Run "`> vagrant destroy`" to turn off the machines and delete them completely. Answer "y" to confirm deletion.

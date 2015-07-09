Exercise 8: Troubleshooting
==============================

* TODO: Include DHCP

Prerequisites
--------------------------
Before starting this lesson, you should have a basic understanding of the following terms:

* IP Address
* Subnet
* Subnet mask
* DNS
* Gateway

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Use `ipconfig` and `ipconfig /all` on Windows to view network configuration.
2. Use `ifconfig` to view Linux network configuration.
3. Use `ip route show` to view Linux the default gateway on Linux.
4. Display the Linux network configuration file.

Steps
--------------------------

In this section, the "host" refers to your computer. "Guest" refers to the virtual machine running inside your computer.

### Step 1: Setup and Connect to a Linux Guest

* Create a new folder on your computer for this exercise.
* Open a command prompt and navigate to the folder.
    * (Remember Start > cmd [enter], cd, md)
* In the command prompt, run `vagrant init ubuntu/trusty64`
* Run `vagrant ssh` to connect to the machine.

### Step 2: Discover the Guest Network Configuration

The default Vagrant box comes preconfigured with networking capability. In this section, you will issue commands to discover what networking is enabled by default.

* Run `$ ifconfig`
    * `ifconfig` is a Linux command that shows the network "**i**nter**f**ace **config**uration."
* Two connections will be listed. We are concerned with the "eth0" interface. The "eth0" is a simulated Ethernet (wired) connection.
* Look at the "inet addr". This is the Internet Protocol (IP) version 4 address. Like all IP addresses, it is composed of 4 numbers between 0 and 255, separated by periods. IP addresses within a network must be unique.
* The "Mask" identifies the subnet (i.e. sub network).
* The "HWaddr" is the hardware address. This is the media access control (MAC) address. Each MAC address is unique across the entire world.
* The output of the command also lists the amount of information sent and received.

You will be come more familiar with these terms throughout the exercises. For now, it is most important that you know where to find this information.

### Step 3: Discover Your Host Computer's Network Configuration

* Open a new command prompt on your host machine.
* Run `> ipconfig` to show the Internet Protocol configuration.
    * This is a tremendously important command. Remember it.
    * The number of interfaces depends on the number of network adapters on your machine and software installed (such as Virtual Private Network [VPN] software or VirtualBox).
    * Look for a connection named "Ethernet adapter Local Area Connection" or something similar.
    * What do you notice that is similar and different from the `ifconfig` output?
* Run `> ipconfig /all`
    * Notice that the Windows `ipconfig /all` command shows the Default Gateway, Domain Name Server (DNS), and Dynamic Control Host Protocol (DHCP) information that the Linux `ifconfig` does not show.

### Step 4: More Guest Network Configuration

Windows makes it easy to see the DHCP configuration and DNS configuration in one place. This same information can be obtained in Linux, but the information is located in several parts of the system.

* Run `$ ip route show`
* The output will show "default via x.x.x.x" (where x.x.x.x is the IP address of the default gateway).
* More information can be found in the network configuration file. In Debian systems (like Ubuntu), run the following command:
    * `$ cat /etc/network/interfaces`
    * The `cat` command prints the contents of files to your shell.
    * `/etc/network/interfaces` is a text file that contains networking configuration.
* You should notice that at the end of the file, there is a `source` command that loads all network configurations in the `/etc/networking/interfaces.d/` directory.
* Run `$ cd /etc/networking/interfaces.d/`
* Run `$ ls` to **l**i**s**t the contents of the folder.
    * There should only be one file in the folder: eth0.cfg.
* Run `$ cat eth0.cfg` and you should see output similar to the following:

```
auto eth0
iface eth0 inet dhcp
```

* The configuration tells us the following facts about the network:
    * `auto eth0` tells the system to load the network interface at boot
    * `iface eth0 inet dhcp` tells the system to obtain an IP address automatically
* There are several ways to get DNS information.
    * Run `$ cat /etc/resolv.conf`
        * Look for the IP address of the nameserver
    * Run `$ dig google.com` (or use another website)
        * The "SERVER:" line will contain the DNS server.
* It is possible to manually define the default gateway, DNS, and IP addressing in the network configuration file (e.g. eth0.cfg), but it is often best to let the system obtain this information automatically.

### Step 5: Cleanup (Optional)

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

Exercise 2: IP Configuration
==========================

Internet Protocol (IP) addressing helps to identify the location of machines on a network and facilitates routing messages between machines. 

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

In this step, you will create a 64 bit Ubuntu Linux virtual machine.

* Create a new folder on your computer for this exercise.
* Open a command prompt and navigate to the folder.
    * (Remember Start > cmd [enter], cd, md. Refer to the first exercise for more detailed instructions on creating and navigating folders in a command prompt.)
* In the command prompt, run `> vagrant init ubuntu/trusty64`
* Run `> vagrant ssh` to connect to the machine.

### Step 2: Discover the Guest Network Configuration

The default Vagrant box comes preconfigured with networking capability. In this section, you will issue commands to discover what networking is enabled by default.

* Run `$ ifconfig`
    * `ifconfig` is a Linux command that shows the network "**i**nter**f**ace **config**uration."
* Two connections will be listed. We are concerned with the "eth0" interface. The "eth0" is a simulated Ethernet (wired) connection.
* Look at the "inet addr". This is the Internet Protocol (IP) version 4 address.
    * Like all IP addresses, it is composed of 4 numbers between 0 and 255, separated by periods. IP addresses within a network must be unique because they identify a specific machine. IP addresses are much like mailing addresses. If two people had the same mailing address, mail carriers would not know where to deliver the mail. IP addresses on a network must be unique. Most operating systems will give you a warning if you try to connect to a network with a duplicate IP address.
* The "Mask" identifies the subnet (i.e. sub network).
    * At a high level, subnets are used to separate traffic to allow for more efficient communication. An analogy is a single large classroom where four classes are simultaneously being taught. It would be difficult to communicate in such a crowded classroom with students asking questions of the various instructors and instructors trying to be heard over the noise. It would be more efficient if the single large classroom were broken down into four distinct classrooms. This way, the communication for each class would be contained in a separate classroom. One of the primary benefits of subnetting is the ability to regulate traffic. Ideally, as much traffic as possible is kept on the same subnet.
* The "HWaddr" is the hardware address. This is the media access control (MAC) address. Each MAC address is unique across the entire world. There are two parts of a MAC address--the hardware vendor identification and the device identification. Every piece of network equipment created by Cisco will start with the same ID, but each device will be unique. This convention is a standard that all device manufacturers follow. It should be noted, however, that users can "spoof" their MAC address, changing it from the address defined in hardware to something that the user chooses in software.
* The output of the `ifconfig` command also lists the amount of data sent and received.

You will become more familiar with these terms throughout the exercises. For now, it is most important that you know where to find this information.

### Step 3: Discover Your Windows Host Network Configuration

This step assumes that you are using a Windows host. If you are not using a Windows host, use a library computer or borrow a friend's Windows computer to complete this section.

* Open a new command prompt on your host machine.
* Run `> ipconfig` to show the Internet Protocol configuration.
    * This is a tremendously important command. Remember it.
    * The number of interfaces depends on the number of network adapters on your machine and software installed (such as Virtual Private Network [VPN] software or VirtualBox).
    * Look for a connection named "Ethernet adapter Local Area Connection" or something similar.
    * What do you notice that is similar and different from the `ifconfig` output?
* Run `> ipconfig /all`
    * Notice that the Windows `ipconfig /all` command shows the Default Gateway, Domain Name Server (DNS), and Dynamic Control Host Protocol (DHCP) information that the Linux `ifconfig` does not show.

### Step 4: More Linux Guest Network Configuration

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


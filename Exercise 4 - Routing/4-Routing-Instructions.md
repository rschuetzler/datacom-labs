Exercise 4: Routing
==========================

In the days of the first computer networks, communication within a single network provided tremendous value. Networked computers could connect to printers, file servers, and each other. But the full power of networked communications could only be realized when computers could communicate across networks. To communicate across networks, data must be routed. In this lesson, you will learn several routing protocols, and you will configure a Linux server as a router. 

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Explain the following routing methods:
    - [Static Routing](https://en.wikipedia.org/wiki/Static_routing)
    - [Routing Information Protocol (RIP)](https://en.wikipedia.org/wiki/Routing_Information_Protocol)
    - [Open Shortest Path First (OSPF)](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
    - [Hot Standby Router Protocol (HSRP)](https://en.wikipedia.org/wiki/Hot_Standby_Router_Protocol)
2. Configure a Linux server as a router

Routing
--------------------------

Routing can be explained by returning to the post office analogy. Consider each city as an individual network. The Las Vegas post office knows where to deliver each piece of mail to every address within its city limits. However, if it receives a piece of mail destined for San Diego, the Las Vegas post office does not know where in San Diego that address resides, and it cannot deliver the mail itself. The Las Vegas post office *routes* the mail to the San Diego post office. The Las Vegas post office knows that Interstate 15 is the fastest way to get to San Diego, so it puts the letter in a van and sends it on its way. When the letter gets to San Diego, the people in the San Diego office know how to deliver the message to the local recipient.

The main purpose of routing is to get data where it's supposed to go as quickly and efficiently as possible. Routing is what occurs between networks. The technology underlying the current Internet and modern computer networking was created in a time when nuclear war was considered a likely possibility. Because an entire city might be destroyed, hardware and software were created to be fault tolerant. Sophisticated routing protocols were created that could adjust routing on the fly in case a node in the network failed. We will cover four basic routing protocols.

Routing Protocols
-------------------------------

[*Routing tables*](https://en.wikipedia.org/wiki/Routing_table) determine what path a router chooses to send data. At a high level, routing tables contain the destination, paths to get to that destination, and a rating for how fast and reliable that path is.

Suppose  you were to construct a routing table for Phoenix, Arizona. The *Network Destination* would be the place you ultimately want to end up at. The *Gateway* is the intermediate hop to get to your final destination. The *Interface* is the network adapter (or transportation method in this example) that can be used to reach the next hop. The *Metric* defines the cost of the route, basically how fast and reliable it is.

|Network Destination| Gateway      | Interface                 | Metric |
|-------------------|--------------|---------------------------|--------|
|Tucson             | Casa Grande  | Bust Stop at 4th and Main | 500    |
|Tucson             | Casa Grande  | Helicopter Pad            | 5      |

If you want to get to Tucson from Phoenix, you must pass through Casa Grande. There are two possible routes defined in the routing table above--a bus and helicopter. The metric for the helicopter is much lower, so the router will choose this route. The router in Casa Grande will have its own routing table for the most efficient way to send data from Casa Grande to Tucson.

|Network Destination| Gateway       | Interface    | Metric |
|-------------------|---------------|--------------|--------|
|192.168.100.15/24  | 192.168.100.1 |192.168.0.100 | 10     |

The above routing table has a single entry. It says that if data needs to get to the 192.168.100.15/24 network, it should send it to 192.168.100.1 using the network card with the IP address 192.168.0.100.

### [Static Routing](https://en.wikipedia.org/wiki/Static_routing)

Static routing is the simplest way to configure routing, though it is only useful for very simple networks. Static routing requires that every routing entry be configured manually. A human being must type in each of the routes. If something changes in the network configuration, the routes must be updated manually.

Imagine a small satellite office where four employees work. The four employees connect to a local printer, but most of the resources they access are on the main campus. A simple static route could forward any non-local traffic to the main campus router. Essentially, there would be a single route.

Large organizations cannot use static routing exclusively. Administrators would have to ensure that hundreds of routers and thousands of routes were properly configured. It would be time consuming and prone to errors. There may be situations, however, where static routing makes sense, but on a limited scale.

### [Routing Information Protocol (RIP)](https://en.wikipedia.org/wiki/Routing_Information_Protocol)

The Routing Information Protocol (RIP) was one of the first routing protocols. It calculates the cost of sending data based on the number of hops required to reach the destination. This is similar to airline flights. A direct flight from Los Angeles to New York is a single hop. A flight from Los Angeles to New York that stops in Las Vegas and Denver would be three hops. So in theory, the direct flight should be fastest.

RIP is limited to 15 hops, so it is unsuitable for very large networks. However, it is simple to deploy and widely supported.

### [Open Shortest Path First (OSPF)](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)

The Open Shortest Path First (OSPF) routing protocol is common in large organizations. The protocol discovers the network topology surrounding, creates routing tables based on distance, bandwidth, and reliability. OSPF can detect changes and adapt automatically. OSPF is very performant and scales to large networks.

[Click here to compare RIP versus OSPF](http://resources.intenseschool.com/rip-vs-ospf-which-is-better-for-your-network/).

### [Hot Standby Router Protocol (HSRP)](https://en.wikipedia.org/wiki/Hot_Standby_Router_Protocol)

Hot Standby Router Protocol (HSRP) is not a routing protocol, but a way to make the default gateway fault-tolerant. Routing is an essential part of network communication, and a routing going offline can have severe consequences.

Configuring a Router
----------------------

In this example, we will have two networks. The "Ace" network has "alice", "amy", and "arouter". The "Blaster" network has "bob", "billy", and "brouter". The following lists the IP addresses of the five computers.

![Network Configuration](Simple-routing-instructions.png "Network Configuration")

### Step 1: Setup and Connect to a Linux Guest

* Copy the Vagrantfile for this exercise to a folder.
* Open a command prompt and navigate to the folder where you saved the Vagrantfile.
* Run `vagrant up` to bring up the machines.
    * Note that because six machines are defined in the Vagrantfile, any Vagrant command that does not target a specific machine will automatically target all machines. It will take a few minutes for this to run.

Note that *six* virtual machines will be created. The machines are named alice, amy, arouter, bob, billy, and brouter. You might be surprised that arouter and brouter are just regular virtual machines, but routers are basically just computers. Most router hardware strips away uneeded operating system functionality (like graphical user interfaces), but the underlying networking capabilities are equivalent to what you would find in any modern operating system.

### Step 2: Discover the Guest Network Configuration

The default Vagrant box comes preconfigured with networking capability. In this section, you will issue commands to discover what networking is enabled by default.

* Run `> vagrant ssh alice`
* Run `alice $ ifconfig`
    * eth1 will have the interface used for this exercise
    * eth0 exists so that your host machine can communicate with the guest
* sudo route del default


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

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

Every workstation, server, and router has a routing table. In windows, type the command `> route print` to list the routing tables. There will be separate tables for IPv4 and IPv6. Take a minute to look at the list.

![Windows Routing Table Entry](windows-route-table-entry.png "Windows Routing Table Entry")

The 0.0.0.0 network is the default network. If traffic is being routed to a network that is not listed in the routing table, it will be routed through the specified Gateway and Interface. In this example, my home router has the IP address 192.168.1.1. So if I try to access an IP address that my computer does not recognize as a local address, it sends it through my router and off to my internet service provider.

When I run `ipconfig` on my Windows workstation, I can see that my wireless network card has the IP address 192.168.1.244.

![Windows IP Config Output](windows-ipconfig.png "Windows IP Config Output")

There may be entries in your routing table to the same Network Destination but through different interfaces. Each interface can have a different Metric, and the computer will use this metric when deciding which interface to use.

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

Note that the diagram shows distinct cables connecting the devices. However, Vagrant essentially puts them all in the same physical space. The machines will have to be configured to appear like they are distinct physical networks.

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
* Run `alice $ tracepath 192.168.10.11`
    * `tracepath` comes with the default Ubuntu installation. It is similar to the `tracert` command in windows, or the `traceroute` command in other systems. The `tracepath` command shows the different hops or routes through a network that are required to reach a remote host.
    * This will attempt to find the path to amy. This should be successful since they are on the same network.
    * Because alice and amy are on the same subnet, no routing is required.
* Run `alice $ tracepath 192.168.10.5`
    * This should also be successful, since the internally facing interface of the router is on the same network.
* Run `alice $ tracepath 192.168.3.5`
    * This command will fail. The externally facing interface of the router is not on the same network. The command will fail at 10.0.2.2--your host machine. Your host machine does not know how to route the traffic to the appropriate network.
* Run `alice $ netstat -rn` to show the routing table.
    * You should see output like the screenshot below.
    * ![Alice Routing Table](netstat-alice-pre.png "Alice Routing Table")
* Run `alice $ sudo route add -net 192.168.3.0 netmask 255.255.255.0 gw 192.168.10.10`
    * sudo: runs the command in privileged mode
    * route: accesses the routing table
    * add: inserts a new entry
    * -net: specifies the network destination to add
    * gw: the local network interface to route through
* Run `alice $ tracepath 192.168.3.5` again
    * The command should succeed.
* Run `alice $ tracepath 192.168.20.11`
    * The command will fail.
* Open a new command prompt and SSH into arouter with `> vagrant ssh arouter`.
    * Run `sudo route add -net 192.168.20.0 netmask 255.255.255.0 gw 192.168.3.6`
        * This command tells the `a` router how to route traffic to the `b` network.

http://imranasghar.blogspot.com/2009/09/how-to-make-ubuntudebian-as-router.html

Arouter/Brouter:
sudo vi /etc/sysctl.conf
    * Uncomment "net.ipv4.ip_forward = 1"
sudo sysctl -p
sudo /etc/init.d/networking restart
sudo iptables -t nat -A POSTROUTING -o eth2 -j MASQUERADE

Alice:
sudo route del default
sudo ip route add default via 192.168.10.5
traceroute 192.168.20.5

brouter
vagrant ssh brouter
sudo ip route add -net 192.168.20.0 netmask 255.255.255.0 gw 192.168.20.5

sudo apt-get install inetutils-traceroute
    

### Step 5: Cleanup (Optional)

After submitting your work, you can destroy any boxes you used.

* Run "`$ exit`" to leave the SSH session. You will be back at your regular command prompt.
* Run "`> vagrant destroy`" to turn off the machine and delete it completely from your system. Answer "y" to confirm deletion.

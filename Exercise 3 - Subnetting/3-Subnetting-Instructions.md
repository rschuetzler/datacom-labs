Exercise 3: Subnetting
==========================

Like with cars, too much traffic causes congestion. Networks can be segmented to separate traffic. The segments are called subnetworks, or subnets. The subnet is defined by a subnet mask.

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Determine the subnet mask.
2. Change the subnet.
3. Explain how subnetting effects the ability of computers on a network to communicate.

Steps
--------------------------

### Step 1: Load the Preconfigured Vagrant File

Previously, when you have run the "`vagrant init ubuntu/Trusty64`" command, Vagrant automatically generated a file named "`Vagrantfile`" (with no extension). This file contains the configuratoin options for your virtual machine. For this exercise, a Vagrantfile has already been created.

* Copy the Vagrantfile for this exercise to a folder.
* Open a command prompt and navigate to the folder where you saved the Vagrantfile.
* Run `vagrant up` to bring up the machines.
    * Note that because two machines are defined in the Vagrantfile, any Vagrant command that does not target a specific machine will automatically target all machines.

Note that *two* virtual machines will be created. The machines are named "alice" and "bob."

### Step 2: Check Network Settings

* Run `> vagrant ssh alice` to connect to the first machine.
* Open a new Windows command prompt, navigate to the folder with your Vagrantfile, and run `> vagrant ssh bob` to connect to the second machine.
* Run `$ ifconfig` to check the IP address and subnet of each machine.
* Note that there are two ethernet connections. This lab will focus on `eth1`. This is a bridged connection that allows multiple guests virtual machines to communicate with each other. For the purposes of this exercise, you can pretend that `eth0` doesn't exist.
* Alice and Bob have different IP addresses, but they have they same subnet mask.
    * You need two pieces of information to determine if computers are on the same network (i.e. subnetwork): 1) the IP address, and 2) the subnet mask.

Subnet masks define the IP addresses for a subnetwork. Remember that IPv4 addresses are 4 numbers ranging from 0 to 255. Subnet masks are more limited. It is easiest to see how subnet masks are defined in binary. The subnet mask 255.255.255.0 is very common, and is represented in binary as 11111111.11111111.11111111.00000000. Subnet masks 

The ta

|Netmask notation | Binary Representation               | [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) | Hosts |
|-----------------|-------------------------------------|:----:|------:|
|255.255.0.0      | 11111111.11111111.00000000.00000000 | /16  | 65,533|
|255.255.255.0    | 11111111.11111111.11111111.00000000 | /24  | 254   |
|255.255.255.128  | 11111111.11111111.11111111.10000000 | /25  | 126   |
|255.255.255.240  | 11111111.11111111.11111111.11110000 | /28  | 14    |

You can calculate the number of hosts with a simple formula: (2^host bits)-2. So for the /28 subnet, there are 4 bits (i.e. 4 0's) for the host addresses. So we calculate 2^4-2=14. You can connect 14 computers on the /28 subnet. Each subnet has two reserved addresses--the [network address](https://en.wikipedia.org/wiki/Subnetwork#subnet_zero) and the [broadcast address](https://en.wikipedia.org/wiki/Broadcast_address).

Consider two computers in an organization that are both configured with a /28 subnet mask. Computer A has an IP address of 192.168.10.36. Computer B has an IP address of 192.168.10.42. Are these computers in the same subnetwork? We start by determining the number of IP addresses in each network. In the /28 network, 4 bits are reserved for hosts, the broadcast, and network address. So, 2^4 gives us 16 IP addresses reserved for each network. Next, we start with the base network.

The first 2 octets of the /28 subnet mask are all 255, so we know that all network addresses will begin with the first 2 octets of our IP addresses: 192.168. We know that the first network will end with a 0, which gives us a starting network address of 192.168.X.0. For X, we simply substitute the number of IP addresses per subnet--16. So, our first network address will be 192.168.16.0.

Network Address | 1st Valid Host | Last Valid Host | Broadcast Address
192.168.16.0    | 192.168.16.1   | 192.168.16.14   | 192.168.16.15

### Step 3: Test Connections Between Machines

* Run `alice$ ping 192.168.100.25`
    * You should see a *reply* showing how fast the reply was received.
    * The Linux ping utility has several options. Run `$ man ping` to read the user manual. Press `q` to quit reading the manual.
* On Linux, the ping command will keep running until it is stopped. Stop it by pressing `Control+c`.
* On your host machine, open a new command prompt and run `> ping 192.168.100.24`.
    * Note that on Windows, the ping stops after four replies.
    * Run `> ping -?` to see more ping options on Windows.

### Step 4: Change Bob's Subnet

Alice and Bob are currently on the same subnetwork, or subnet. Machines on the same subnet can communicate with each other directly. Communicating with machines outside of the subnet requires that communication to be *routed* to the appropriate network using a router.

* On Bob, run `bob$ sudo ifconfig eth1 192.168.200.25` to change the IP address. Note that this command will place the computer in a different subnet.
    * The command `sudo` is used here to run the command with "root" permissions. The root account in Linux is basically the administrator account that is allowed to make changes. Often, you can run commands that display information without elevated privileges, but to make changes, you must run commands as root by prefixing them with `sudo`.
    * Note that the same command (`ifconfig`) that you used to print network configuration can also be used to modify the network configuration.
* On Bob, run `bob$ ifconfig$ and verify that the IP address was modified.
* On Bob, ping Alice by running `bob$ ping 192.168.100.24`.
    * The ping will be successful.
* On Bob, run `bob$ sudo route del default` to delete the default gateway which will prevent routing between networks.
* On Bob, run `bob$ ping 192.168.100.24`.
    * The ping should fail. The computers are not on the same subnet, and there is no routing.
* On Bob, run `bob$ sudo ifconfig eth1 192.168.100.25` to restore the original IP address.
* On Bob, run `bob$ ping 192.168.100.24`.
    * The ping should succeed because Bob and Alice are on the same subnet and no routing is needed.
 
### Step 5: Cleanup (Optional)

After submitting your work, you can destroy any boxes you used.

* Run "`$ exit`" on Bob and Alice to leave the SSH sessions.
* Run "`> vagrant destroy`" to turn off the machines and delete them completely. Answer "y" to confirm deletion.

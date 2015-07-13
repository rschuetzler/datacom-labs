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

Previously, when you have run the "`vagrant init ubuntu/Trusty64`" command, Vagrant automatically generated a file named "`Vagrantfile`" (with no extension). This file contains the configuraton options for your virtual machine. For this exercise, a Vagrantfile has already been created.

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

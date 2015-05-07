Exercise X: Subnetting
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

1. Include Screenshot of an SSH session open with your virtual machine.
2. What is a virtual machine? (~100 words)
3. What is SSH? (~50 words)
4. What does the Windows PATH variable do? (~15-50 words)
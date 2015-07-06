Exercise 1: Vagrant Setup
==========================

This exercise will aid you in setting up and becoming familiar with Vagrant, VirtualBox, and SSH. You will use these tools throughout the course to learn networking and security concepts. 

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Setup a Linux virtual machine on your computer
2. Connect to a local virtual machine using SSH
3. Suspend a virtual machine
4. Destroy a virtual machine

Conventions
--------------------------
In these exercises, commands run from a Windows command prompt will be prefixed with ">", such as "`> cd ~`". The ">" should not be typed. Commands run in a Linux shell will be prefixed with "$", such as "`$ ls -al`". This notation will help you determine where to run the commands because you will frequently switch between your main computer and the virtual machines.

Steps
--------------------------

### Step 1: Download and Install VirtualBox

VirtualBox allows you to run multiple operating systems in sandboxed environments on your computer.

* Open https://www.virtualbox.org/wiki/Downloads
* Download the latest version of VirtualBox for Windows hosts (or your computer's primary operating system if it is not Windows)
* Install VirtualBox when the download completes

### Step 2: Download and Install Git for Windows

Git is a distributed source control application originally built to manage the Linux kernel. It comes with many helpful tools. The tool required for this exercise is SSH.exe. Other SSH applications exist for Windows (such as Putty.exe), but they do not integrte as easily with Vagrant.

* Open https://msysgit.github.io/
* Click "Download" and install the application once the download completes.

### Step 3: Configure your PATH environment variable

* Right-click on "Computer" and choose "Properties."
* Click "Advanced system settings"
* Click the "Environment Variables" button 
* Edit the PATH variable for your user account to add ";C:\\Program Files (x86)\\Git\\bin". The semi-colon separates entries, so make sure to add the semi-colon if your PATH variable was not empty.
* Click OK. If any command prompts are open, close them and re-open them. The PATH variable is read when the command prompt is first opened; it does not detect if any updates are made while it is running.

### Step 4: Download and install Vagrant

* Open http://www.vagrantup.com/downloads.html
* Install the Windows universal version (or the version that matches your computer's operating system if not Windows)

### Step 5: Setup an Ubuntu Virtual Machine

* Create a folder to store your Vagrant files (e.g. c:\\Users\\John\\Documents\\NetworkingClass\\Vagrant). 
* Open a command prompt and navigate to your Vagrant folder. (The folders that you use might be different based on the folder names on your computer.)
    * Click Start > cmd.exe [enter]
    * `> cd Documents\NetworkingClass\Vagrant`
* Create a new folder called "Exercise1"
    * `> md Exercise1` [enter]
* Navigate to the Exercise1 folder
    * `> cd Exercise1` [enter]
* Create a new virtual machine with the following command:
    * `> vagrant init ubuntu/trusty64` [enter]
* Start the virtual machine with the following command:
    * `> vagrant up` [enter]
    * Note that "ubuntu/trusty64" refers to a Vagrant box (i.e. template computer). If you have not already used this box, the box will be downloaded automatically. Depending on your Internet connection speed, this download may take some time.

Your Ubuntu virtual machine is now running. You will not see a graphical user interface (GUI) because by default, Vagrant virtual machines are "headless." There are ways to turn on the GUI, but for now it is not needed.

### Step 6: Connect to the Ubuntu Virtual Machine with SSH

Secure Shell (SSH) is a secure protocol for connecting to a remote machine to run commands.

* In your command prompt, run the following command in the Exercise1 folder:
    * `> vagrant ssh`
* You should see a connection made to the virtual machine similar to the following image.

    ![ssh screenshot](ssh-success.png "SSH Connection Screenshot")

* Connecting to a machine with SSH is commonly called an SSH session. You close your session when you disconnect.
* Take a screenshot of your own command prompt and copy it into a Word document.

### Step 7: Suspend, Resume, and Destroy

* Run "`$ exit`" to leave the SSH session. You will be back at your regular command prompt.
* Run "`> vagrant suspend`" to suspend your machine. Suspending the machine saves its running state to your hard drive and allows you to bring it up quickly.
* Run "`> vagrant ssh`". This should fail because the machine is not running.
* Run "`> vagrant up`" to bring the machine into a running state again.
* Run "`> vagrant ssh`". This should succeed.
* Run "`$ exit`".
* Run "`> vagrant destroy`" to turn off the machine and delete it completely from your system. Answer "`y`" to confirm deletion.

Submission
----------------------
Create a Word document with the following:

Heading:

  - Name
  - Date
  - Course
  - Exercise 1

Questions

1. Include Screenshot of an SSH session open with your virtual machine.
2. What is a virtual machine? (~100 words)
3. What is SSH? (~50 words)
4. What does the Windows PATH variable do? (~15-50 words)

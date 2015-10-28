Exercise 8: Troubleshooting
==============================

It is often necessary to troubleshoot network configurations. This lab will present several scenarios and ask you to think about what could be causing the problems.

Prerequisites
--------------------------
A knowledge of fundamental networking concepts such as IP addressing, routing, DHCP, and DNS are assumed.

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Explain general troubleshooting steps.
2. Use software tools to help diagnose problems.
3. Fix common networking issues.

Troubleshooting Overview
--------------------------
Troubleshooting networking problems or just about any other computer problem boils down to a few key questions:

1. What is the problem?
2. What elements of the system could be causing the problem?
3. What do I know about the elements that could be causing the problem?
4. How can I find out more about the elements that could be causing the problem?

In general, troubleshooting should start with the assumption that something on your end is broken. When you can confirm that your computer is configured properly, the scope of investigation should proceed to the next hop in the network--such as a switch. By starting locally then proceeding outward, you can ascertain the point of failure.

The following scenarios demonstrate a few common networking problems and provide some guidance on how they can be resolved. Each of these represents an actual networking problem.

Scenario 1
--------------------------

You just installed Windows 10 on a brand new computer. The computer boots up and you launch a web browser. When you try to go to yahoo.com, you see an error message similar to the following:

&nbsp;![Error Message](disabled-error-internet-disconnected.png)

You get the same error message when going to different websites.

What network settings do you check? In the Windows world, you can run `ipconfig` to check basic network connectivity. In Linux or Mac OSX, you would run `ifconfig`. Suppose we saw the following `ipconfig` output in Windows. What does this information tell you?

&nbsp;![IPConfig Output](disabled-ipconfig.png)

It is an Ethernet adapter, which tells us that we should be looking for a plugged in connection. What do you check next?

It would be important to view the cable to see if it is plugged in properly. A loose cable might be causing the issue. Sometimes, the RJ-45 connections can become damaged, causing cables to slip out. Suppose that you check the cable and it is plugged in properly. However, there are no lights blinking. What does this information tell you?

In Windows, it is often important to check the `Network Connections` in the Control Panel. Suppose you view your Network Connections and see the following output. What does this tell you?

&nbsp;![Network Connections](disabled-network-connections.png)

The `Local Area Connection` is disabled. It can be enabled by right-clicking on the adapter, and choosing `Enable`.

&nbsp;![Network Connections](disabled-enable-network-connections.png)

After enabling the network interface, will you immediately be able to connect to the Internet? What processes must take place before a successful connection?

If the adapter is configured to acquire IP configuration settings through DHCP, it can take a few seconds to obtain an IP address and other network configurations. After about 10 seconds, you should be able to open a web browser and connect to the Internet (assuming that a  disabled network adapter was your only problem).

Scenario 2
-----------------------------

You are able to browse most of the web just fine. Yahoo.com works, cnn.com loads reasonably well, but for some reason when you go to Netflix.com your browser just hangs.

1. What is the problem? A single website (Netflix.com) is not loading in the web browser. When defining the problem, it is good to be as specific as possible.

2. What elements of the system could be casuing the problem?
  - Your ISP might have blocked Netflix.
  - Netflix may have taken the service down for maintenance.
  - The DNS lookup for Netflix might have failed.

3. What do I know about the elements that might be causing the problem.
  - It is unlikely that the ISP would be blocking Netflix. Some service providers throttle traffic to limit bandwidth to particular sites, but it would be unusualy for an ISP to outright block traffic. Only if all other troubleshooting steps failed, you might call the ISP and ask specifally about Netflix.
  - Netflix might not be working. Because you do not have direct access to the Netflix servers, we would want to check if Netflix is working for other people.
  - If DNS is not resolving, we will not be able to get to the website. However, DNS appears to be resolving other websites fine.

There are a few ways to gather information about websites. A basic test that can provide useful information is `ping`. The following screenshot shows the output from pinging Netflix.com. By default, Windows sends four ping requsts and records the response.

&nbsp;![Ping Netflix](websitedown-ping.png)

Notice that in the screenshot, the requests timed out. This means that the Netflix server did not response to the pings. For security reasons, some services block ping requsests, so a failed ping does not necessarily mean that the website is down. The ping output shows us that the website netflix.com resolved to the IP address 75.101.139.66. This gives us some assurance that DNS resolution is working properly.

The website http://downforeveryoneorjustme.com/ allows you to enter a website and check if it is accessible from another location.

&nbsp;![Website Checking Tool](websitedown-forallorjustme.png)

If the website is down, then it is probably not a configuration problem on your computer nor an ISP issue. If the website is down for multiple people in different locations, the web server is probably down for everybody. All you can do is wait for the website to restore its service.

Scenario 3
-----------------------

You bring your laptop to the Rotary Club to give a presentation. The Rotary Club allows guests to connect to its WiFi using the password `Pioneer47`. During your presentation you want to show some YouTube videos that you failed to download ahead of time. You connect to the local access point, enter the password, and appear to connect successfully. However, when open your web browser and navigate to youtube.com, the page just hangs and eventually times out. Other people who brought their laptops are able to connect to youtube.com just fine.

What steps do you use to troubleshoot the problem? Options that you might consider are:
  - Loading another website using the domain name (e.g. yahoo.com). What would the outcome of this test tell you?
  - Loading another website using an IP address. What would the outcome of this test tell you?

Assume that loading a different website using the domain name fails, but loading the website via an IP address works. What settings on your computer would you check next?

Looking at the IPv4 configuration, you see the following.

&nbsp;![IP Configuration](googledns-control-panel-ip-config.png)

What do you notice about the DNS settings? What is 8.8.8.8 and 8.8.4.4? Search the Internet if you are unfamiliar with these IP addresses.

Some organizations filter content by DNS. So if you tried to go to poker.com, the DNS server would recognize that site as a gambling site and instead of returning the IP address to the site, it redirects you to a web page telling you that the site is prohibited. These organizations may block DNS lookups to other DNS services to make it more difficult to circumvent their content filtering. By changing your DNS settings to 'Obain DNS server addres automatically,' you would likely be able to connect to websites using a friendly domain name.

Scenario 4
--------------------

In this scenario, you are attempting to expand your network. You began with `Configuration A` which allowed the single computer to access the Internet. In `Configuration B`, an unmanaged switch was connected to common home wireless router. In both configurations, Client A is able to connect to the Internet. However, Client B and Client C are unable to connect to the Internet. Examine the network toplogies in the following figure.

&nbsp;![Network Toplogies](badcable-topology.png)

How would you approach troubleshooting this network connectivity problem?

Here are some steps that you might consider investigating and the results. Think critically about what each piece of information tells you.

  - You check Client B and Client C and they are configured to obtain network settings via DHCP.
  - You run `ipconfig` and find the following IP addresses:
    - Client A: 192.168.0.50/24
	- Client B: 169.254.12.188/16
	- Client C: 168.254.165.122/16
  - You ping Client B from Client C and the pings are successful.
  - Client A can ping 192.168.0.1 and has obtained its network settings from the router.
  - The unmanaged switch and the ports on the wireless router should be able to reach speeds of 1000mb/s.
  - The port on the unanaged switch that is connected to the wireless router shows a blinking amber light. The ports on the unmanaged switch that connect to Client B and Client C have blinking green lights.
  - The unmanaged switch supports MDIX.

The solution to this real-world problem had to do with hardware. The cable that connected Client A to the wireless router in Configuration A was bad, but not bad enough to stop working completely. Client A was able to continue working with the cable. In Configuration B, the same cable was used to connect the unmanaged switch to the wireless router. The unmanaged switch had a lower tolerance for the degraded cable. The strongest clue that the cable was a problem was the fact the blinking amber light, indicating that the switch could not negotiate a faster connection. Replacing the cable resolved the problem, and Client B and Client C could connect to the Internet without any issues.

Scenario 5
----------------------

Ever since your roommate started using your computer, your Internet started to slow down. Websites take forever to load, the computer takes longer to open programs, and everything just feels slower. You roommate swears that he didn't change anything, but you're not sure if you believe him.

If everything is working correctly, but things are just going slow, what could the problem be? Here is a partial list of things that might cause a slow-down:
  1. WiFi interference
  2. Degraded network cable
  3. Degraded ISP performance
  4. Malware

If you are conneting to the Internet wirelessly, your neighbors' wireless routers might be sending signals that overlap with your own wireless router. You might consider changing the WiFi channel to see if that improves performance.

If you want to rule out a degraded cable as an issue, choose another cable and test your speed again. http://www.speedtest.net/ is a website that tells you how fast your internet connection is. You can run the test multiple times with different cables to see if changing the cable makes a difference.

&nbsp;![Bandwidth Test](slow-bandwidth-test.png)

It can also be good to run a bandwidth test before and after power cycling your wireless router.

If the cable is a problem, the ISP might be the issue. An ISP can send a `reset` command to your cable modem which sometimes can solve minor issues. This is similar to rebooting your computer. The ISP can also tell you if they are experiencing any problems with their own systems.

If your computer has malware, the malicious software may be consuming your bandwidth and computer processing power. The `netstat` utility shows TCP/IP connections on your computer. The following screenshot shows a sample output from the netstat command.

&nbsp;![Netstat Output Showing TCP/IP Connections](slow-netstat.png)

Pass additional parameters to see the process (i.e. program) that is making the TCP/IP connection.

&nbsp;![Netstat Output Showing TCP/IP Connections](slow-netstat-ano.png)

Suppose I want to see what process #228 is. In Windows, this can be done in the task manager. Right-click on the task bar, then click 'Task Manager.' To show PID (process identification), right click in the task manager header and ensure that 'PID' is checked. Suppose I was curious was process #228 was. I can see in my task manager that process #228 is Dropbox, and I am fine with Dropbox opening TCP/IP connections on my computer.

&nbsp;![Task Manager](slow-task-manager.png)

If you think you have a virus on your machine, you can also download a program like Malwarebytes (found at https://www.malwarebytes.org/) and do a complete scan of your system. Many computer repair shops charge hundreds of dollars just do download Malwarebytes and run a scan on your machine.

Firewall Setup in Ubuntu Server
=====================================

Ubuntu uses the Netfilter subsystem to filter packets. To learn more about the way Ubuntu manages its firewall, refer to their [server guide](https://help.ubuntu.com/14.04/serverguide/firewall.html). In the first part of this exercise, you will setup Ubuntu host-based firewall rules. In the second part, you will configure IP masquerading to turn the server into a network-based firewall.

Prerequisites
---------------------
1. Vagrant installed and properly configured


Ubuntu Server Virtual Machine Creation
---------------------------------------

Run the following commands to create an Ubuntu server virtual machine and connect to it through SSH.

```
> vagrant init ubuntu/Trusty64
> vagrant up
> vagrant ssh
```

Run the following command to elevate to root privileges.

```
$ su -
```

Note that the command prefix in your shell now ends with `#`.

You should see output similar to the following screenshot.


Host-Based Firewall Configuration
---------------------------------

1. Run the following command to enable the "uncomplicated firewall" service.

```
# ufw enable
```

Type `y` to confirm that you want to enable the firewall. Note that if the default firewall rules bocked port 22, enabling the firewall would immediately terminate your SSH session and prevent you from connecting via SSH in the future.

Note that you will receive a message warning you that turning on the firewall may interrupt ssh connections. If port 22 were blocked in the firewall configuration, the current ssh session would be terminated. Fortunately, port 22 is not blocked by default.

Run the following ufw command to see the status of the firewall rules.

```
# ufw status verbose
```

2. Run the following command to open a port (web traffic in this example).

```
# ufw allow 80
```

Check the status again by running the following command.

```
# ufw status verbose
```

Ubuntu uses ufw to manage the firewall rules, but it uses iptables as the actual firewall. Run the following command to see the iptables output. You may need to expand your command window to avoid line wrapping.

```
# iptables -L
```

3. Run the following command to close a port (port 53 for DNS in this example).

```
# ufw deny 53
```

4. Run the following command to delete a firewall rule:

```
# ufw delete deny 53
```

5. Run the following command to allow SSH access from 192.168.2.1 to any IP address on the server.

```
# ufw allow proto tcp from 192.168.2.1 to any port 22
```

6. Run the following command to allow SSH access from any IP address on the 192.168.2.0/24 subnet.

```
# ufw allow proto tcp from 192.168.2.0/24 to any port 22
```

7. Use the "--dry-run" option to list the firewall rules without applying them.

```
# ufw --dry-run allow smtp
```

8. To check the status of the firewall, run the following command:

```
# ufw status
```

![Firewall Status](status.png "status")

9. Run the following command to disable the firewall.

```
# ufw disable
```

10. Enable the firewall again.

11. Turn logging on:

```
# ufw logging on
```

12. Turn logging off:

```
# ufw logging off
```

### Configuring the Firewall for Applications


Many applications help the operating system determine the firewall rules needed to make them work properly.

1. Run the following command to see which applications have installed a profile.

```
# ufw app list
```

You should see output similar to the following figure.

![Application List](application-list.png "application-list")

2. Run the following command to add a registered application's firewall rules to the current firewall rules.

```
# ufw allow OpenSSH
```

3. Run the following command to see the ports, protocols, and other settings defined for applications.

```
# ufw app info OpenSSH
```

![OpenSSH Firewall Rules](openssh.png "openssh")

4. If you want to allow OpenSSH connections from a range of IP addresses, use the following command:

```
ufw allow from 192.168.2.0/24 to any app OpenSSH
```

Exercise
-----------------------------------
Modify the firewall rules so that the following requirements are satisfied:

  - HTTP traffic is allow from anywhere.
  - DNS traffic is blocked.
  - Port 22 is open from anywhere on the 10.0.0.0/8 network

Delete and add rules as necessary.

Network-Based Firewall
-------------------------------------
A host-based firewall protects a single machine on the network. A network-based firewall filters traffic to protect other machines on the network. For a device to server as a network-based firewall, IP masquerading must be configured. At a high level, IP masquerading ensures that private IP addresses can be routed to public IP addresses.

Several Ubuntu configurations must be updated to allow IP masquerading.

1. Edit /etc/default/ufw by running the following command.

```
# nano /etc/default/ufw
```

Change "DEFAULT_FORWARD_POLICY" TO "ACCEPT".

2. Edit /etc/ufw/sysctl.conf

```
# nano /etc/ufw/sysctl.conf
```

  - Uncomment "net/ipv4/ip_forward=1" by deleting the "#" at the beginning of the line.
  - Uncomment "net/ipv6/conf/default/forwarding=1" by deleting the "#" at the beginning of the line.
  - Save the file and exit.

3. Edit /etc/ufw/before.rules

```
# nano /etc/ufw/before.rules
```

Type the following text at the top of the file:

```
# nat Table rules
*nat
:POSTROUTING ACCEPT [0:0]

# Forward traffic from eth1 through eth0.
-A POSTROUTING -s 10.0.2.0/24 -o eth0 -j MASQUERADE

# don't delete the 'COMMIT' line or these nat table rules won't be processed
COMMIT
```

4. Run the following command to reload ufw and apply the changes.

```
# ufw disable && ufw enable
```

Cleanup
----------------------------

Exit from the ssh session and run `vagrant destroy` to delete the virtual machine when you are finished.
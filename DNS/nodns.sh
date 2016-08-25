#!/bin/bash
echo 'echo "supersede domain-name-servers 127.0.0.1;" >> /etc/dhcp/dhclient.conf' | sudo -s
sudo shutdown -r now

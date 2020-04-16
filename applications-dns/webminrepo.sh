#!/bin/bash
# sudo ln -nsf ../run/resolvconf/resolv.conf /etc/resolv.conf
wget -qO- http://www.webmin.com/jcameron-key.asc | sudo apt-key add
sudo add-apt-repository "deb http://download.webmin.com/download/repository sarge contrib"
sudo apt update

#!/usr/bin/env bash

apt-get update
apt-get install -y wireshark

chmod 4711 `which dumpcap`

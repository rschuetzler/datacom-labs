#!/usr/bin/env bash

apt-get update
apt-get install -y tshark

chmod 4711 `which dumpcap`

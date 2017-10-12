#!/usr/bin/env bash


yum -y update
yum -y install yum-utils groupinstall development https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u python36u-pip python36u-devel


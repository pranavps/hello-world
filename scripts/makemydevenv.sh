#!/bin/bash
# Script that sets up all dev packages and environments on linux machine
set -eux
# git

# vim
# "Development tools"
yum groupinstall "Development Tools"
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u
python3.6 -V
yum -y install python36u-pip
yum -y install python36u-devel

# python
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar -xJf Python-3.7.3.tar.xz
cd Python-3.7.3
./configure
make
make install
 
# pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

# Django
pip install django
# Copy scripts from github
# 

# yum update -y
yum update -y

set +eux

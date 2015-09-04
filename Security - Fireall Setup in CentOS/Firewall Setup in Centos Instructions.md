



1. Open a command prompt in a new folder.
2. Run `> touch Vagrantfile` to create an empty file with no extension.
3. Put the following text in the Vagrantfile:

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.define "myfirewall" do |myfirewall|
    myfirewall.vm.box = "puppetlabs/centos-7.0-64-puppet"
    myfirewall.vm.host_name = "myfirewall"
    myfirewall.vm.network "private_network", ip: "192.168.20.5"
    myfirewall.vm.network "private_network", ip: "192.168.3.5"
    myfirewall.vm.box_check_update = false
  end
  
end
```

4. Save the Vagrantfile then run:

```
> vagrant up
> vagrant ssh
```

5. In your Linux console, run the following command to elevate permissions:

```
sudo su -
```

3. Follow the steps outlined in https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-7 to setup your firewall.
  - Note: Your inteface names will be different. Run `$ ifconfig` to see their names.
  - Do not restart the firewalld.service. VirtualBox networking can cause problems recognizing all interfaces.

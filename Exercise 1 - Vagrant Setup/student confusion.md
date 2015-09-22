Ryan
-----

* Didn't have enough space allocated in a Windows Bootcamp partition to complete the lab
  in Windows. Give an estimate (~10GB free?) for how much space will be required so they
  can be sure they have enough.
* Git path to add to %PATH% needs to be fixed to specify either the 32 or 64 bit versions
    * For some reason, one recent version of Git did not install ssh.exe or any
	of the other typical command-line tools. Need to double-check the steps to
	make sure the steps we have will get that installed
* Bad timing on Windows 10 release. Virtualbox not officially supported, so we just had to
  hope it worked. Thankfully it did without too much trouble. It could have been nasty if
  class had started just 2 weeks earlier. Hopefully Microsoft doesn't do anything like
  that next year.
* Add instructions to make sure your computer doesn't go to sleep during VM download
  (vagrant up). Apparently Macs at least don't detect that the download is happening and
  still go to sleep as usual.
* Be more explicit about the options to select when installing Git. It has some fancy
  terms in there, and newbies may not be comfortable with it.

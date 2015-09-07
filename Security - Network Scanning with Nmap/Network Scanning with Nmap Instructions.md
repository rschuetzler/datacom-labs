Network Scanning with Nmap Instructions
========================================


Learning Objectives
-------------------------------
By the end of this lesson, you will be able to:

1. Perform basic network scanning with Zenmap (an nmap front-end).
2. Understand basic nmap command line options.

Installation
----------------------------------
Download Zenmap from https://nmap.org/zenmap/. Zenmap will install nmap. Zenmap is a graphical user interface that uses nmap under the hood to perform network scanning.

First Scan
-----------------------------------
1) Launch Zenmap.
2) In the target, enter "scanme.nmap.org". (No quotes.)
  - The command text box will show "nmap -T4 -A -v scanme.nmap.org"
3) In profile, keep the "Intense Scan" option.
4) Slick Scan.
  - The scan can take a minute to run.
5) Look at the output in the Nmap Output tab.
  - Examine the different tasks that nmap completed.
6) Examine the Ports/Hosts tab.
7) Examine the topology tab.
8) Examine the Host Details tab.
9) Examine the Scans tab.
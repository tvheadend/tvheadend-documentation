##Install The Tuner Hardware

This section will give you some basic ideas on how to get your tuner working with your operating system. However,
it's clearly way beyond the scope of this guide to tell you everything: consult specialist forums, search around, 
and at least do some research to work out what's likely to work or not before you hand over any money.

####1. Install the tuner hardware

This is obviously a core requirement that's outside of the scope of this guide

You basically have the choice of:

* External USB tuners that plug in

* Internal (e.g. PCI) tuners that go inside the computer chassis

* External SAT>IP tuners that send their decoded signals over a LAN connection. 

Follow the appropriate installation instructions and, if relevant, the setup instruction (e.g. for SAT>IP, which are effectively small, standalone computers).

####2. Install the tuner firmware and/or drivers

Similar to the above, tvheadend can do nothing if your tuners aren't working properly. A good place to check how to set up your tuners is the linuxtv wiki - this will not only tell you what's supported under Linux, but also how to get it all working:

[LinuxTV wiki device library](http://www.linuxtv.org/wiki/index.php/Hardware_Device_Information)

Many tuners require firmware - normally, a binary file that's been extracted from the proprietary drivers used by Windows. Many Linux distros include a package for the most common devices (e.g. linux-firmwares under Ubuntu or firmware-linux-nonfree under Debian). If this isn't sufficient, a good source of firmware files is the OpenElec git repository:

[OpenElec firmware library](https://github.com/OpenELEC/dvb-firmware)

Typically, you would download the binary file and install it into `/lib/firmware`, owned by `root:root`, permissions `rw-r--r--` (0644)


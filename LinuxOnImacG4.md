<h1> Notes on getting Lubuntu to USB boot on an old mac iMac G4</h1> 

This would likely work for most iMacs of the early 2000s era

<b>the main steps will are as headers for easy and quick access and less talking</b>

<h2> Step 1: Getting Linux to boot </h2>
<h3> Lubuntu and USB</h3>
This proved to be more difficult than anticipated. A PowerPC architecture compliant version of Linux (Lubuntu) was found <h3><a href="https://forums.macrumors.com/threads/lubuntu-16-04-remix-updated.2204742/">here</a></h3>. Downloading this from the forum posts linked google drive, a suitable 8 Gb usb was found and formatted using <h3>Rufus (https://rufus.ie/en_US/)</h3>. Once this USB was ready to go it was plugged into the iMac. 

\* the reason a USB boot is needed is because the harddrive and CD drive had been removed and used for parts (see HardWare hacking post for context)

From here there are a few potential paths forward. Booting the device and pressing and holding the option key should bring up the "boot picker" which will allow you to select the drive you boot from... This never worked on the tested machine it would get stuck on the boot picker screen and not accept any input. But results may vary depending on the rig.

Next option is to boot the device with Open Firmware mode. this involves presing <h2>command option O F on startup</h2>. It should bring up a termional and say open firmware mode. More info on open firmware here (http://www.firmworks.com/QuickRef.html)

Once here, the usb port that the newly formatted usb drive is plugged into must be found. (commands in bold are written <i>exactly</i> as they need to be typed)

running <h2><b>dev / ls </b></h2> lists all devices that are connected (should see things like the wifi card any ROM connected and so on) in this case the USB devices are desired. The formatted device should have some disk@1 or disk@2 as a directory inside. This should be the desired drive. Alternatively if the exact port the usb was plugged into is known or can be easily found then this could be used. 

The desired drive will be listed as something like usb@18 or similar this is the internal naming to find the naming needed to boot from it the command <h2><b>devalias</b></h2> can be used and the names matched.

now we want to set this to be the boot for every time the device startsup. to do this the command <h2><b>setenv boot-device usb0/disk@2:,\\\\yaboot</b></h2> obviously replacing the usb and disk name to match 


then <h2><b>boot usb0/disk@2:,\\\\yaboot</b></h2> can be run to boot into linux. It will take a minute or so to boot and might ask for a keystroke to start.

Linux should now be working and it runs reasonably well on the G4. 

<h1>Step 2: WiFi</h1>

Included in the scripts folder of the repo is a wifiSetup.sh file that contains the commands that were succesful on the tested machine to get it to connect to a local network. 

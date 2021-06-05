sudo ifconfig wlan0 down
sudo service network-manager stop
sudo ifconfig wlan0 up
wpa_passphrase YOURSSIDHERE YOURPASSWRDHERE | sudo tee /etc/wpa_supplicant.conf
sudo wpa_supplicant -c /etc/wpa_supplicant.conf -i wlan0 -B
sudo dhclient wlan0
dig google.com 

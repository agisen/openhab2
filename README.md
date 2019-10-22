# rapi_weather
A Raspberry Pi weatherstation using openHAB2 and SHT75s to monitore temperature &amp; humidity
or
how to display the temperature & humidity values of up to two SHT75 sensors connected to a Raspberry Pi on your browser.

## Prerequisites
### Installation from scratch
1. Install openHAB 2:
  * Go to https://www.openhab.org/download/
  * Package Installation is the most convienent way
  * Navigate with a web browser to http://<ip-address-of-pi>:8080/paperui/index.html#/extensions
  * Install the following extensions:
    * Look in „Binding“ for  „Exec Binding“
    * Look in „Persistence“ for „RRD4j Persistence“
    * Look in „Transformations“ for „RegEx Transformation“
  * Copy the files from https://github.com/agisen/rapi_weather to the corresponding folders in /etc/openhab2/
  * Ensure ownership of these files, especcially make the scripts excecutable:
    * sudo chmod +x /etc/openhab2/scripts/sht.py
  * To make openHAB automatically start after booting the Linux host
  `sudo systemctl daemon-reload`
  `sudo systemctl enable openhab2.service`

### Software already running
The SHT sensors must be connected to the correct pins of the Raspberry Pi, as these are hard-coded. These are:
  * GPIO14 (SKT) & GPIO4 (DATA) for the first sensor
  * GPIO8 (SKT) & GPIO11 (DATA) for the second sensor

Use 3.3V for VDD and GND for GND.

## Usage
The IP address of the Raspberry Pi must be available. The measured values are displayed at <Raspberry IP>:8080/basicui/app?sitemap=weatherstation

## Troubleshooting
  * Rasberry Pi pin assignment can be displayed via `pinout`
  * The openHAB log can be displayed via `tail -f /var/log/openhab2/openhab.log -f /var/log/openhab2/events.log`
  * OpenHAB can be restarted via `sudo systemctl restart openhab2.service`

### How to obtain the IP adress of a device using DHCP
* If its the only Pi in the network, you can try with `ping raspberrypi.local`
* Use nmap for port scanning
  * Unplug the network cable of the device
  * Use nmap for port scanning. You should restrict it to a specific subnet ("/24").
  * Plug the network cable
  * Use nmap for port scanning
  * A comparison now shows the IP address
      ```bash
      nmap -n -v -oG - -sn 129.217.167.0/24 > 1.txt
      nmap -n -v -oG - -sn 129.217.167.0/24 > 2.txt
      diff 1.txt 2.txt
      rm 1.txt 2.txt
      ```


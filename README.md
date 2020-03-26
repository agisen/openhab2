# openHAB2-git
This repo contains files to create a Raspberry Pi weatherstation using openHAB2 and DHT22 sensors to monitore temperature &amp; humidity and to display the temperature & humidity values of up to two sensors connected to a Raspberry Pi on your browser.
SHT75s are also supported, but may require some adjustements.

## Prerequisites
### Software
  * Git
  * Java (von OpenHAB benötigt):
    * testen ob vorhanden: `java -version`
    * Installation (Java 8): `sudo apt install openjdk-8-jdk`
  * pip
  * Adafruit_Python_DHT for python
    * `sudo pip3 install Adafruit_DHT`

### Installation from scratch
1. Install openHAB 2:
  * Go to https://www.openhab.org/download/
  * Package Installation is the most convienent way
2. Navigate with a web browser to http://<ip-address-of-pi>:8080
  * "First-time setup" shows, go for "Standard"
  * Go to "Paper UI" -> "Addons" (http://<ip-address-of-pi>:8080/paperui/index.html#/extensions)
3. Install the following extensions:
  * Look in „Binding“ for  „Exec Binding“
  * Look in „Persistence“ for „RRD4j Persistence“
  * Look in „Transformations“ for „RegEx Transformation“
4. Copy the files from https://github.com/agisen/openhab2-git to the corresponding folders in /etc/openhab2/. Step by step:
  * `cd /etc/`
  * `sudo git clone https://github.com/agisen/openhab2-git.git`
  * `sudo mv openhab2-git/.git openhab2/.git`
  * `sudo rm -rf  openhab2-git`
  * `cd openhab2/`
  * `sudo git reset --hard origin/master`
5. Ensure ownership of these files, especcially make the scripts excecutable:
  * sudo chmod +x /etc/openhab2/scripts/dht22.py
  * sudo chmod +x /etc/openhab2/scripts/sht.py
6. Ensure GPIO-access for openhab:
  * `sudo adduser openhab gpio`
7. Start openHAB with `sudo systemctl start openhab2.service`
8. Make openHAB automatically start after booting the Linux host
  * `sudo systemctl daemon-reload`
  * `sudo systemctl enable openhab2.service`

### Software already running
The sensors must be connected to the correct pins of the Raspberry Pi, as these are hard-coded. These are:
  * For the SHTs:
    * GPIO24 (DATA) for the first sensor
    * GPIO17 (DATA) for the second sensor
  * For the SHTs:
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


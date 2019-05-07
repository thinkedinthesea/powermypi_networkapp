# POWERMYPI_NETWORKAPP
Python script that interact with **POWERMYPI** Android app<br/><br/>
[Link to the App on Play Store](https://play.google.com/store/apps/details?id=com.thinkedinthesea.powermypi)<br/>

****
Take control of your Raspberry Pi board. <br/>
Send command to your RPI or whatever *NIX board.<br/>
Power Off, Reboot and 4 customizable commands.<br/><br/>
# Istructions for the Server part:<br/>
Open a terminal on your RPi:<br/>
cd /home/pi<br/>
git clone https://github.com/thinkedinthesea/PowermyPi-UNO.git<br/>
cd PowermyPi-UNO<br/>
chmod u+x install.sh<br/>
sudo ./install.sh 3<br/><br/><br/>

- **Now insert IP and Port on the Android App and enjoy**<br/><br/>
# Changing Default Port:<br/>
- Open a terminal<br/>
```
cd /home/pi/powermypi_networkapp
nano powermypi_networkapp.py
```
- Scroll down to the line 20 ```myPort=1234``` and change to any unused port<br/>
- Once you've added that line, press ```control-x```, ```y``` and ```enter``` to exit nano.<br/>
- Reboot for changes to take effect.<br/>

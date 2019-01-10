# POWERMYPI_NETWORKAPP
Python script that interact with **POWERMYPI** Android app<br/><br/>
[Link to the App on Play Store](https://play.google.com/store/apps/details?id=com.thinkedinthesea.powermypi)<br/>

****
Take control of your Raspberry Pi board. <br/>
Send command to your RPI or whatever *NIX board.<br/>
Power Off, Reboot and 4 customizable commands.<br/><br/>
# Istructions for the Server part:<br/>
- Open a terminal<br/>
```
cd /home/pi
git clone https://github.com/thinkedinthesea/powermypi_networkapp.git
cd powermypi_networkapp
chmod 777 powermypi_networkapp.py
sudo crontab -e
```
- At the end of file insert this line<br/>

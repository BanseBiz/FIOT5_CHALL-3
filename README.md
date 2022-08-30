## Steps for setting up the Pi

1. Using a clean install of the raspbian OS (we recommend using the [Raspi installer](https://www.raspberrypi.com/software/) to make it easy to install )

2.  After enabling SSH and configuring the wifi using `wpa_supplicant.conf` install RaspAP to setup the pi as an access point

```bash
curl -sL https://install.raspap.com | bash
```

3. These are the default credentials you get after installing RaspAP
   - **IP address:** 10.3.141.1
   - **Username:** admin
   - **Password:** secret
   - **DHCP range:** 10.3.141.50 — 10.3.141.255
   - **SSID:** raspi-webgui
   - **Password:** ChangeMe

You can also use [our raspberry pi image]() to skip the steps above.

 `IP address: 192.168.0.152`

**SSH** 
`user` fiot5
`password` fiot5!

**AP**

`IP address` 10.3.141.1

`SSID` raspi-webGUI
`password`  ChangeMe

## Steps for Dashboard

1. Update the pi

```bash
sudo apt update -y && sudo apt upgrade -y
```

2. Install python3-pip

```bash
sudo apt install python3-pip
```

3. Install python dependencies (Pandas is optional)

```bash
sudo apt install python3-plotly python3-pandas
pip3 install dash 
```

IF you get an warning like this: : “The scripts  xxx are installed in ‘/home/pi/.local/bin’ which is not on PATH.” 
Use the following commands, which create a backup of your  environment variable and then add the required path according to your user:

```bash
sudo cp /etc/environment /etc/environment.backup
sudo sed -i 's|PATH="|PATH="\/home\/'"$USER"'\/.local\/bin:|g' /etc/environment
```

4.  Run the dashboard app using:

```bash
python3 app.py
```


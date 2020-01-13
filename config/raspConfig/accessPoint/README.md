- Step 1
######    sudo apt-get install dnsmasq hostapd
- Step 2 
###### sudo nano /etc/dhcpcd.conf
		denyinterfaces wlan0
- Step 3 
######  		sudo nano /etc/network/interfaces
		allow-hotplug wlan0
		iface wlan0 inet static
		address 192.168.1.2 # wanted ip
		netmask 255.255.255.0
		network 192.168.1.1
		broadcast 192.168.1.255
- Step 4 
######     sudo nano /etc/hostapd/hostapd.conf
        interface=wlan0
        driver=nl80211
        ssid=Raspberry-AP # Network name
        hw_mode=g
        channel=6
        macaddr_acl=0
        auth_algs=1
        ignore_broadcast_ssid=0
        wpa=2
        wpa_passphrase=raspberry # Network password
        wpa_key_mgmt=WPA-PSK
        rsn_pairwise=CCMP
- Step 5 
###### 	sudo nano /etc/default/hostapd
		- DAEMON_CONF="/etc/hostapd/hostapd.conf" # Edit line 'DAEMON_CONF'
- Step 6 
###### 	sudo nano /etc/dnsmasq.conf
		interface=wlan0
		listen-address=192.168.1.2 # same ip from step 2
		bind-interfaces
		server=8.8.8.8
		domain-needed
		bogus-priv
		dhcp-range=192.168.1.120,192.168.1.254,12h
- Step 7 
###### 	sudo nano /etc/sysctl.conf
		uncomment line  'net.ipv4.ip_forward=1'
- Step 8 
###### 	sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
###### 	sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
###### sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
- Step 9 
###### 	sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
- Step 10 
###### 	sudo nano /etc/rc.local
		iptables-restore < /etc/iptables.ipv4.nat
		/usr/sbin/hostapd /etc/hostapd/hostapd.conf
		service ssh restart

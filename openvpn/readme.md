# OpenVPN Server Installation and Configuration Guide

## Prerequisites
Ensure your system is up to date:
```bash
sudo apt update
sudo apt upgrade -y
```

## Install OpenVPN and Easy-RSA
```bash
sudo apt install openvpn easy-rsa -y
```

## Set Up the Public Key Infrastructure (PKI)
```bash
mkdir ~/easy-rsa
ln -s /usr/share/easy-rsa/* ~/easy-rsa/
cd ~/easy-rsa
./easyrsa init-pki
```

### Build Certificate Authority (CA)
```bash
./easyrsa build-ca nopass
```

### Generate Server Certificate and Key
```bash
./easyrsa gen-req server nopass
./easyrsa sign-req server server
```

### Generate Diffie-Hellman Parameters
```bash
./easyrsa gen-dh
```

### Copy Certificates and Keys to OpenVPN Directory
```bash
sudo cp ~/easy-rsa/pki/ca.crt /etc/openvpn/server/
sudo cp ~/easy-rsa/pki/issued/server.crt /etc/openvpn/server/
sudo cp ~/easy-rsa/pki/private/server.key /etc/openvpn/server/
sudo cp ~/easy-rsa/pki/dh.pem /etc/openvpn/server/
```

## Configure OpenVPN Server
Create a new configuration file:
```bash
sudo nano /etc/openvpn/server/server.conf
```
Paste the following configuration:
```ini
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh.pem
server 10.8.0.0 255.255.255.0
push "route 10.0.2.0 255.255.255.0"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"
keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
verb 3
```

## Enable IP Forwarding
```bash
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Configure NAT and Firewall Rules
```bash
sudo iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
sudo apt install iptables-persistent -y
```

## Start and Enable OpenVPN Service
```bash
sudo systemctl start openvpn-server@server
sudo systemctl enable openvpn-server@server
```

## Generate Client Certificate
```bash
cd ~/easy-rsa
./easyrsa gen-req client1 nopass
./easyrsa sign-req client client1
```

## Create Client Configuration File
Create a new file `client.ovpn` and add the following content:
```ini
client
dev tun
proto udp
remote YOUR_SERVER_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
verb 3
```
Append CA, client certificate, and key:
```bash
echo "<ca>" >> client.ovpn
cat ~/easy-rsa/pki/ca.crt >> client.ovpn
echo "</ca>" >> client.ovpn

echo "<cert>" >> client.ovpn
cat ~/easy-rsa/pki/issued/client1.crt >> client.ovpn
echo "</cert>" >> client.ovpn

echo "<key>" >> client.ovpn
cat ~/easy-rsa/pki/private/client1.key >> client.ovpn
echo "</key>" >> client.ovpn
```

## Verify OpenVPN Status
```bash
sudo systemctl status openvpn-server@server
```
Monitor logs:
```bash
sudo tail -f /var/log/openvpn/openvpn.log
```

## Configure Routing for Internal Network
```bash
push "route 10.0.0.0 255.0.0.0"
sudo sysctl -w net.ipv4.ip_forward=1
echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/sysctl.conf
sudo iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -d 10.0.2.0/24 -j MASQUERADE
sudo iptables -A FORWARD -s 10.8.0.0/24 -d 10.0.2.0/24 -j ACCEPT
```

Your OpenVPN server is now set up and ready to use. Distribute the `client.ovpn` file to clients for connection.

## On your local machine
```bash
sudo cp ~/Downloads/client.ovpn /etc/openvpn/client/
sudo openvpn --config /etc/openvpn/client/client.ovpn

```
# How to keep an SSH connection when establishing an OpenVPN connection on a VPS server

## The issue
When establishing a VPN connection from a VPS server, new default routes are added to use the VPN tunnel interface and gateway, which take precedence over the existing routes. This results in any existing remote connectivity to the VPS server failing, such as the current SSH remote connections, since the return routes used to the establish the original connection are now different.

## The resolution
To correct the issue, we need to add a new route to the host routing table, which will route all traffic to the existing remote host through the original default gateway rather than the new VPN tunnel interface and gateway.
This can be done manually by executing the script below prior to establishing the VPN connection on the VPS,
``` #!/bin/bash

# Get the remote IP address for the active connection
IP=$(/usr/bin/who -m --ips|/usr/bin/awk '{print $6}')

# Get the current default gateway
GW=$(route -n | /usr/bin/grep -e ^0.0.0.0 | /usr/bin/awk '{print $2}')

# Add a new host route for the remote host
route add -host $IP gw $GW
```
or alternatively, may be executed automatically through OpenVPN by adding the following lines to the .ovpn file, which will execute the script once the VPN tunnel interface is up.
``` 
script-security 2
up /path/to/script/add_route.sh
```
## What does the script do?
The script will grab the IP address and default gateway for the existing remote connection, and add it to the route table.

## How does this affect my VPN communications?
Your remote connection source address will continue to be routed through the existing non-VPN interface, meaning existing active remote connections will continue to work. However, all other VPS IP traffic will be routed through the VPN tunnel.
If you require VPN connectivity to the remote address, you will need to establish a separate VPN connection from the client machine to the VPS server prior to running this script and establishing the VPN on the VPS server.

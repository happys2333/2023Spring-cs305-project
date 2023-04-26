# 提示：仅仅完成这份文件里的代码并不会让Ryu变成一个DHCP服务器，你需要在controller.py中引用这里的代码。
# GitHub上有许多Ryu框架相关的项目，你或许能从中得到灵感。
class DHCPServer(object):
    # The MAC address and the host name of the controller
    hw_addr = 
    hostname = ''
    
    netmask = ''
    dns = ''
    pool = ['192.168.1.'+ str(x) for x in range(3,254)]
    segment = 
    ip_pool = {}
    ip_leases = {}
    ip_offers = {}
    lease_time = 

    @classmethod
    def get_option(cls, dhcp_pkt, tag):
    	# Parse Options from a DHCP packet
        pass

    @classmethod
    def add_arp(cls, ip_addr, mac_addr, datapath, port):
    	# Add records to the ARP table
        pass

    @classmethod
    def create_ack(cls, pkt, datapath, port):
        # Create a DHCP Ack packet

    @classmethod
    def create_offer(cls, pkt, datapath):
        # Create a DHCP Offer packet

    @classmethod
    def get_state(cls, pkt_dhcp):
        # Get the state from a DHCP packet

    @classmethod
    def _handle_dhcp(cls, datapath, port, pkt):
        # Handle inbound DHCP packets

    @classmethod
    def _send_packet(cls, datapath, port, pkt):
        # Send DHCP packets

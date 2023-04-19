# mininet command line tools to help you test
import logging


# ping a host from another host
def ping(host, dst, count=1, timeout=1):
    return host.cmd('ping -c %s -W %s %s' % (count, timeout, dst))


# arp pack send
def send_arp(node, count=1):
    node.cmd('arping -c %s -A -I %s-eth0 %s' % (count, node.name, node.IP()))


# arp all hosts
def do_arp_all(mn):
    for h in mn.hosts:
        # Send a "join message", which is a gratuitous ARP
        send_arp(h)


# setting ip for host
def set_ip(host, ip):
    host.setIP(ip, intf='%s-eth0' % host.name)

# router config
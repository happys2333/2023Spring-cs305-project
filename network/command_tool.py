# mininet command line tools to help you test


# ping a host from another host
def ping(host, dst, count=1, timeout=1):
    return host.cmd('ping -c %s -W %s %s' % (count, timeout, dst))


# arp pack send
def send_arp(node, count=1):
    node.cmd('arping -c %s -A -I %s-eth0 %s' % (count, node.name, node.IP()))


# arp all hosts
def do_arp_all(net):
    for h in net.hosts:
        # Send a "join message", which is a gratuitous ARP
        send_arp(h)


# setting ip for host
def set_ip(host, ip):
    host.setIP(ip, intf='%s-eth0' % host.name)

# disable ipv6
def disable_ipv6(node):
    node.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    node.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    node.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

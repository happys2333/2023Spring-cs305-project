import sys
import time
import argparse
from topo import net_topo
from command_tool import disable_ipv6, do_arp_all
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController

from mininet.topolib import TreeTopo
from mininet.log import setLogLevel, info

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--topo', type=str, default='Star')
    parser.add_argument('--controller_ip', type=str, default='127.0.0.1')
    parser.add_argument('--controller_port', type=int, default=6633)
    args = parser.parse_args()
    net = Mininet(topo=net_topo[args.topo](), switch=OVSSwitch, controller=RemoteController('SUSTC Controller',
                                                                                          ip=args.controller_ip,
                                                                                          port=args.controller_port))

    # disable ipv6 for all hosts and switches
    for h in net.hosts:
        disable_ipv6(h)


    for h in net.switches:
        disable_ipv6(h)


    net.start()
    do_arp_all(net)
    CLI(net)
    net.stop()

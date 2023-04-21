from mininet.topo import Topo


# a simple topology with 3 hosts and 1 switch
class StarTopology(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        for i in range(3):
            h = self.addHost('h%s' % (i + 1))
            self.addLink(s1, h)

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.build()


# a simple topology with 3 hosts and 3 switches connected in a linear fashion
class LinearTopology(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, h1)
        self.addLink(s3, h2)
        self.addLink(s3, h3)

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.build()


class RingTopology(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.build()


class InternetTopology(Topo):
    def build(self):
        coreSwitch = self.addSwitch('s1')
        aggrSwitch1 = self.addSwitch('s2')
        aggrSwitch2 = self.addSwitch('s3')
        accessSwitch1 = self.addSwitch('s4')
        accessSwitch2 = self.addSwitch('s5')

        for i in range(5):
            host = self.addHost('h%s' % (i + 1))
            self.addLink(accessSwitch1, host)
        for i in range(5, 10):
            host = self.addHost('h%s' % (i + 1))
            self.addLink(accessSwitch2, host)

        self.addLink(coreSwitch, aggrSwitch1)
        self.addLink(coreSwitch, aggrSwitch2)
        self.addLink(aggrSwitch1, accessSwitch1)
        self.addLink(aggrSwitch2, accessSwitch1)
        self.addLink(aggrSwitch1, accessSwitch2)
        self.addLink(aggrSwitch2, accessSwitch2)

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.build()


class DualRingTopology(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s6)
        self.addLink(s6, s1)
        self.addLink(s2, s5)
        self.addLink(s3, s6)

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.build()


class InternetServerTopology(Topo):
    def build(self):
        # 创建路由器
        isp1 = self.addHost('r1', ip='10.0.1.1/24')
        isp2 = self.addHost('r2', ip='10.0.2.1/24')
        router1 = self.addHost('r3')

        # 创建交换机
        coreSwitch = self.addSwitch('s1')
        distributionSwitch1 = self.addSwitch('s2')
        accessSwitch1 = self.addSwitch('s3')
        accessSwitch2 = self.addSwitch('s4')
        accessSwitch3 = self.addSwitch('s5')
        accessSwitch4 = self.addSwitch('s6')
        accessSwitch5 = self.addSwitch('s7')

        # 创建主机
        server1 = self.addHost('server1', ip='192.168.1.10/24')
        server2 = self.addHost('server2', ip='192.168.1.11/24')
        server3 = self.addHost('server3', ip='192.168.1.12/24')
        client1 = self.addHost('client1', ip='192.168.2.10/24')
        client2 = self.addHost('client2', ip='192.168.2.11/24')
        client3 = self.addHost('client3', ip='192.168.3.10/24')
        client4 = self.addHost('client4', ip='192.168.3.11/24')
        client5 = self.addHost('client5', ip='192.168.4.10/24')
        client6 = self.addHost('client6', ip='192.168.4.11/24')
        client7 = self.addHost('client7', ip='192.168.5.10/24')
        client8 = self.addHost('client8', ip='192.168.5.11/24')
        client9 = self.addHost('client9', ip='192.168.6.10/24')
        client10 = self.addHost('client10', ip='192.168.6.11/24')

        # 给每个交换机附加一个VLAN ID
        coreSwitch.cmd('ovs-vsctl set bridge s1 vlan_mode=dot1q')
        distributionSwitch1.cmd('ovs-vsctl set bridge s2 vlan_mode=dot1q')
        accessSwitch1.cmd('ovs-vsctl set bridge s3 vlan_mode=dot1q')
        accessSwitch2.cmd('ovs-vsctl set bridge s4 vlan_mode=dot1q')
        accessSwitch3.cmd('ovs-vsctl set bridge s5 vlan_mode=dot1q')
        accessSwitch4.cmd('ovs-vsctl set bridge s6 vlan_mode=dot1q')
        accessSwitch5.cmd('ovs-vsctl set bridge s7 vlan_mode=dot1q')

        # 连接路由器和ISP
        self.addLink(router1, isp1)
        self.addLink(router1, isp2)

        # 连接交换机和路由器
        self.addLink(coreSwitch, router1, intfName2='r3-eth1')

        # 连接交换机和交换机
        self.addLink(coreSwitch, distributionSwitch1, intfName1='s1-eth2', intfName2='s2-eth2')
        self.addLink(distributionSwitch1, accessSwitch1, intfName1='s2-eth3', intfName2='s3-eth1')
        self.addLink(distributionSwitch1, accessSwitch2, intfName1='s2-eth4', intfName2='s4-eth1')
        self.addLink(distributionSwitch1, accessSwitch3, intfName1='s2-eth5', intfName2='s5-eth1')
        self.addLink(distributionSwitch1, accessSwitch4, intfName1='s2-eth6', intfName2='s6-eth1')
        self.addLink(distributionSwitch1, accessSwitch5, intfName1='s2-eth7', intfName2='s7-eth1')

        # 连接交换机和主机
        self.addLink(accessSwitch1, server1)
        self.addLink(accessSwitch1, server2)
        self.addLink(accessSwitch1, server3)
        self.addLink(accessSwitch2, client1)
        self.addLink(accessSwitch2, client2)
        self.addLink(accessSwitch3, client3)
        self.addLink(accessSwitch3, client4)
        self.addLink(accessSwitch4, client5)
        self.addLink(accessSwitch4, client6)
        self.addLink(accessSwitch5, client7)
        self.addLink(accessSwitch5, client8)
        self.addLink(accessSwitch5, client9)
        self.addLink(accessSwitch5, client10)

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.build()

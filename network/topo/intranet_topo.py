
from mininet.topo import Topo

class SingleSwitchTopology(Topo):
    def build(self):
        # 创建交换机
        switch1 = self.addSwitch('s1')

        # 创建主机
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')

        # 连接交换机和主机
        self.addLink(switch1, host1)
        self.addLink(switch1, host2)
        self.addLink(switch1, host3)


class TwoSwitchTopology(Topo):
    def build(self):
        # 创建交换机
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')

        # 创建主机
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')

        # 连接交换机和主机
        self.addLink(switch1, host1)
        self.addLink(switch1, host2)
        self.addLink(switch2, host3)

        # 连接交换机
        self.addLink(switch1, switch2)


class ThreeTierTopology(Topo):
    def build(self):
        # 创建交换机
        coreSwitch = self.addSwitch('s1')
        distributionSwitch1 = self.addSwitch('s2')
        distributionSwitch2 = self.addSwitch('s3')
        accessSwitch1 = self.addSwitch('s4')
        accessSwitch2 = self.addSwitch('s5')
        accessSwitch3 = self.addSwitch('s6')

        # 创建主机
        server1 = self.addHost('server1')
        server2 = self.addHost('server2')
        client1 = self.addHost('client1')
        client2 = self.addHost('client2')
        client3 = self.addHost('client3')
        client4 = self.addHost('client4')

        # 连接交换机和主机
        self.addLink(coreSwitch, distributionSwitch1)
        self.addLink(coreSwitch, distributionSwitch2)
        self.addLink(distributionSwitch1, accessSwitch1)
        self.addLink(distributionSwitch1, accessSwitch2)
        self.addLink(distributionSwitch2, accessSwitch3)
        self.addLink(accessSwitch1, server1)
        self.addLink(accessSwitch2, server2)
        self.addLink(accessSwitch3, client1)
        self.addLink(accessSwitch3, client2)
        self.addLink(accessSwitch3, client3)
        self.addLink(accessSwitch3, client4)

class SimpleRouterTopology(Topo):
    def build(self):
        # 创建路由器
        router1 = self.addHost('r1', ip='10.0.1.1/24')
        router2 = self.addHost('r2', ip='10.0.2.1/24')

        # 创建主机
        client1 = self.addHost('c1', ip='10.0.1.2/24')
        client2 = self.addHost('c2', ip='10.0.2.2/24')

        # 连接路由器和主机
        self.addLink(router1, client1)
        self.addLink(router2, client2)

        # 设置路由器的路由表
        router1.cmd('ip route add 10.0.2.0/24 via 10.0.1.1')
        router2.cmd('ip route add 10.0.1.0/24 via 10.0.2.1')
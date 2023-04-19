from mininet.net import Mininet
from mininet.clean import Cleanup
from topo import intranet_topo
from config import config
from mininet.node import RemoteController


topo = intranet_topo['Single']()

# TODO: change the ip address to your controller's ip address
net = Mininet(topo=topo, controller=RemoteController(name='SUSTC ITSC', ip='127.0.0.1', port=config.CONTROLLER_PORT),
              autoSetMacs=False)


# clean up cache
Cleanup()
from mininet.net import Mininet
from mininet.clean import Cleanup
from topo import internet_topo
from config import config
from mininet.node import RemoteController

topo = internet_topo['Star']()
# TODO: change the ip address to your controller's ip address
net = Mininet(topo=topo, controller=RemoteController(name='SUSTC ITSC', ip='**.**.**.**', port=config.CONTROLLER_PORT),
              autoSetMacs=False)

# clean up cache
Cleanup()

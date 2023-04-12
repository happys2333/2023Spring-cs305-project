from mininet.net import Mininet
from mininet.clean import Cleanup
from .topo import intranet_topo
from config import config
from mininet.node import RemoteController


topo = intranet_topo['Single']()


net = Mininet(topo=topo,controller=RemoteController(name='SUSTC ITSC',ip='',port=config.CONTROLLER_PORT))


# clean up cache
Cleanup()
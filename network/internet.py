from mininet.net import Mininet
from mininet.clean import Cleanup
from .topo import internet_topo
from config import config
from mininet.node import RemoteController


topo = internet_topo['Star']()


net = Mininet(topo=topo,controller=RemoteController(name='SUSTC ITSC',ip='',port=config.CONTROLLER_PORT))


# clean up cache
Cleanup()
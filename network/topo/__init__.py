from .topo import *


net_topo = {
    "Star" : StarTopology,
    "Linear" : LinearTopology,
    "Ring": RingTopology,
    "Internet": InternetTopology,
    "Server": InternetServerTopology,
}
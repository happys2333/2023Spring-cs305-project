from .intranet_topo import *
from .internet_topo import *

intranet_topo = {
    "Single": SingleSwitchTopology,
    "Double": TwoSwitchTopology,
    "Three": ThreeTierTopology,
    "Router": SimpleRouterTopology,

}

internet_topo = {
    "Star" : StarTopology,
    "Linear" : LinearTopology,
    "Ring": RingTopology,
    "Internet": InternetTopology,
    "Server": InternetServerTopology,
}
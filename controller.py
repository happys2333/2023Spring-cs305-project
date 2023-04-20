from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.topology import event, switches
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ether_types, arp
from topo_builder import TopoGraph


class RoutingApp(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topo = TopoGraph("mininet")
        # TODO: implement initialization code here

    @set_ev_cls(event.EventSwitchEnter)
    def handle_switch_add(self, ev):
        # This function will call when a switch is added to the network
        pass

    @set_ev_cls(event.EventSwitchLeave)
    def handle_switch_leave(self, ev):
        # This function will call when a switch is removed from the network
        pass

    @set_ev_cls(event.EventHostAdd)
    def handle_host_add(self, ev):
        # This function will call when a host is added to the network
        pass

    @set_ev_cls(event.EventHostDelete)
    def handle_host_delete(self, ev):
        # This function will call when a host is removed from the network
        pass

    @set_ev_cls(event.EventLinkAdd)
    def handle_link_add(self, ev):
        # This function will call when a link is added to the network
        pass

    @set_ev_cls(event.EventPortModify)
    def handle_port_modify(self, ev):
        pass

    @set_ev_cls(event.EventLinkDelete)
    def handle_link_delete(self, ev):
        # This function will call when a link is removed from the network
        pass

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        pass

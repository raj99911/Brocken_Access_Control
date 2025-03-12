from scapy.all import sniff
from channels.layers import get_channel_layer
import asyncio

def packet_callback(packet):
    packet_data = {
        "source": packet.src if hasattr(packet, "src") else "Unknown",
        "destination": packet.dst if hasattr(packet, "dst") else "Unknown",
        "protocol": packet.proto if hasattr(packet, "proto") else "Unknown",
        "length": len(packet),
    }

    channel_layer = get_channel_layer()
    asyncio.run(channel_layer.group_send("packet_monitor", {"type": "send_packet", "packet": packet_data}))

def start_sniffing():
    sniff(prn=packet_callback, store=False)

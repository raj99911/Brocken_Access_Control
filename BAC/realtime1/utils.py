

from realtime1.models import IntrusionLog

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP


packet_count = 0  # Global counter

def save_intrusion_alert(src_ip, dst_ip, protocol, message):
    print(f"Saving to DB: {src_ip} -> {dst_ip} ({protocol}) | {message}")
    IntrusionLog.objects.create(
        source_ip=src_ip,
        destination_ip=dst_ip,
        protocol=protocol,
        alert_message=message
    )

def packet_callback(packet):
    global packet_count
    packet_count += 1  # Increment counter

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"

        print(f"Packet {packet_count}: {src_ip} -> {dst_ip} ({protocol})")

        # Save only every 30th packet
        if packet_count % 100 == 0:
            alert_msg = f"Traffic detected from {src_ip}"
            save_intrusion_alert(src_ip, dst_ip, protocol, alert_msg)

# Start sniffing
def start_sniffing():
    print("Starting packet sniffing...")
    sniff(prn=packet_callback, iface="en0", store=False)

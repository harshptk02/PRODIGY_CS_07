from scapy.all import sniff, IP, TCP, UDP, Ether
import argparse

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Other"

        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip} | Protocol: {protocol_name}")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload: {payload[:50]}...")  
        print("-" * 50)


def start_sniffing(interface=None, count=0):
    print(f"Starting packet sniffer on interface {interface}...")
    sniff(iface=interface, prn=process_packet, count=count)

if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description="A basic packet sniffer for educational purposes.")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on", required=True)
    parser.add_argument("-c", "--count", type=int, help="Number of packets to capture (0 for unlimited)", default=0)
    args = parser.parse_args()

 
    try:
        start_sniffing(interface=args.interface, count=args.count)
    except PermissionError:
        print("Error: You need root/administrator privileges to capture packets.")
    except KeyboardInterrupt:
        print("\nPacket sniffing stopped.")
from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

packet_count = 0
protocol_count = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "Other": 0
}


def analyze_packet(packet):
    global packet_count

    # Ignore packets that don't contain an IP layer
    if IP not in packet:
        return

    packet_count += 1

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Analyze payload
    if packet.haslayer("Raw"):
        payload = bytes(packet["Raw"].load)
        payload_size = len(payload)

        # Hexadecimal representation
        payload_preview = payload[:32].hex(" ")

        # Try to extract readable text
        readable_text = ''.join(
            chr(byte) if 32 <= byte <= 126 else '.'
            for byte in payload[:64]
        )

    else:
        payload_size = 0
        payload_preview = "No payload"
        readable_text = "No payload"

    # Identify protocol
    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"
    else:
        protocol = "Other"

    protocol_count[protocol] += 1

    print(f"\nPacket #{packet_count}")
    print(f"Time          : {timestamp}")
    print(f"Source IP     : {source_ip}")
    print(f"Destination   : {destination_ip}")
    print(f"Protocol      : {protocol}")
    print(f"Packet Size   : {packet_size} bytes")
    print(f"Payload Size  : {payload_size} bytes")
    print(f"Payload Hex   : {payload_preview}")
    print(f"Payload Text  : {readable_text}")
    print("-" * 50)


print("=" * 50)
print("              BASIC NETWORK SNIFFER")
print("=" * 50)
print("\nCapturing 20 packets...")
print("Generate some normal network traffic.\n")

sniff(count=20, prn=analyze_packet, store=False)

print("\n" + "=" * 50)
print("              PROTOCOL SUMMARY")
print("=" * 50)

for protocol, count in protocol_count.items():
    print(f"{protocol:<10}: {count}")

print(f"\nTotal packets captured: {packet_count}")
print("=" * 50)

print("Capture completed!")
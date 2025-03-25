from scapy.all import IP, ICMP, sr1
import sys

def traceroute(destination, max_hops=30):
    print(f"Tracing route to {destination}\n")
    
    for ttl in range(1, max_hops + 1):
        packet = IP(dst=destination, ttl=ttl) / ICMP()
        reply = sr1(packet, verbose=0, timeout=1)

        if reply is None:
            print(f"{ttl}: * * * Request timed out")
        else:
            print(f"{ttl}: {reply.src}")
            if reply.src == destination:
                print("Trace complete.")
                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python traceroute.py <destination>")
    else:
        traceroute(sys.argv[1])

class ARP_RARP_Simulator:
    def __init__(self):
        # Simulating an ARP table (IP to MAC mapping)
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18",
        }

        # Simulating a RARP table (MAC to IP mapping)
        self.rarp_table = {
            mac_address: ip_address
            for ip_address, mac_address in self.arp_table.items()
        }

    def arp_request(self, ip_address):
        """Simulate an ARP request to get the MAC address for an IP."""
        print(f"ARP Request: Who has {ip_address}? Tell me your MAC address.")
        mac_address = self.arp_table.get(ip_address)

        if mac_address:
            print(f"ARP Reply: {ip_address} is at {mac_address}.")
            return mac_address

        print(f"ARP Reply: {ip_address} is not found.")
        return None

    def rarp_request(self, mac_address):
        """Simulate a RARP request to get the IP address for a MAC."""
        print(
            f"RARP Request: Who has MAC address {mac_address}? "
            "Tell me your IP address."
        )
        ip_address = self.rarp_table.get(mac_address)

        if ip_address:
            print(f"RARP Reply: {mac_address} is associated with IP {ip_address}.")
            return ip_address

        print(f"RARP Reply: {mac_address} is not found.")
        return None


if __name__ == "__main__":
    simulator = ARP_RARP_Simulator()

    # ARP request examples
    simulator.arp_request("192.168.1.1")
    simulator.arp_request("192.168.1.100")

    # RARP request examples
    simulator.rarp_request("00:0a:95:9d:68:16")
    simulator.rarp_request("00:0a:95:9d:68:99")

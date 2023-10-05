class Router:
    def __init__(self):
        self.routing_table = []

    def add_route(self, network, mask, gateway):
        self.routing_table.append((network, mask, gateway))

    def find_best_route(self, destination):
        best_route = None
        longest_prefix = 0

        for route in self.routing_table:
            network, mask, gateway = route
            network_ip = self.ip_to_int(network)
            destination_ip = self.ip_to_int(destination)

            # Calculate the network address for the route
            route_ip = network_ip & self.ip_to_int(mask)

            if destination_ip & self.ip_to_int(mask) == route_ip:
                # The destination IP matches this route's network
                if len(mask) > longest_prefix:
                    longest_prefix = len(mask)
                    best_route = route

        return best_route

    def ip_to_int(self, ip):
        parts = [int(part) for part in ip.split('.')]
        return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

    def int_to_ip(self, ip_int):
        return ".".join(map(str, [(ip_int >> 24) & 255, (ip_int >> 16) & 255, (ip_int >> 8) & 255, ip_int & 255]))


# Create a router
router = Router()

# Add static routes to the routing table
router.add_route("192.168.1.0", "255.255.255.0", "192.168.0.1")
router.add_route("10.0.0.0", "255.0.0.0", "10.0.0.1")

# Simulate a packet arriving at the router with a destination IP
destination_ip = "192.168.1.100"
best_route = router.find_best_route(destination_ip)

if best_route:
    print(f"Packet to {destination_ip} should be forwarded to gateway {best_route[2]}")
else:
    print(f"No matching route found for {destination_ip}")

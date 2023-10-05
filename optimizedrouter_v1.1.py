import json

class Router:
    def __init__(self):
        self.routing_table = []
        self.route_log = {}  # To store routing decisions

    def add_route(self, network, mask, gateway):
        self.routing_table.append((network, mask, gateway))

    def find_best_route(self, destination):
        best_route = None
        longest_prefix = 0

        for route in self.routing_table:
            network, mask, gateway = route
            network_ip = self.ip_to_int(network)
            destination_ip = self.ip_to_int(destination)

            route_ip = network_ip & self.ip_to_int(mask)

            if destination_ip & self.ip_to_int(mask) == route_ip:
                if len(mask) > longest_prefix:
                    longest_prefix = len(mask)
                    best_route = route

        # Log the routing decision
        self.route_log[destination] = best_route

        return best_route

    def export_route_log(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.route_log, json_file)

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

# Simulate routing decisions
router.find_best_route("192.168.1.100")
router.find_best_route("10.0.0.5")

# Export the route log to a JSON file
router.export_route_log("route_log.json")

class Host:
    def __init__(self, ip):
        self.ip = ip
        self.connected_hosts = []

    def connect(self, host):
        self.connected_hosts.append(host)
def create_broadcast_tree(subnet):
    hosts = [Host(f"{subnet}.{i}") for i in range(1, 255)]
    broadcast_address = Host(f"{subnet}.255")
    for host in hosts:
        host.connect(broadcast_address)

    return hosts, broadcast_address

def print_broadcast_tree(hosts, broadcast_address):
    for host in hosts:
        print(f"{host.ip} --> {broadcast_address.ip}")
subnet = "192.168.1"
hosts, broadcast_address = create_broadcast_tree(subnet)
print_broadcast_tree(hosts, broadcast_address)
    
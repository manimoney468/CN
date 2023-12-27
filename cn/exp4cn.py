import copy
network = {
    'A': {'A': 0, 'B': 3, 'C': 2, 'D': float('inf')},
    'B': {'A': 3, 'B': 0, 'C': float('inf'), 'D': 4},
    'C': {'A': 2, 'B': float('inf'), 'C': 0, 'D': 1},
    'D': {'A': float('inf'), 'B': 4, 'C': 1, 'D': 0}
}
def distance_vector_routing(network):
    updated = True
    iterations = 0
    while updated:
        updated = False
        iterations += 1
        prev_network = copy.deepcopy(network)
        for node in network:
            for dest in network[node]:
                if dest != node:
                    min_cost = float('inf')
                    for neighbor in network:
                        cost = prev_network[node][neighbor] + prev_network[neighbor][dest]
                        if cost < min_cost:
                            min_cost = cost
                    if min_cost < network[node][dest]:
                        network[node][dest] = min_cost
                        updated = True
        if updated:
            print(f"Iteration {iterations}:")
            for node, costs in network.items():
                print(f"Node {node}: {costs}")
            print()
print("Initial Network Topology:")
for node, costs in network.items():
    print(f"Node {node}: {costs}")
print()
distance_vector_routing(network)

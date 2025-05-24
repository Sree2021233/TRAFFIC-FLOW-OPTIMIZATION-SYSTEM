import networkx as nx
import matplotlib.pyplot as plt
import heapq

class TrafficNetwork:
    def _init_(self):
        self.graph = nx.DiGraph()

    def add_road(self, from_node, to_node, base_time, traffic_factor=1.0):
        travel_time = base_time * traffic_factor
        self.graph.add_edge(from_node, to_node, weight=travel_time)

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_dist, current_node = heapq.heappop(queue)

            for neighbor in self.graph.neighbors(current_node):
                weight = self.graph[current_node][neighbor]['weight']
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

    def draw_network(self):
        pos = nx.spring_layout(self.graph)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Traffic Network with Travel Times")
        plt.show()


# Example usage
network = TrafficNetwork()
network.add_road('A', 'B', base_time=4, traffic_factor=1.0)
network.add_road('A', 'C', base_time=2, traffic_factor=1.2)  # Slight congestion
network.add_road('B', 'C', base_time=5, traffic_factor=1.5)  # Heavy traffic
network.add_road('B', 'D', base_time=10, traffic_factor=0.9) # Light traffic
network.add_road('C', 'D', base_time=3, traffic_factor=1.1)

# Compute shortest travel times from 'A'
shortest_paths = network.dijkstra('A')
print("Shortest travel times from A:", shortest_paths)

# Visualize the network
network.draw_network()
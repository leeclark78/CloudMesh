import logging
import networkx as nx
import matplotlib.pyplot as plt

class ArchitectureVisualizer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def visualize(self, architecture):
        self.logger.info("Visualizing cloud architecture")
        
        G = nx.Graph()
        
        for cloud, services in architecture.items():
            G.add_node(cloud, color='lightblue', size=3000)
            for service in services:
                G.add_node(service['name'], color='lightgreen', size=1000)
                G.add_edge(cloud, service['name'])
        
        pos = nx.spring_layout(G)
        colors = [G.nodes[node]['color'] for node in G.nodes()]
        sizes = [G.nodes[node]['size'] for node in G.nodes()]
        
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, node_color=colors, node_size=sizes, with_labels=True)
        plt.title("Cloud Architecture Visualization")
        
        # Save the plot to a file
        plt.savefig("cloud_architecture.png")
        plt.close()
        
        return "cloud_architecture.png"

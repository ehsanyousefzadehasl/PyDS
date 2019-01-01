class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        list_to_return = []
        for edge in self.edges:
            list_to_return.append((edge.value, edge.node_from.value, edge.node_to.value))
        return list_to_return

    def get_adjacency_list(self):
        max_index = self.find_max_index()

        adjacency_list = [None] * (max_index + 1)
        for edge_object in self.edges:
            if adjacency_list[edge_object.node_from.value]:
                adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
            else:
                adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
        return adjacency_list
    
    def get_adjacency_matrix(self):
        max_index = self.find_max_index()
        adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        for edge_object in self.edges:
            adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
        return adjacency_matrix


    def find_max_index(self):
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

graph = Graph()
graph.insert_edge(500, 0, 2)
graph.insert_edge(501, 1, 5)
graph.insert_edge(502, 2, 3)
graph.insert_edge(503, 3, 5)
graph.insert_edge(503, 4, 5)
# Should be [(500, 0, 2), (501, 1, 5), (502, 2, 3), (503, 3, 5), (503, 4, 5)]
print(graph.get_edge_list())
# Should be [[(2, 500)], [(5, 501)], [(3, 502)], [(5, 503)], [(5, 503)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 500, 0, 0, 0], [0, 0, 0, 0, 0, 501], [0, 0, 0, 502, 0, 0], [0, 0, 0, 0, 0, 503], [0, 0, 0, 0, 0, 503], [0, 0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
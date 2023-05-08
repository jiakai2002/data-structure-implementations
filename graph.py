class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        # convert list structure into dictionary
        # with a key and list of values
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_path(self, start, end, path=[]):
        path = path + [start]
        # simplest case / terminal condition
        if start == end:
            return [path]
        # null case
        if start not in self.graph_dict.keys():
            return []
        # regular case: reduce problem recursively
        paths = []
        for node in self.graph_dict[start]:
            # avoid loops
            if node not in path:
                # all paths for node to end, append to paths
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        # same loops
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                current_sp = self.get_shortest_path(node, end, path)
                # filter case of None
                if current_sp:
                    if shortest_path is None or len(current_sp)<len(shortest_path):
                        shortest_path = current_sp
        return shortest_path

            

if __name__ == "__main__":
    routes = [("SG", "Paris"), ("SG", "Dubai"), ("Paris", "Dubai"), ("Paris", "NY"), ("Dubai", "NY"), ("NY", "Toronto")]
    route_graph = Graph(routes)
    print(route_graph.get_path("SG","Toronto"))
    print(route_graph.get_shortest_path("SG","Toronto"))

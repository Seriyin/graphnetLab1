import networkx as nx
from random import choices
from itertools import permutations, repeat, starmap
from matplotlib import pyplot

class Grapher:

    def generate_n(self, n):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(range(0,n))
    
    def build_connected(self):
        population = list(range(0,len(self.graph)))
        weights = list(repeat(1,len(self.graph)))
        while not nx.is_connected(self.graph):
            l = choices(population,weights=weights, k=2)
            if (l[0]!=l[1] and not self.graph.has_edge(l[0],l[1])) :
                self.graph.add_edge(l[0], l[1])
                weights[l[0]]*=1.15
                weights[l[1]]*=1.15

    def sample_graph(self, size, samples):
        self.generate_n(size)
        self.build_connected()
        return nx.degree_histogram(self.graph)


def main():
    graph = Grapher()
    for i in range(20,100,5):
        samplemat = graph.sample_graph(i, 30)
        f = pyplot.figure()
        pyplot.plot(range(0,len(samplemat)),samplemat)
        pyplot.savefig(f'powergraphsampling{i}.pdf')
        pyplot.close(f)

main()

import networkx as nx
from random import randrange
from itertools import product
from matplotlib import pyplot

class Grapher:

    def generate_n(self, n):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(range(0,n))
    
    def build_connected(self):
        weights = list(range(0,len(self.graph))) 
        while not nx.is_connected(self.graph):
            s = randrange(0, len(self.graph)-1)
            tc = randrange(0, weights[len(self.graph)-1])
            if weights[s] != tc or not (weights[s] < tc and weights[s+1] > tc) :
                t = self.loop_node(weights, s, tc)
                self.graph.add_edge(s, t)

    def loop_node(self, weights, s, tc) :
        r = False
        if weights[s] > tc :
            for i,n in enumerate(weights) :
                if n > tc and r==False :
                    t = i
                    weights[i] += 1
                    r = True
                elif(i > s):
                    weights[i] += 2
                elif(n > tc) :
                    weights[i] += 1
        else :
            for i,n in enumerate(weights) :
                if n > tc and r==False:
                    t = i
                    weights[i] += 2
                    r = True
                elif(n > tc):
                    weights[i] += 2
                elif(i > s):
                    weights[i] += 1
        return t

    def sample_graph(self, size):
        self.generate_n(size)
        self.build_connected()
        return nx.degree_histogram(self.graph)


def main():
    graph = Grapher()
    samplemat = graph.sample_graph(30)
    f = pyplot.figure()
    pyplot.plot(range(0,len(samplemat)),samplemat)
    pyplot.show()
    pyplot.savefig('powergraphsampling.pdf')

main()

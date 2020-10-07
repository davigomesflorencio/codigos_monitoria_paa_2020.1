from collections import defaultdict 
import networkx as nx 

class Graph: 
  
    def __init__(self): 
        self.graph = nx.Graph()
        
    def addNode(self,node):
        self.graph.add_node(node)
    
    def addMultipleNodes(self,nodes):
        self.graph.add_nodes_from(nodes)
    
    def getNodes(self):
        return self.graph.nodes
        
    def getLenNodes(self):
        return self.graph.number_of_nodes()
    
    def getLenEdge(self):
        return len(self.graph.edges)  

    def addEdge(self, u, v): 
        self.graph.add_edge(u,v)
    
    def addEdge(self, u, v, p): 
        self.graph.add_edge(u,v,peso=p)

    def getNeighbors(self,v):
        return self.graph.neighbors(v)
        
    def getVertexDegreee(self,v):
        grau=0
        for _ in self.graph.neighbors(v):
            grau+=1 
        return grau
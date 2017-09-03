import networkx as nx

class GraphByEdgeData:
    """
    """
    def __init__(self, graphName):
        """
        """
        self._name=graphName
        self._table=None
        self._nx=nx.Graph()

    def addTable(self, tableIterator):
        """
        required columns
            -> node_source
            -> node_target
            -> edge_date
        """
        self._table=tableIterator

    def runGraph(self):
        """
        """
        for row in self._table:

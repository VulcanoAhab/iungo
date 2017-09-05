#append path
import sys
import os
_toHere=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_toHere)

#imports
import unittest
from loadTable import Transform

class TransformTest(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self._file="tests/tableTest.csv"
        self._table=Transform(self._file)

    def test_tableParse(self):
        """
        """
        _reqs=("edge_date", "node_source","node_target")
        for row in self._table.parseRows():
            for field in _reqs:self.assertIn(field, row)


# command line
if __name__ == "__main__":

    unittest.main()

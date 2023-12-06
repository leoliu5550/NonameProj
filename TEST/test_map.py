import sys
sys.path.append(".")
from pathfinds.pathfind import pathfindalg


class Testpathfind:
    def test_map1(self):
        
        test_network = {
            0: {1: 62, 2: 44, 3: 67},
            1: {0: 62, 2: 32, 4: 52},
            2: {0: 44, 1: 33, 3: 32, 4: 52},
            3: {0: 67, 2: 32, 4: 54},
            4: {1: 52, 2: 52, 3: 54}
        }
        mapp = pathfindalg(test_network)
        assert mapp['path'][4][0] ==[4, 2, 0]
        assert mapp['length'][4][0] ==96
        
    def test_map2(self):
        
        test_network = {
            0: {1: 1},
            1: {0: 1, 2: 1},
            2: {1: 1, 3: 1, 5: 1},
            3: {2: 1, 4: 1, 6: 2},
            4: {3: 1},
            5: {2: 1, 6: 1, 7: 1},
            6: {3: 2, 5: 1, 8: 1},
            7: {5: 1},
            8: {6: 1}
        }
        mapp = pathfindalg(test_network)
        assert mapp['path'][0][-1] ==[0, 1, 2, 5, 6, 8]
        assert mapp['length'][0][-1] ==5
        
    def test_map3(self):
        
        test_network = {
            0: {1: 1},
            1: {0:1,2:1},
            2: {1:1,3:1},
            3: {2:1}
        }
        mapp = pathfindalg(test_network)
        assert mapp['path'][0][-1] ==[0, 1, 2, 3]
        assert mapp['length'][0][-1] ==3
        
    def test_map4(self):
        
        test_network = {
            0: {1: 1},
            1: {0:1,2:1,6:2},
            2: {1:1,3:1,4:2,5:1},
            3: {2:1},
            4: {2:2,6:5},
            5: {2:100},
            6: {4:5,1:2}
        }
        mapp = pathfindalg(test_network)
        assert mapp['path'][0][6] ==[0, 1, 6]
        assert mapp['length'][0][6] == 3
        
        
# {
#     "0": {
#       "1": 1
#     },
#     "1": {
#       "0": 1,
#       "2": 1
#     },
#     "2": {
#       "1": 1,
#       "3": 1
#     },
#     "3": {
#       "2": 1
#     }
# }
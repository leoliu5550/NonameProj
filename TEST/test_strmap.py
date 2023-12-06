import sys
sys.path.append(".")
from pathfinds.pathfind import pathfindalg,trans_strmap


class Testpathfind:
    def test_map1(self):
        
        test_network = {
            "A": {"B": 1},
            "B": { "A": 1,"C": 1},
            "C": {"B": 1,"D": 1},
            "D": {"C": 1}
        }
        substitute_network, _,_ = trans_strmap(test_network)
        mapp = pathfindalg(substitute_network)
        print(mapp)
        assert mapp['path'][3][0] ==[3, 2, 1,0]
        assert mapp['length'][3][0] ==3
        
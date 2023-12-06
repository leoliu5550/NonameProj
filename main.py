from pathfinds.pathfind import pathfindalg



if __name__ == '__main__':
    test_network = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    # network2 =  {
    #         "A": {"B": 1},
    #         "B": { "A": 1,"C": 1},
    #         "C": {"B": 1,"D": 1},
    #         "D": {"C": 1}
    #     }
    mapp = pathfindalg(test_network)
    
    # print("path")
    # for row in mapp['path']:
    #     print(row)
    # print("length")
    # for row in mapp['length']:
    #     print(row)

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle as pk
from typing import Dict


from pathfinds.pathfind import pathfindalg,trans_strmap


app = FastAPI()
class Item(BaseModel):
    name: str
    map_item: Dict

@app.post("/create_map/")
async def create_item(item: Item):
    # item = item.dict()
    # mapp = pathfindalg(item.map_item)
    substitute_network, reversed_mapping ,mapping = trans_strmap(item.map_item)
    shortpath = pathfindalg(substitute_network)
    
    shortpath_result = {
        "mapp":shortpath,
        "reversed_mapping":reversed_mapping,
        "mapping":mapping
    }
    with open(f"mapsazing/{item.name}.pkl","wb") as file:
        pk.dump(shortpath_result,file)
    print()
    return shortpath,mapping
# {
#     "A": {"B": 1},
#     "B": { "A": 1,"C": 1},
#     "C": {"B": 1,"D": 1},
#     "D": {"C": 1}
# }
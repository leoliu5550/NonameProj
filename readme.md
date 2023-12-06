# floyd-Warshall service

# POST Request
## url
    https://noname-proj.vercel.app//create_map/
## request payload
```JSON
{
  "name": "test",
  "map_item": {
    "node0": {"node1": 1},
    "node1": {"node0": 1,"node2": 1},
    "node2": {"node1": 1,"node3": 1},
    "node3": {"node2": 1}
  }
}
```

# Response
```JSON

{
  "mapp": {
    "path": [
      [
        [0],
        [0,1],
        [0,1,2],
        [0,1,2,3]
      ],
      [
        [1,0],
        [1],
        [1,2],
        [1, 2,3]
      ],
      [
        [2,1,0],
        [2,1],
        [2],
        [2,3]
      ],
      [
        [3,2,1,0],
        [3,2,1],
        [3,2],
        [3]
      ]
    ],
    "length": [
      [0,1,2,3],
      [1,0,1,2],
      [2,1,0,1],
      [3,2,1,0]
    ]
  },
  "reversed_mapping": {
    "0": "node0",
    "1": "node1",
    "2": "node2",
    "3": "node3"
  },
  "mapping": {
    "node0": 0,
    "node1": 1,
    "node2": 2,
    "node3": 3
  }
}

```
# Example Map
```mermid
    graph TD
        A-->B
        A-->C
        B-->D
        C-->D
```
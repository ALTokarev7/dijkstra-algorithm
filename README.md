# Dijkstra algorithm
Implementation of Dijkstra's algorithm for finding optimal paths in graphs.

## To run:
```bash
python main.py
```
or:
```bash
python3 main.py
```
## Sample:
### Enter this graph:
<img width="467" alt="image" src="https://github.com/user-attachments/assets/3f040b46-0fd3-47e9-b67f-68974bcbd682">

```bash
Enter a vertex name: A
Add neighbors? [y/n] y
vertex name: B
path cost: 1
Add more neighbors?  [y/n]: y
vertex name: C
path cost: 4
Add more neighbors?  [y/n]: n
Add more vertices?  [y/n]: y
Enter a vertex name: B
Add neighbors? [y/n] y
vertex name: D
path cost: 5
Add more neighbors?  [y/n]: n
Add more vertices?  [y/n]: y
Enter a vertex name: C
Add neighbors? [y/n] y
vertex name: D
path cost: 4
Add more neighbors?  [y/n]: n
Add more vertices?  [y/n]: n
Enter start name: A
Enter end name: D
Сriterion type [add/max]: add
```
### Output:
```bash
Path quality criterion:  6.0
Path: A->B->D
```

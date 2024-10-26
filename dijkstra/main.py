from dijkstra import Dijkstra


def enter_graph() -> dict:
    stop = False
    graph = {}
    while not stop:
        v = input('Enter a vertex name: ')
        graph[v] = {}
        add = True if input('Add neighbors? [y/n] ') == 'y' else False
        while add:
            v_next_name = input('vertex name: ')
            v_next_cost = input('path cost: ')
            graph[v][v_next_name] = float(v_next_cost)
            graph[v_next_name] = {}
            add = True if input('Add more neighbors?  [y/n]: ') == 'y' else False
        stop = False if input('Add more vertices?  [y/n]: ') == 'y' else True
    return graph


def main() -> None:
    graph = enter_graph()
    finder = Dijkstra()
    finder.set_graph(graph)
    start = input('Enter start name: ')
    end = input('Enter end name: ')
    crit = input('Сriterion type [add/max]: ')
    table, path = finder.run(start, end, crit)
    print('Path quality criterion: ', table[end].cost)
    print('Path:', '->'.join(path))


if __name__ == '__main__':
    main()

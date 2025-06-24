def dfs_iterative(adj_list, start):
    visited = set()
    stack = [start]
    result= []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # print(node, end=' ')
            result.append(node)
            # Add neighbors in reverse order to mimic recursive DFS
            for neighbor in reversed(adj_list.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result



from collections import deque

def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

adj_list = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

print("DFS:")
print(*dfs_iterative(adj_list, 1), sep= " ")

bfs(adj_list, 1)

import random

class Node:
    def __init__(self, value: int, name: str, text: str):
        self.value = value
        self.name = name
        self.text = text
        self.next_nodes = []


    def add_next(self, next_node):
        if not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node instance")
        self.next_nodes.append(next_node)


    def __repr__(self):
        return f"Node({self.value})"




class DirectedGraph:
    def __init__(self):
        self.nodes = {}


    def add_node(self, value, name:str, text:str):
        if value not in self.nodes:
            self.nodes[value] = Node(value, name, text)
        return self.nodes[value]


    def add_edge(self, from_value, to_value):
        from_node = self.nodes.get(from_value)
        to_node = self.nodes.get(to_value)
        
        if from_node is None:
            raise ValueError(f"节点 {from_value} 不存在")
        if to_node is None:
            raise ValueError(f"节点 {to_value} 不存在")
        
        from_node.add_next(to_node)


    def dfs(self, start_value):
        visited = set()  # 记录已访问的节点
        self._dfs_helper(self.nodes[start_value], visited)


    def _dfs_helper(self, node, visited):
        if node in visited:
            return
        print(node)  # 访问节点的操作
        visited.add(node)
        
        # 如果存在多个下一跳，则随机选择一个
        if node.next_nodes:
            next_node = random.choice(node.next_nodes)
            self._dfs_helper(next_node, visited)


    def get_node_by_id(self, value):
        # 根据id获取节点
        return self.nodes.get(value)


    def get_next_nodes(self, value):
        # 获取节点指向的所有节点
        node = self.get_node_by_id(value)
        if node is None:
            raise ValueError(f"节点 {value} 不存在")
        return node.next_nodes



if __name__ == '__main__':
    # 示例用法
    graph = DirectedGraph()
    graph.add_node(1, '节点A', '这是节点A')
    graph.add_node(2, '节点B', '这是节点B')
    graph.add_node(3, '节点C', '这是节点C')
    graph.add_node(4, '节点D', '这是节点D')
    graph.add_node(5, '节点E', '这是节点E')


    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)

    # 从节点 'A' 开始遍历
    graph.dfs(1)
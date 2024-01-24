class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def __find(self, node, parent, value): #node - текущий узел; parent - родитель node; value - значение искомое
        if node is None: #узел со значением value не найден
            return None, parent, False
        if value == node.data: #добавлять не нужно, уже есть в дереве
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value) #переход вниз по левой ветви
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value) #вниз по правой
        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        current, parent_of_cur, found = self.__find(self.root, None, obj.data)
        if not found and current:
            if obj.data < current.data:
                current.left = obj
            else:
                current.right = obj

        return obj

    def tree_wide_traverse(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left is not None:
                    vn += [x.left]
                if x.right is not None:
                    vn += [x.right]
            print()
            v = vn


    def tree_traverse_in_order(self, node): #сортирует
        if node is None:
            return
        self.tree_traverse_in_order(node.left)
        print(node.data)
        self.tree_traverse_in_order(node.right)

    def tree_traverse_pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self.tree_traverse_pre_order(node.right)
        self.tree_traverse_pre_order(node.left)

    def tree_traverse_post_order(self, node):
        if node is None:
            return
        self.tree_traverse_post_order(node.right)
        self.tree_traverse_post_order(node.left)
        print(node.data)

    def __del_pepe_One(self, node, parent):

        if parent is None:
            if node.left is None:
                self.root = node.right
            elif node.right is None:
                self.root = node.left

        elif node == parent.left:
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left

        elif node == parent.right:
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left

    def __find_min(self, node, parent):
        if node.left:
           return self.__find_min(self, node.left, node) #идем по левому дереву правого потомка удаляемого элемента в самый низ

        else:
            return node, parent

    def __del_pepe_Zero(self, node, parent):
       if parent.left == node:
           parent.left = None
       elif parent.right == node:
           parent.right = None


    def delete_node(self, key):
        current, parent_of_cur, found = self.__find(self.root, None, key)

        if not found:
            return None
        if current.left is None and current.right is None: #удалить элемент без потомков
            self.__del_pepe_Zero(current, parent_of_cur)
        elif current.left is None or current.right is None:
            self.__del_pepe_One(current, parent_of_cur)
        else:
            right_min, parent_of_min = self.__find_min(current.right, current) #найти минимальный элемент в правом поддереве,
            # начиная от того элемента, который нужно удалить
            current.data = right_min.data
            self.__del_pepe_One(right_min, parent_of_min)

    def set_line(self, line):
        notNumbers = "(), "
        end = 0
        tempLine = line
        a = []
        while len(tempLine):
            if tempLine[end] in notNumbers:
                num = tempLine[:end]
                if num != "":
                    a.append(int(num))
                tempLine = tempLine[end+1:]
                end = 0
            else:
                end += 1
        return a

    def input_tree_data1(self, list):
        for i in range(0, len(list)):
            t.append(Node(list[i]))


print("скобки")
lineOfSkobok = input()
t = Tree()

t.input_tree_data1(t.set_line(lineOfSkobok))

#t.delete_node(1)

t.tree_wide_traverse(t.root)
print("\n")
t.tree_traverse_in_order(t.root)

#8 (3 (1, 6 (4,7)), 10 (, 14(13,)))

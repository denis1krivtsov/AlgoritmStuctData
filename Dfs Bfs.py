def DFS(root):
    """ Обхід дерева в глибину
    :param root: корінь дерева з якого починається обхід
    """

    print(root.key(), end=" -> ")  # Опрацьовуємо корінь

    # запускаємо DFS для всіх дітей кореня
    for child in root.getChildren():
        DFS(child)


def BFS(root):
    """ Обхід дерева в ширину
    :param root: корінь дерева з якого починається обхід
    """
    q = Queue()      # Черга для опрацьованих вузлів
    q.enqueue(root)  # Додаємо у чергу корінь дерева

    while not q.empty():               # Поки черга не порожня
        node = q.dequeue()             # Беремо перший вузол з черги
        print(node.key(), end=" -> ")  # Опрацьовуємо взятий вузол

        # Додаємо в чергу всіх дітей поточного вузла
        for child in node.getChildren():
            q.enqueue(child)

'''def enqueue(self, item):
        """ Додає елемент у чергу (в кінець)
        :param item: елемент, що додається
        :return: None
        """
        self.mItems.append(item)'''
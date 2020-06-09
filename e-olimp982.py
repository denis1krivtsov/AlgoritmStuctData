class VertexBase:
    """ Базовий клас Vertex - вершина.
        Є базовим класом для класу, що описує вершину графа
        Клас містить поля - ключ (ім'я) вершини mKey,
        а також її навантаження (тобто дані) mData.
    """

    def __init__(self, key):
        """ Конструктор створення вершини
        :param key: Ключ вершини
        """
        self.mKey = key    # Ключ (ім'я) вершини
        self.mData = None  # Навантаження (дані) вершини

    def key(self):
        """ Повертає ключ (ім'я) вершини
        :return: Ключ вершини
        """
        return self.mKey

    def setData(self, data):
        """ Встановлює навантаження на вершину
        :param data: Навантаження
        :return: None
        """
        self.mData = data

    def data(self):
        """ Повертає навантаження вершини
        :return: Навантаження вершини
        """
        return self.mData

    def __str__(self):
        """ Зображення вершини у вигляді рядка """
        return str(self.mKey) + ": Data=" + str(self.data())


class Vertex(VertexBase):

    def __init__(self, key):
        """ Конструктор створення вершини
        :param key: Ключ вершини
        """
        super().__init__(key)  # Викликаємо конструктор батьківського класу
        self.mNeighbors = {}   # Список сусідів вершини у вигляді пар (ім'я_сусіда: вага_ребра)

    def addNeighbor(self, vertex, weight=1):
        """ Додати сусіда
        Додає ребро, що сполучає поточну вершину з вершиною Vertex з вагою weight
        Vertex може бути або іншою вершиною, тобто об'єктом класу Vertex
        або ключем (ідентифікатором вершини)
        :param vertex: Вершина-сусід або ключ вершини
        :param weight: Вага ребра
        :return: None
        """
        if isinstance(vertex, VertexBase):  # Якщо Vertex - вершина
            self.mNeighbors[vertex.key()] = weight
        else:                            # Якщо Vertex - ім'я (ключ) вершини
            self.mNeighbors[vertex] = weight

    def neighbors(self):
        """ Повертає список ключів всіх сусідів поточної вершини
        :return: Список ключів всіх сусідів вершини
        """
        return self.mNeighbors.keys()

    def weight(self, neighbor):
        """ Повертає вагу ребра, що сполучає поточну вершину та вершину-сусіда
        :param neighbor: Вершина-сусід
        :return: Вага ребра
        """
        if isinstance(neighbor, VertexBase):  # Якщо aNeighbor - вершина (не ім'я)
            return self.mNeighbors[neighbor.key()]
        else:  # Якщо aNeighbor - ім'я (ключ) сусідньої вершини
            return self.mNeighbors[neighbor]

    def __str__(self):
        """ Зображення вершини у вигляді рядка у разом з усіма її сусідами """
        return super().__str__() + ' connected to: ' + str(self.mNeighbors)



class Graph:
    """ Граф, що задається списком суміжних вершин """

    def __init__(self, oriented=False):
        """ Конструктор графа
        :param oriented: Чи орієнтований граф
        """
        self.mIsOriented = oriented    # Поле чи орієнтований граф
        self.mVertexNumber = 0         # Лічильник вершин у графі
        self.mVertices = {}            # Список (словник) вершин у графі у вигляді пар (ключ: вершина)

    def addVertex(self, vertex):
        """ Додає вершину у граф, якщо така вершина не міститься у ньому
        :param vertex: ключ (тобто ім'я) нової вершини
        :return: True, якщо вершина успішно додана
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = Vertex(vertex)  # створюємо нову вершину з іменем Vertex
        self.mVertices[vertex] = new_vertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1      # Збільшуємо лічильник вершин у графі
        return True

    def getVertex(self, vertex):
        """ Повертає вершину графу, якщо така вершина міститься у графі
        :param vertex: ключ (тобто ім'я) вершини
        :return: Вершина графа
        """
        assert vertex in self

        # Визначаємо ключ вершини, якщо це необхідно
        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.mVertices[key]

    def vertices(self):
        """ Повертає список всіх вершин у графі"""
        return self.mVertices

    def addEdge(self, source, destination, weight=1):
        """ Додавання ребра з кінцями в точках source та destination з вагою weight
        :param source:      Перша вернина
        :param destination: Друга вершина
        :param weight:      Вага ребра
        """
        if source not in self:           # Якщо вершина source ще не міститься у графі
            self.addVertex(source)       # додаємо вершину source
        if destination not in self:      # Якщо вершина destination ще не міститься у графі
            self.addVertex(destination)  # додаємо вершину destination

        # Встановлюємо зв'язок (тобто ребро) між вершинами source та destination
        self[source].addNeighbor(destination, weight)

        if not self.mIsOriented:  # Якщо граф не орієнтований, то треба додати зворотній зв'язок
            self.mVertices[destination].addNeighbor(source, weight)

    def setData(self, vertex, data):
        """ Встановлення навантаження вершини
        :param vertex: ключ вершини або вершина графа
        :param data:   навантаження
        :return: None
        """
        assert vertex in self  # Перевірка чи міститься вершина в графі
        self[vertex].setData(data)

    def getData(self, vertex):
        """ Повертає навантаження вершини
        :param vertex: Вершина або її ключ
        :return: Навантаження вершини
        """
        assert vertex in self  # Перевірка чи міститься вершина в графі
        return self[vertex].data()


    def __contains__(self, vertex):
        """Перевизначення оператора in - перевіряє чи міститься вершина у графі
        :param vertex: Вершина або її ключ
        :return: True, якщо задана вершина міститься у графі
        """
        if isinstance(vertex, Vertex):  # Якщо Vertex - вершина (не ім'я)
            return vertex.key() in self.mVertices
        else:                           # Якщо Vertex - ім'я (ключ) вершини
            return vertex in self.mVertices

    def __iter__(self):
        """ Ітератор для послідовного проходження всіх вершин у графі """
        return iter(self.mVertices.values())

    def __len__(self):
        """ Перевизначення методу len() як кількість вершин у графі
        :return: кількість вершин у графі
        """
        return self.mVertexNumber

    def __str__(self):
        """ Зображення графа разом з усіма вершинами і ребрами у вигляді рядка """
        s = ""
        for vertex in self:
            s = s + str(vertex) + "\n"
        return s

    def __getitem__(self, vertex):
        return self.getVertex(vertex)


def DFS(graph, start):
    """ Обхід графа в глибину починаючи з заданої вершини
    :param graph: Граф
    :param start: Вершина з якої відбувається запуск обходу в глибину
    :return: Множина відвіданих вершин
    """

    visited = set()    # відвідані вершини
    __dfs_helper(graph, visited, start)  # запускаємо DFS з вершини start

    return visited

def __dfs_helper(graph, visited, start):
    """ Рекурсивний допоміжний метод, що реалізує обхід графа в глибину
    :param graph:   Граф
    :param visited: Відвідані вершин
    :param start:   Вершина з якої відбувається запуск обходу в глибину
    """
    # print(start, end=" ")    # Опрацьовуємо елемент на вході
    visited.add(start)       # Помічаємо стартовий елемент як відвіданий
    # для всіх сусідів стартового елементу
    for neighbour in graph[start].neighbors():
        if neighbour not in visited:  # які ще не були відвідані
            __dfs_helper(graph, visited, neighbour)  # запускаємо DFS

def __check_connected_helper(graph: Graph, start):

    visited = DFS(graph, start)
    for v in graph.vertices():
        if v not in visited:
            return False
    return True

def checkConnected(graph: Graph):
    assert not graph.mIsOriented
    return __check_connected_helper(graph, 1)

def exampleNonorientedHandBook():
    g = Graph()  # Створюємо неорієнтований граф
    n, m = map(int, input().split())

    for i in range(n):
        g.addVertex(i+1)

    for i in range(m):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    return g

if __name__ == "__main__":  # Для тестування
    g = exampleNonorientedHandBook()
    c = checkConnected(g)
    if c:
        print("YES")
    else:
        print("No")
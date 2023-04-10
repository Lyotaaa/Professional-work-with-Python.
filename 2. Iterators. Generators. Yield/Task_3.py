class FlatIterator:
    # Вариант № 1
    def __init__(self, list_of_list):
        self.list_of_list = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_of_list:
            self.item = self.list_of_list.pop()
            if not isinstance(self.item, list):
                return self.item
            for i in reversed(self.item):
                self.list_of_list.append(i)
        raise StopIteration

    # Вариант № 2
    # def __init__(self, list_of_list):
    #     self.list_of_list = list_of_list

    # def __iter__(self):
    #     self.iterator = iter(self.list_of_list)
    #     self.result = []
    #     return self

    # def __next__(self):
    #     while True:
    #         try:
    #             self.item = next(self.iterator)
    #         except StopIteration:
    #             if not self.result:
    #                 raise StopIteration
    #             else:
    #                 self.iterator = self.result.pop()
    #                 continue
    #         if isinstance(self.item, list):
    #             self.result.append(self.iterator)
    #             self.iterator = iter(self.item)
    #         else:
    #             return self.item


def test_3():
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
        "!",
    ]

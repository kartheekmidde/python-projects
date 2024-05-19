# Custom Classes
print("-" * 20 + "\n Custom Classes \n" + "-" * 20)


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    # to make the object iterable
    # use built in class iter and set the item to iterate over
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("python")

print(cloud["Python"])

# print(cloud.__tags) - since __tags is private can not access
print(cloud.__dict__)  # to see all attributes of a class
print(cloud._TagCloud__tags)  # can still access underlying attributes

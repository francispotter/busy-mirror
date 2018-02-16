

class Selector:

    CRITERIUM_TYPES = []

    @classmethod
    def add_criterium_type(self, criterium_type):
        self.CRITERIUM_TYPES.append(criterium_type)

    @classmethod
    def get_criterium(self, word):
        for criterium_type in self.CRITERIUM_TYPES:
            if criterium_type.match(word):
                return criterium_type(word)

    def __init__(self, args, default=None):
        self.all = False
        self.criteria = [c for c in [self.get_criterium(w) for w in args] if c]
        if not self.criteria:
            if default == None:
                self.all = True
            else:
                self.criteria = [self.get_criterium(default)]

    def hit(self, index, value):
        return self.all or \
            any([c.hit(index, value) for c in self.criteria])

    def indices(self, elements):
        return [i for i, t in enumerate(elements) if self.hit(i, t)]

    # @staticmethod
    # def select(elements, arguments, default=None):
    #     selector = Selector(arguments, default)
    #     indices = selector.indices(elements)
    #     return indices

class IndexCriterium:
    def match(word):  return str(word).isdigit()
    def __init__(self, word):  self.index = int(word) - 1
    def hit(self, index, value):  return index == self.index

Selector.add_criterium_type(IndexCriterium)


class TagCriterium:
    def match(word):  return str(word).isidentifier()
    def __init__(self, word):  self.tag = str(word).lower()
    def hit(self, index, value):  return '#'+self.tag in value

Selector.add_criterium_type(TagCriterium)

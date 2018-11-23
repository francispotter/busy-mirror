

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

    def __init__(self, args):
        self.criteria = [c for c in [self.get_criterium(w) for w in args] if c]

    def hit(self, index, value):
        if self.criteria:
            return any([c.hit(index, value) for c in self.criteria])
        else:
            return True

    def indices(self, elements):
        return [i for i, t in enumerate(elements) if self.hit(i, t)]

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

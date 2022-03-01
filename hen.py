class new_sets():
    def  __init__(self):
        self.sets = set([])
    def __add__(self,other):
        try:
            self.sets.update(other)
        except:
            self.sets.add(other)
    def __sub__(self,other):
        try:
            for _ in other:
                self.sets.remove(_)
        except:
            self.sets.remove(other)
    def __eq__(self, o: object) -> bool:
        pass
    def __repr__(self):
        return f"{self.sets}"
    def __call__(self):
        return print(f"{self.sets}")

a=new_sets()
a()


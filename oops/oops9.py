class Dad:
    Basketball = 7
class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no. of times"
class Grandson(Son):
    dance = 6
    # def isdance(self):
    #     return f"Jackson Yeah! Yes I dance very awesomely {self.dance} no. of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.Basketball)

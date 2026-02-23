class Vertebrate:

    def __init__(self, backbone = True):
        self.has_backbone = backbone

    def vertebrate_info(self):
        print("vertebrate")


class Aquatic:
    def __init__(self, habitat+"watar"):
         self.habitat = habitat


    def aquatic_info(self):
        print("aquatic")


class Fish(Vartebrate,Aquatic):

    def __init__(self, species , backbone=True, habitat="watar"):

        super().__init__(backbone=backbone)
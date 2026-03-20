class CellPhone :
    # model = "M1"
    # factory = "Samsung"

    def __init__(self, m, f, s):
        self.model = m
        self.factory = f
        self.__serial = s

    def call(self):
        print("전화를 겁니다")

    def receive(self):
        print("전화를 받습니다")

    def send_msg(self):
        print("문자를 보냅니다")
        
    def info(self):
        print(f"모델은 {self.model}이고, {self.factory}에서 만들었습니다.")
        print(f"serial 번호는{self.__serial}입니다.")

p1 = CellPhone("m2","apple","1234")
p2 = CellPhone("m3","samsung","9999")
p2.serial = "8888"

print(p1.info())
print(p1.send_msg())

print(p2.info())
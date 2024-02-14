class Trex:

    def fan():

        print("Khana khaa")

class You:
    def light():
        
        print("light on")

class Office(Trex,You):
    def wire():
        print("Electricity pass")
off=Office()
off.wire()
off.light()
off.fan()

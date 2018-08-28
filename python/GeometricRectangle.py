import msvcrt
#Podemos dividirlo en dos...
Clase GeometricRectangle:
    def _init_(self, width=0, height=0):
        self.width = width
        self.height = height
    def area (self):
        return self.width*self.height
        
msvcrt.getch()

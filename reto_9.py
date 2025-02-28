import math
import time

class Point ():
    def __init__(self,x_y):
        self.x, self.y = x_y

    def punto_(self):
        self.xy = self.x, self.y
        return self.xy

class Linea():

    def __init__ ( self, punto_inicial: tuple ,  punto_final: tuple ):
        self.punto1 = Point(punto_inicial)
        self.punto  = Point(punto_final)
        self.p1  = self.punto1.punto_()
        self.p0 = self.punto.punto_()
        self.distance = float(((self.punto.x - self.punto1.x )**2+(self.punto.y - self.punto1.y )**2)**0.5)
    

    def distancia(self):
        return self.distance


class Shape():
    def __init__(self):
        self._calcular_area = None 
        self._calcular_perimetro = None  
        

    @property
    def calcular_area(self):

        return self.calcular_area

    @property
    def calcular_perimetro(self):
        return self.calcular_perimetro
    
    @classmethod
    def cambiar_tipo_forma(cls, nuevo_tipo):
        cls.tipo_forma = nuevo_tipo
        return

    
    def vertices(self):
        pass

    def aristas(self):
        pass

    def ang_inter(self):
        pass

class Rectangulo(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple, p4: tuple):
        self.puntos = [Point(p1), Point(p2), Point(p3), Point(p4)]
        self.lineas = [Linea(p1, p2), Linea(p2, p3), Linea(p3, p4), Linea(p4, p1)]
        self.lados = [linea.distancia() for linea in self.lineas]

        if not self.es_rectangulo():
            raise ValueError("Los puntos no forman un rectángulo válido.")


    def decorador_de_time(func):
        def wrapper(*args):
            inicio = time.time()
            result = func(*args)
            end_time = time.time()
            print(f"""
Tiempo en ejecucion: 
    {end_time - inicio :.4f} segundos""")
            return result
        return wrapper
    
    def es_rectangulo(self):
        return self.lados[0] == self.lados[2] and self.lados[1] == self.lados[3]
    

    @decorador_de_time
    def calcular_perimetro(self):
        return (self.lados[0] + self.lados[1]) * 2
    
    @decorador_de_time
    def calcular_area(self):
        return self.lados[0] * self.lados[1]
    
    @decorador_de_time
    def vertices(self):
        return f"""
    Sus vertices son los puntos: 
        Punto 1: {self.puntos[0]} 
        Punto 2: {self.puntos[1]} 
        Punto 3: {self.puntos[2]} 
        Punto 4: {self.puntos[3]}
        lista={self.lados}
        """
    
    @decorador_de_time
    def aristas(self):
        return f"""
    Sus aristas son las lineas:
        Linea 1: {self.lados[0]} unidades
        Linea 2: {self.lados[1]} unidades
        Linea 3: {self.lados[2]} unidades
        Linea 4: {self.lados[3]} unidades
        lista={self.lados}
        """
    
    @decorador_de_time
    def ang_inter(self):
        return "es un rectangulo , por lo tanto todos sus angulos interiores miden 90° por vertice"

class Cuadrado(Rectangulo):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple, p4: tuple):
        super().__init__(p1, p2, p3, p4)
        if not self.es_cuadrado():
            raise ValueError("Los puntos no forman un cuadrado válido.")

    def decorador_de_time(func):
        def wrapper(*args):
            inicio = time.time()
            result = func(*args)
            end_time = time.time()
            print(f"tiempo en ejecucion: {end_time - inicio:.4f} segundos")
            return result
        return wrapper
    

    def es_cuadrado(self):
        return self.es_rectangulo() and all(lado == self.lados[0] for lado in self.lados)
    

    def ang_inter(self):
        return "es un cuadrado, por lo tanto todos sus angulos interiores miden 90° por vertice"

class Triangulo(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.p1 =p1; self.p2 =p2; self.p3 =p3
        self.lineas = [Linea(p1, p2), Linea(p2, p3), Linea(p3, p1)]
        self.lados = [linea.distancia() for linea in self.lineas]

        self.perimetro = sum(self.lados)
        s = self.perimetro / 2
        self.area = math.sqrt(s * (s - self.lados[0]) * (s - self.lados[1]) * (s - self.lados[2]))

        if self.area == 0:
            raise ValueError("Los puntos no forman un triangulo valido")

        self.angulos = [
            math.degrees(math.acos((self.lados[1]**2 + self.lados[2]**2 - self.lados[0]**2) /\
                 (2 * self.lados[1] * self.lados[2]))),
            math.degrees(math.acos((self.lados[0]**2 + self.lados[2]**2 - self.lados[1]**2) /\
                 (2 * self.lados[0] * self.lados[2]))),
            math.degrees(math.acos((self.lados[0]**2 + self.lados[1]**2 - self.lados[2]**2) /\
                 (2 * self.lados[0] * self.lados[1])))
        ]
    
    def decorador_de_time(func):
        def wrapper(*args):
            inicio = time.time()
            result = func(*args)
            end_time = time.time()
            print(f"tiempo en ejecucion: {end_time - inicio:.8f} segundos")
            return result
        return wrapper
    
    @decorador_de_time
    def calcular_perimetro(self):
        return f"El perimetro del triangulo es {self.perimetro}"
    
    @decorador_de_time
    def calcular_area(self):
        return f"El area del triangulo es {self.area}"

    def aristas(self):
        return f"""
    Las aristas del triangulo son:
        {self.lados[0]}
        {self.lados[1]}
        {self.lados[2]}
    lista: {self.lados}
    """
    @decorador_de_time
    def vertices(self):
        return f"""
    Los vertices del triangulo son:
        {self.p1} 
        {self.p2} 
        {self.p3}
    Sus lados son: {self.lados}
    """

    def ang_inter(self):
        return f"""
    Aproximadamente los angulos internos son: 
        {self.angulos[0]}°
        {self.angulos[1]}°
        {self.angulos[2]}°
    """


try:
    triangulos = Triangulo((0, 0), (6, 0), (3, 5))
    rectangulos = Rectangulo((2, 0), (0, 0), (0, 3), (2, 3))
    cuadrados = Cuadrado((2, 0), (0, 0), (0, 2), (2, 2))
    # print(rectangulos.aristas())
    # print(triangulos.vertices())
    # print(cuadrados.calcular_area())
    # print(triangulos.calcular_perimetro())
    # print(rectangulos.ang_inter())
    print(cuadrados.calcular_area())


except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
# Reto 09
por fiiin.
aqui es muy sencillo lo que haremos, de acuerdo a la clase de decoradores vamos a decorar nuestra clase shape.
primero agregar property a los datos protegidosa shape.
segundo agregar classmethod 
tercero agregar el decorador de time.

```python
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
```
Aquí lo que hicimos fue volver los protegidos de calcular perimetro y area en atributos, volvimos azules los que eran amarillos.
2.)
```python
class Shape():
    def __init__(self):
        self._calcular_area = None 
        self._calcular_perimetro = None 
    @classmethod
    def cambiar_tipo_forma(cls, nuevo_tipo):
        cls.tipo_forma = nuevo_tipo
        return
```
usamos este etodo que ahora nos va a poder permitir cambiar el tipo de información que se puede agregar, como por ejemplo cambiar un rectangulo a cuadrado 
o viceversa.

3.)
```python
class Rectangulo(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        ...
    def decorador_de_time(func):    #Esta heredada de shape
        def wrapper(*args):
            inicio = time.time()
            result = func(*args)
            end_time = time.time()
            print(f"tiempo en ejecucion: {end_time - inicio:.8f} segundos")
            return result
        return wrapper
    @decorador_de_time
    def calcular_area(self):
        return f"El area del rectangulo es {self.area}"
```
Aqui vemos la herencia de shape a rectangulo, usando el decorador en el metodo de, "calcular_area()" que nos permitira saber el tiempo de uso de este.
todo el codigo esta arriba, dónde lo podran ver y detallar más a profundidad.

## Fin:

La verdaad... ya se acabo, me fue re mal en el examen pero ps bueno, jajaja, me gusto mucho hacer tareas por acá, muy contrario a classroom. La asignatura de por si me gusto mucho,
aunque no me fue muy bien en los examenes(ja) creo que aprendi mucho, creo que era necesario perder esos examenes con un bonito 2, para adentrarme más en la programación, 
se que en mi carrera vere mucha programación, nose si python me ayudara o no, pero si puedo decir que tengo buenas bases para iniciar en cualquier lenguaje de programación.
En fin... ya me voy, bye.


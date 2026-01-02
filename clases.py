
# --- #: Clase Robot :# --- #

class Robot:
    def __init__(self, nombre, detalles):
        self.nombre = nombre
        self.detalles = detalles
        self.arma_izquierda = None
        self.arma_derecha = None
    
    def __str__(self):
        return f"Robot: {self.nombre} | Detalles: {self.detalles}"
        
    def equipar_arma_izquierda(self, arma):
        self.arma_izquierda = arma
        
    def equipar_arma_derecha(self, arma):
        self.arma_derecha = arma

    def quitar_arma_izquierda(self):
        self.arma_izquierda = None
        
    def quita_arma_derecha(self):
        self.arma_derecha = None
    
# --- #: Clase Arma :# --- #
        
class Arma:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def __str__(self):
        return f"Arma: {self.nombre} | Tipo: {self.tipo}"
    
# --- #: Clase Combate :# --- #

class Combate:
    def __init__(self, Robot_A, Robot_B, fecha, arena, control, modo):
        self.combate = f'{Robot_A} vs {Robot_B}'
        self.robot_a = Robot_A
        self.robot_b = Robot_B
        self.fecha = fecha
        self.modo = modo
        self.arena = arena
        self.control = control
        
        
    def __str__(self):
        return f'Combate: {self.combate} | Fecha: {self.fecha} | Modo: {self.modo} | Arena: {self.arena} | Control: {self.control}'
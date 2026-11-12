# 2. MÓDULO SERVICIO 

from abc import abstractmethod


class ABC:
    ...

class Servicio(ABC):
    """Clase abstracta base para los servicios de Software FJ."""
    
    def __init__(self, descripcion):
        self.descripcion = descripcion

    @abstractmethod
    def calcular_costo(self):
        pass

    def describir(self):
        return f"Servicio: {self.descripcion}"

    def validar_parametros(self):
        return True


class ReservaSala(Servicio):
    """Servicio 1: Reserva de salas físicas."""
    def __init__(self, fila, asiento):
        super().__init__("Reserva de Sala")
        self.fila = fila
        self.asiento = asiento

    def calcular_costo(self, descuento=0.0):
        base = 8000 if self.fila in [1, 2] else (6000 if self.fila in [3, 4] else 4000)
        return base * (1 - descuento)

    def describir(self):
        return f"Sala - Fila {self.fila}, Asiento {self.asiento}"

    def validar_parametros(self):
        return 1 <= self.fila <= 5 and 1 <= self.asiento <= 10


class AlquilerEquipo(Servicio):
    """Servicio 2: Alquiler de equipos tecnológicos."""
    def __init__(self, nombre_equipo, horas):
        super().__init__("Alquiler de Equipo")
        self.nombre_equipo = nombre_equipo
        self.horas = horas

    def calcular_costo(self, impuesto=1.19):
        return (5000 * self.horas) * impuesto

    def describir(self):
        return f"Equipo: {self.nombre_equipo} ({self.horas} hrs)"

    def validar_parametros(self):
        return len(self.nombre_equipo.strip()) > 0 and self.horas > 0


class AsesoriaEspecializada(Servicio):
    """Servicio 3: Asesorías técnicas."""
    def __init__(self, tema, nivel):
        super().__init__("Asesoría Especializada")
        self.tema = tema
        self.nivel = nivel  # 1: Básico, 2: Avanzado

    def calcular_costo(self, recargo=1.2):
        return 15000 * (recargo if self.nivel > 1 else 1.0)

    def describir(self):
        return f"Asesoría en {self.tema} (Nivel {self.nivel})"

    def validar_parametros(self):
        return len(self.tema.strip()) > 0 and self.nivel in [1, 2]
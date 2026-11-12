class Cliente:
    """Clase para manejar los datos y validaciones del cliente."""
    
    def __init__(self, nombre, documento, correo):
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo

    def validar_nombre(self):
        return len(self.__nombre.strip()) > 0

    def validar_documento(self):
        return str(self.__documento).isdigit() and len(str(self.__documento)) >= 6

    def validar_correo(self):
        return "@" in self.__correo and "." in self.__correo

    def mostrar_datos(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento}"
        # 2. MÓDULO SERVICIO (servicio.py)

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

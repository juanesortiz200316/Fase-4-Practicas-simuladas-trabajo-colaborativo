# 3. MÓDULO RESERVA 

class Reserva:
    """Clase para gestionar el estado y procesamiento de reservas."""
    
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.cliente.validar_nombre() and self.servicio.validar_parametros():
                self.estado = "Confirmada"
                return True
            else:
                raise ValueError("Parámetros inválidos.")
        except Exception:
            self.estado = "Cancelada"
            raise

    def cancelar(self):
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
            return True
        return False

    def procesar(self):
        if self.estado == "Confirmada":
            total = self.servicio.calcular_costo()
            self.estado = "Procesada"
            return total
        raise RuntimeError("La reserva no está confirmada.")

    def mostrar_reserva(self):
        return f"[{self.estado}] {self.cliente.mostrar_datos()} -> {self.servicio.describir()}"

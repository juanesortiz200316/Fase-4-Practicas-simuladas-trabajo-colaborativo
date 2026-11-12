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
    
   
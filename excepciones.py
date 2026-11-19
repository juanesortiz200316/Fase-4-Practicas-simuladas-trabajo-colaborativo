# 4. MÓDULO EXCEPCIONES (excepciones.py)

class ErrorSoftwareFJ(Exception):
    """Clase base para excepciones personalizadas[cite: 16]."""
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass

class ReservaInvalidaError(ErrorSoftwareFJ):
    pass
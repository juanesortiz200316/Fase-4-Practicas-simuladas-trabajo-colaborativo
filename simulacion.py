from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

def ejecucion_simulaciones():
    print("\n--- INICIO DE 10 SIMULACIONES (VÁLIDAS E INVÁLIDAS) ---")
    
    pruebas = [
        (Cliente("Ana Gómez", "102345", "ana@mail.com"), ReservaSala(1, 4), True),
        (Cliente("Luis Pérez", "987654", "luis@mail.com"), AlquilerEquipo("Laptop", 2), True),
        (Cliente("Sofía Ruiz", "456789", "sofia@mail.com"), AsesoriaEspecializada("Redes", 2), True),
        (Cliente("Carlos Vives", "321654", "carlos@mail.com"), ReservaSala(5, 10), True),
        (Cliente("Maria Gil", "789123", "maria@mail.com"), AlquilerEquipo("Proyector", 1), True),
        (Cliente("Pedro Mal", "111", "pedro@mail.com"), ReservaSala(6, 12), False),
        (Cliente("Marta Mal", "222222", "marta@mail.com"), AlquilerEquipo("", 0), False),
        (Cliente("Juan Mal", "333333", "juan@mail.com"), AsesoriaEspecializada("BD", 5), False),
        (Cliente("Error Doc", "ABC", "err@mail.com"), ReservaSala(2, 3), False),
        (Cliente("Nulo", "999999", "test@mail.com"), None, False)
    ]

    for i, (cli, serv, es_valido) in enumerate(pruebas, 1):
        try:
            print(f"\n[Prueba {i}] Ejecutando...")
            if serv is None:
                raise ValueError("Servicio nulo.")
            reserva = Reserva(cli, serv)
            
            try:
                reserva.confirmar()
                total = reserva.procesar()
            except Exception as e:
                raise RuntimeError(f"Falla en proceso: {e}")
            else:
                print(f"-> ÉXITO: Total a pagar: ${total}")
            finally:
                print(f"-> Estado final: {reserva.estado}")
                
        except Exception as e:
            if not es_valido:
                print(f"-> ÉXITO CONTROLADO (Error atrapado correctamente): {e}")
            else:
                print(f"-> FALLO INESPERADO: {e}")
    print("\n--- FIN DE SIMULACIONES ---\n")

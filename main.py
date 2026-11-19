# 7. MÓDULO PRINCIPAL
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from logger_config import registrar_evento, registrar_error
from simulacion import ejecucion_simulaciones

def main():
    registrar_evento("Sistema Software FJ iniciado.")
    opcion = 0

    while opcion != 5:
        print("\n==============================")
        print("   SOFTWARE FJ - MENÚ         ")
        print("==============================")
        print("1. Reservar Sala")
        print("2. Alquilar Equipo")
        print("3. Solicitar Asesoría")
        print("4. Ejecutar 10 Simulaciones")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            try:
                nom = input("Nombre: ")
                doc = input("Documento: ")
                cor = input("Correo: ")
                cli = Cliente(nom, doc, cor)
                
                f = int(input("Fila (1-5): "))
                a = int(input("Asiento (1-10): "))
                serv = ReservaSala(f, a)

                res = Reserva(cli, serv)
                res.confirmar()
                total = res.procesar()
                print(f"¡Reserva exitosa! Total: ${total}")
                registrar_evento(f"Reserva de sala exitosa para {nom}")
            except Exception as e:
                print(f"Error: {e}")
                registrar_error(e)

        elif opcion == 2:
            try:
                nom = input("Nombre: ")
                doc = input("Documento: ")
                cor = input("Correo: ")
                cli = Cliente(nom, doc, cor)
                
                eq = input("Nombre equipo: ")
                hrs = int(input("Horas: "))
                serv = AlquilerEquipo(eq, hrs)

                res = Reserva(cli, serv)
                res.confirmar()
                total = res.procesar()
                print(f"¡Alquiler exitoso! Total: ${total}")
                registrar_evento(f"Alquiler de equipo exitoso para {nom}")
            except Exception as e:
                print(f"Error: {e}")
                registrar_error(e)

        elif opcion == 3:
            try:
                nom = input("Nombre: ")
                doc = input("Documento: ")
                cor = input("Correo: ")
                cli = Cliente(nom, doc, cor)
                
                tema = input("Tema asesoría: ")
                nivel = int(input("Nivel (1: Básico, 2: Avanzado): "))
                serv = AsesoriaEspecializada(tema, nivel)

                res = Reserva(cli, serv)
                res.confirmar()
                total = res.procesar()
                print(f"¡Asesoría exitosa! Total: ${total}")
                registrar_evento(f"Asesoría exitosa para {nom}")
            except Exception as e:
                print(f"Error: {e}")
                registrar_error(e)

        elif opcion == 4:
            ejecucion_simulaciones()

        elif opcion == 5:
            print("Saliendo del sistema...")
            registrar_evento("Sistema cerrado.")

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

import datetime

def configurar_logger():
    return "Logger listo."

def registrar_evento(mensaje):
    tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[INFO] {tiempo} - {mensaje}"
    print(log)
    try:
        with open("sistema_log.txt", "a", encoding="utf-8") as f:
            f.write(log + "\n")
    except Exception:
        pass

def registrar_error(error):
    tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[ERROR] {tiempo} - {str(error)}"
    print(log)
    try:
        with open("sistema_log.txt", "a", encoding="utf-8") as f:
            f.write(log + "\n")
    except Exception:
        pass

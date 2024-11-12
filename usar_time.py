import time

class TimeExamples:
    def __init__(self):
        # Inicializa la clase, definiendo un ejemplo de tiempo inicial para algunos cálculos
        self.timestamp = time.time()  # Obtiene el tiempo actual en segundos desde el epoch (1 de enero de 1970)
    
    def obtener_tiempo_actual(self):
        """
        Muestra cómo obtener el tiempo actual en segundos desde el epoch.
        """
        tiempo_actual = time.time()
        print("Tiempo actual en segundos desde el epoch:", tiempo_actual)
    
    def pausa_espera(self, segundos):
        """
        Realiza una pausa en la ejecución del programa durante un número de segundos específicos.
        """
        print(f"Esperando {segundos} segundos...")
        time.sleep(segundos)
        print("Espera completada.")
    
    def conversiones_estructuradas(self):
        """
        Convierte el tiempo en segundos a una estructura de tiempo detallada y viceversa.
        """
        # time.localtime() convierte un timestamp a la hora local en una estructura de tiempo
        hora_local = time.localtime(self.timestamp)
        print("Hora local (struct_time):", hora_local)

        # time.gmtime() convierte un timestamp a UTC en una estructura de tiempo
        hora_utc = time.gmtime(self.timestamp)
        print("Hora UTC (struct_time):", hora_utc)

        # time.mktime() convierte una estructura de tiempo a segundos desde el epoch
        timestamp_local = time.mktime(hora_local)
        print("Timestamp convertido desde struct_time (hora local):", timestamp_local)

    def obtener_zona_horaria(self):
        """
        Obtiene la zona horaria local en segundos de desplazamiento desde UTC y el nombre de la zona.
        """
        # time.timezone es el desplazamiento de la zona horaria en segundos desde UTC
        zona_horaria_segundos = -time.timezone if time.localtime().tm_isdst == 0 else -time.altzone
        nombre_zona_horaria = time.tzname
        print("Desplazamiento de la zona horaria en segundos desde UTC:", zona_horaria_segundos)
        print("Nombre de la zona horaria:", nombre_zona_horaria)

    def formatear_fecha_tiempo(self):
        """
        Formatea la fecha y hora actuales como string en un formato específico.
        """
        hora_formateada = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Fecha y hora formateadas:", hora_formateada)

    def parsear_fecha_tiempo(self):
        """
        Convierte un string de fecha y hora en una estructura de tiempo (struct_time).
        """
        fecha_str = "2023-11-10 15:30:45"
        struct_tiempo = time.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        print("Fecha y hora parseadas desde string (struct_time):", struct_tiempo)

    def medir_duracion_proceso(self):
        """
        Mide la duración de un proceso usando time.perf_counter para alta precisión.
        """
        inicio = time.perf_counter()
        # Simulación de un proceso con una breve pausa
        time.sleep(1)
        duracion = time.perf_counter() - inicio
        print("Duración del proceso en segundos:", duracion)

    def medir_duracion_cpu(self):
        """
        Mide el tiempo de CPU usado por el proceso actual usando time.process_time.
        """
        inicio_cpu = time.process_time()
        # Simulación de una carga de trabajo para la CPU
        for _ in range(1000000):
            pass
        duracion_cpu = time.process_time() - inicio_cpu
        print("Tiempo de CPU usado en segundos:", duracion_cpu)

    def ejecutar_ejemplos(self):
        """
        Ejecuta todos los métodos de ejemplo para mostrar las funcionalidades del módulo time.
        """
        print("=== Tiempo Actual ===")
        self.obtener_tiempo_actual()

        print("\n=== Pausa o Espera ===")
        self.pausa_espera(2)  # Pausa de ejemplo de 2 segundos

        print("\n=== Conversiones Estructuradas ===")
        self.conversiones_estructuradas()

        print("\n=== Información de Zona Horaria ===")
        self.obtener_zona_horaria()

        print("\n=== Formateo de Fecha y Hora ===")
        self.formatear_fecha_tiempo()

        print("\n=== Parseo de Fecha y Hora ===")
        self.parsear_fecha_tiempo()

        print("\n=== Medición de Duración de un Proceso ===")
        self.medir_duracion_proceso()

        print("\n=== Medición de Duración de CPU ===")
        self.medir_duracion_cpu()


# Crear instancia de la clase y ejecutar ejemplos
ejemplos_time = TimeExamples()
ejemplos_time.ejecutar_ejemplos()

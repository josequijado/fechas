import datetime

class DateTimeExamples:
    def __init__(self):
        # Inicializa la clase y define algunos ejemplos básicos de fecha y hora
        self.fecha = datetime.date(2023, 11, 10)
        self.hora = datetime.time(15, 30, 45)
        self.fecha_hora = datetime.datetime(2023, 11, 10, 15, 30, 45)
    
    def crear_fecha_hora(self):
        """
        Ejemplo de creación de objetos de fecha, hora y fecha-hora.
        """
        print("Fecha específica:", self.fecha)
        print("Hora específica:", self.hora)
        print("Fecha y hora específica:", self.fecha_hora)

    def obtener_fecha_hora_actual(self):
        """
        Obtiene la fecha y hora actuales usando el método now() de datetime.
        """
        ahora = datetime.datetime.now()
        print("Fecha y hora actuales:", ahora)

    def sumar_restar_tiempo(self):
        """
        Muestra cómo usar timedelta para sumar o restar tiempo a objetos datetime.
        """
        diez_dias_despues = self.fecha_hora + datetime.timedelta(days=10)
        print("10 días después de la fecha dada:", diez_dias_despues)

        una_semana_antes = self.fecha_hora - datetime.timedelta(weeks=1)
        print("1 semana antes de la fecha dada:", una_semana_antes)

    def calcular_diferencia(self):
        """
        Calcula la diferencia en días y segundos entre dos fechas y horas usando timedelta.
        """
        otra_fecha = datetime.datetime.now()
        diferencia = otra_fecha - self.fecha_hora
        print("Diferencia en días:", diferencia.days)
        print("Diferencia en segundos:", diferencia.total_seconds())

    def formatear_fecha_hora(self):
        """
        Formatea un objeto datetime a un string en un formato específico usando strftime.
        """
        formato = self.fecha_hora.strftime("%A, %d de %B de %Y %H:%M:%S")
        print("Fecha formateada:", formato)

    def parsear_fecha_hora(self):
        """
        Convierte un string a un objeto datetime usando strptime.
        """
        fecha_str = "10/11/2023 15:30:45"
        fecha_parseada = datetime.datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
        print("Fecha parseada desde string:", fecha_parseada)

    def manejo_zonas_horarias(self):
        """
        Demuestra cómo trabajar con zonas horarias básicas en datetime, usando UTC y zonas horarias personalizadas.
        """
        utc = datetime.timezone.utc
        fecha_hora_utc = datetime.datetime.now(utc)
        print("Fecha y hora en UTC:", fecha_hora_utc)

        zona_madrid = datetime.timezone(datetime.timedelta(hours=1))
        fecha_hora_madrid = datetime.datetime.now(zona_madrid)
        print("Fecha y hora en Madrid (UTC+1):", fecha_hora_madrid)

        # Convertir una fecha UTC a una zona horaria específica
        fecha_aware = self.fecha_hora.replace(tzinfo=utc)
        fecha_madrid = fecha_aware.astimezone(zona_madrid)
        print("Fecha UTC convertida a Madrid:", fecha_madrid)

    def detalles_avanzados_fecha_hora(self):
        """
        Obtiene detalles avanzados de la fecha, como el número de semana y el día en el año.
        """
        semana_del_anio = self.fecha.isocalendar()[1]
        print("Número de semana del año:", semana_del_anio)

        dia_del_anio = self.fecha.timetuple().tm_yday
        print("Número de día en el año:", dia_del_anio)

    def combinar_fecha_hora(self):
        """
        Combina un objeto date y un objeto time en un objeto datetime usando datetime.combine.
        """
        fecha_hora_combinada = datetime.datetime.combine(self.fecha, self.hora)
        print("Fecha y hora combinadas:", fecha_hora_combinada)

    def modificar_fecha_hora(self):
        """
        Modifica partes de un objeto datetime usando replace.
        """
        fecha_modificada = self.fecha_hora.replace(year=2025, month=12)
        print("Fecha y hora con año y mes modificados:", fecha_modificada)

    def desde_timestamp(self):
        """
        Convierte un timestamp (marca de tiempo) en un objeto date o datetime.
        """
        timestamp = 1699575645
        fecha_desde_timestamp = datetime.date.fromtimestamp(timestamp)
        fecha_hora_desde_timestamp = datetime.datetime.fromtimestamp(timestamp)
        print("Fecha desde timestamp:", fecha_desde_timestamp)
        print("Fecha y hora desde timestamp:", fecha_hora_desde_timestamp)

    def obtener_ordinal(self):
        """
        Obtiene el número ordinal de una fecha (días desde el 1 de enero del año 1).
        """
        ordinal = self.fecha.toordinal()
        print("Número ordinal de la fecha:", ordinal)

    def limites_fecha_hora(self):
        """
        Muestra los límites de las fechas y horas posibles con date y datetime.
        """
        print("Fecha mínima:", datetime.date.min)
        print("Fecha máxima:", datetime.date.max)
        print("Fecha y hora mínima:", datetime.datetime.min)
        print("Fecha y hora máxima:", datetime.datetime.max)

    def utc_from_timestamp(self):
        """
        Convierte un timestamp en UTC usando utcfromtimestamp.
        """
        timestamp = 1699575645
        fecha_hora_utc = datetime.datetime.utcfromtimestamp(timestamp)
        print("Fecha y hora UTC desde timestamp:", fecha_hora_utc)

    def ejecutar_ejemplos(self):
        """
        Ejecuta todos los métodos de ejemplo para mostrar las funcionalidades del módulo datetime.
        """
        print("=== Creación de Fecha y Hora ===")
        self.crear_fecha_hora()

        print("\n=== Fecha y Hora Actuales ===")
        self.obtener_fecha_hora_actual()

        print("\n=== Sumar y Restar Tiempo ===")
        self.sumar_restar_tiempo()

        print("\n=== Cálculo de Diferencia ===")
        self.calcular_diferencia()

        print("\n=== Formateo de Fecha y Hora ===")
        self.formatear_fecha_hora()

        print("\n=== Parseo de Fecha y Hora ===")
        self.parsear_fecha_hora()

        print("\n=== Manejo de Zonas Horarias ===")
        self.manejo_zonas_horarias()

        print("\n=== Detalles Avanzados de Fecha ===")
        self.detalles_avanzados_fecha_hora()

        print("\n=== Combinación de Fecha y Hora ===")
        self.combinar_fecha_hora()

        print("\n=== Modificación de Fecha y Hora ===")
        self.modificar_fecha_hora()

        print("\n=== Conversión desde Timestamp ===")
        self.desde_timestamp()

        print("\n=== Número Ordinal de Fecha ===")
        self.obtener_ordinal()

        print("\n=== Límites de Fecha y Hora ===")
        self.limites_fecha_hora()

        print("\n=== Conversión UTC desde Timestamp ===")
        self.utc_from_timestamp()


# Crear instancia de la clase y ejecutar ejemplos
ejemplos_datetime = DateTimeExamples()
ejemplos_datetime.ejecutar_ejemplos()

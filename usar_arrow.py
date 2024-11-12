import arrow

class ArrowExamples:
    def __init__(self):
        # Fecha y hora base para los ejemplos, en UTC
        self.fecha_hora_base = arrow.utcnow()
    
    def obtener_fecha_hora_actual(self):
        """
        Muestra la fecha y hora actuales en UTC y en la zona horaria local.
        """
        fecha_hora_utc = arrow.utcnow()
        fecha_hora_local = arrow.now()
        print("Fecha y hora actual en UTC:", fecha_hora_utc)
        print("Fecha y hora actual en la zona horaria local:", fecha_hora_local)

    def crear_fecha_desde_string(self, fecha_str):
        """
        Convierte un string en un objeto Arrow utilizando un formato específico.
        """
        fecha_convertida = arrow.get(fecha_str, "YYYY-MM-DD HH:mm:ss")
        print("Fecha convertida desde string:", fecha_convertida)

    def manipular_fecha_hora(self):
        """
        Realiza operaciones de manipulación de tiempo, como sumar días, semanas y meses.
        """
        fecha_siguiente_dia = self.fecha_hora_base.shift(days=1)
        fecha_siguiente_mes = self.fecha_hora_base.shift(months=1)
        print("Fecha un día después:", fecha_siguiente_dia)
        print("Fecha un mes después:", fecha_siguiente_mes)

    def formatear_fecha_hora(self):
        """
        Formatea un objeto Arrow en un string con un formato específico.
        """
        fecha_formateada = self.fecha_hora_base.format("YYYY-MM-DD HH:mm:ss")
        print("Fecha formateada:", fecha_formateada)

    def convertir_zona_horaria(self, zona):
        """
        Convierte la fecha y hora base a otra zona horaria.
        """
        fecha_convertida = self.fecha_hora_base.to(zona)
        print(f"Fecha y hora en {zona}:", fecha_convertida)

    def obtener_fecha_hora_relativa(self):
        """
        Muestra la fecha y hora en términos relativos (ej., 'hace 3 días').
        """
        fecha_hace_dias = self.fecha_hora_base.shift(days=-3)
        print("Fecha y hora relativa:", fecha_hace_dias.humanize())

    def ejecutar_ejemplos(self):
        """
        Ejecuta todos los métodos de ejemplo para mostrar las funcionalidades del módulo arrow.
        """
        print("=== Fecha y Hora Actuales ===")
        self.obtener_fecha_hora_actual()

        print("\n=== Creación de Fecha desde String ===")
        self.crear_fecha_desde_string("2023-11-10 15:30:45")

        print("\n=== Manipulación de Fecha y Hora ===")
        self.manipular_fecha_hora()

        print("\n=== Formateo de Fecha y Hora ===")
        self.formatear_fecha_hora()

        print("\n=== Conversión de Zona Horaria ===")
        self.convertir_zona_horaria("America/New_York")

        print("\n=== Fecha y Hora Relativa ===")
        self.obtener_fecha_hora_relativa()


# Crear instancia de la clase y ejecutar ejemplos
ejemplos_arrow = ArrowExamples()
ejemplos_arrow.ejecutar_ejemplos()

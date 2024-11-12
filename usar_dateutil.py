from datetime import datetime, timedelta
from dateutil import parser, relativedelta, tz

class DateutilExamples:
    def __init__(self):
        # Fecha y hora base para los ejemplos
        self.fecha_hora_base = datetime(2023, 11, 10, 15, 30, 45)
    
    def parsear_fecha_desde_string(self, fecha_str):
        """
        Convierte un string en un objeto datetime usando dateutil.parser.parse.
        """
        fecha_parseada = parser.parse(fecha_str)
        print("Fecha y hora parseada desde string:", fecha_parseada)

    def sumar_periodos_relativos(self):
        """
        Suma periodos de tiempo relativos a una fecha, como meses, años, etc., usando relativedelta.
        """
        fecha_siguiente_mes = self.fecha_hora_base + relativedelta.relativedelta(months=1)
        fecha_proximo_anio = self.fecha_hora_base + relativedelta.relativedelta(years=1)
        print("Fecha un mes después:", fecha_siguiente_mes)
        print("Fecha un año después:", fecha_proximo_anio)

    def calcular_diferencia_relativa(self, fecha_futura):
        """
        Calcula la diferencia relativa entre dos fechas en términos de años, meses y días.
        """
        diferencia = relativedelta.relativedelta(fecha_futura, self.fecha_hora_base)
        print("Diferencia relativa - Años:", diferencia.years)
        print("Diferencia relativa - Meses:", diferencia.months)
        print("Diferencia relativa - Días:", diferencia.days)

    def ajustar_fecha_fin_mes(self):
        """
        Ajusta una fecha al último día del mes actual usando relativedelta.
        """
        fin_mes = self.fecha_hora_base + relativedelta.relativedelta(day=31)
        print("Fecha ajustada al final del mes:", fin_mes)

    def zonas_horarias_con_dateutil(self):
        """
        Trabaja con zonas horarias usando dateutil.tz.
        """
        # Definir zonas horarias
        zona_nueva_york = tz.gettz("America/New_York")
        zona_londres = tz.gettz("Europe/London")

        # Asignar la zona horaria a la fecha base
        fecha_ny = self.fecha_hora_base.replace(tzinfo=zona_nueva_york)
        print("Fecha y hora en Nueva York:", fecha_ny)

        # Convertir a otra zona horaria
        fecha_londres = fecha_ny.astimezone(zona_londres)
        print("Fecha y hora convertida a Londres:", fecha_londres)

    def manejar_repeticion_eventos(self, inicio, frecuencia, total_eventos):
        """
        Genera una lista de fechas recurrentes con una frecuencia específica usando timedelta.
        """
        eventos = [inicio + timedelta(days=frecuencia * i) for i in range(total_eventos)]
        print("Fechas de eventos recurrentes:")
        for evento in eventos:
            print(evento)

    def ejecutar_ejemplos(self):
        """
        Ejecuta todos los métodos de ejemplo para mostrar las funcionalidades del módulo dateutil.
        """
        print("=== Parseo de Fecha desde String ===")
        self.parsear_fecha_desde_string("2023-11-10 15:30:45")

        print("\n=== Suma de Periodos Relativos ===")
        self.sumar_periodos_relativos()

        print("\n=== Cálculo de Diferencia Relativa ===")
        fecha_futura = datetime(2025, 11, 10, 15, 30, 45)
        self.calcular_diferencia_relativa(fecha_futura)

        print("\n=== Ajuste de Fecha al Fin de Mes ===")
        self.ajustar_fecha_fin_mes()

        print("\n=== Manejo de Zonas Horarias con dateutil ===")
        self.zonas_horarias_con_dateutil()

        print("\n=== Manejo de Repetición de Eventos ===")
        inicio_evento = datetime(2023, 11, 10)
        self.manejar_repeticion_eventos(inicio_evento, frecuencia=7, total_eventos=5)


# Crear instancia de la clase y ejecutar ejemplos
ejemplos_dateutil = DateutilExamples()
ejemplos_dateutil.ejecutar_ejemplos()

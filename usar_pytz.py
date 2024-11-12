import datetime
import pytz

class PytzExamples:
    def __init__(self):
        # Inicializa la clase con una fecha y hora base en UTC para los ejemplos
        self.fecha_hora_base = datetime.datetime(2023, 11, 10, 15, 30, 45, tzinfo=pytz.UTC)

    def listar_zonas_horarias(self):
        """
        Muestra todas las zonas horarias disponibles en pytz.
        """
        zonas = pytz.all_timezones
        print("Lista de todas las zonas horarias disponibles en pytz:")
        for zona in zonas[:10]:  # Muestra solo las primeras 10 para no saturar la salida
            print(zona)
        print("...")  # Indica que hay muchas más zonas horarias

    def convertir_a_zona_horaria(self, zona):
        """
        Convierte la fecha y hora base a una zona horaria específica.
        """
        zona_horaria = pytz.timezone(zona)
        fecha_convertida = self.fecha_hora_base.astimezone(zona_horaria)
        print(f"Fecha y hora en {zona}:", fecha_convertida)

    def manejo_de_horario_verano(self, zona):
        """
        Demuestra cómo pytz maneja el horario de verano (DST) en una zona horaria específica.
        """
        zona_horaria = pytz.timezone(zona)
        # Una fecha que normalmente tendría horario de verano
        fecha_dst = datetime.datetime(2023, 6, 1, 12, 0, 0)
        fecha_converted_dst = zona_horaria.localize(fecha_dst, is_dst=None)
        print(f"Fecha con horario de verano aplicado en {zona}:", fecha_converted_dst)

    def convertir_a_utc(self, fecha_hora_local, zona):
        """
        Convierte una fecha y hora local a UTC.
        """
        zona_horaria = pytz.timezone(zona)
        fecha_localizada = zona_horaria.localize(fecha_hora_local)
        fecha_utc = fecha_localizada.astimezone(pytz.UTC)
        print("Fecha y hora en UTC:", fecha_utc)

    def zonas_horarias_comunes(self):
        """
        Muestra ejemplos de zonas horarias comunes y sus conversiones.
        """
        zonas_comunes = ["Europe/Madrid", "America/New_York", "Asia/Tokyo"]
        for zona in zonas_comunes:
            self.convertir_a_zona_horaria(zona)

    def obtener_zona_horaria_local(self):
        """
        Obtiene la zona horaria local y convierte la fecha base a esta zona.
        """
        zona_local = pytz.timezone('Europe/Madrid')  # Como ejemplo, usamos la zona horaria de Madrid
        fecha_local = self.fecha_hora_base.astimezone(zona_local)
        print("Fecha y hora en la zona horaria local (Madrid):", fecha_local)

    def ejecutar_ejemplos(self):
        """
        Ejecuta todos los métodos de ejemplo para mostrar las funcionalidades del módulo pytz.
        """
        print("=== Lista de Zonas Horarias Disponibles ===")
        self.listar_zonas_horarias()

        print("\n=== Conversión a Zona Horaria ===")
        self.convertir_a_zona_horaria("America/New_York")

        print("\n=== Manejo del Horario de Verano (DST) ===")
        self.manejo_de_horario_verano("Europe/London")

        print("\n=== Conversión a UTC ===")
        fecha_hora_local = datetime.datetime(2023, 11, 10, 12, 0, 0)
        self.convertir_a_utc(fecha_hora_local, "America/Los_Angeles")

        print("\n=== Zonas Horarias Comunes ===")
        self.zonas_horarias_comunes()

        print("\n=== Zona Horaria Local ===")
        self.obtener_zona_horaria_local()


# Crear instancia de la clase y ejecutar ejemplos
ejemplos_pytz = PytzExamples()
ejemplos_pytz.ejecutar_ejemplos()

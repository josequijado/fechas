import calendar

class CalendarExamples:
    def __init__(self, year=2023, month=11):
        # Inicializa la clase con un año y mes específicos para los ejemplos
        self.year = year
        self.month = month
    
    def mostrar_calendario_mes(self):
        """
        Muestra el calendario de un mes específico en formato de texto.
        """
        cal_mes = calendar.month(self.year, self.month)
        print(f"Calendario de {self.month}/{self.year}:\n{cal_mes}")

    def mostrar_calendario_anio(self):
        """
        Muestra el calendario completo de un año en formato de texto.
        """
        cal_anio = calendar.calendar(self.year)
        print(f"Calendario del año {self.year}:\n{cal_anio}")

    def comprobar_bisiesto(self):
        """
        Verifica si un año es bisiesto.
        """
        es_bisiesto = calendar.isleap(self.year)
        print(f"¿Es {self.year} un año bisiesto?:", es_bisiesto)

    def contar_bisiestos(self, start_year, end_year):
        """
        Cuenta cuántos años bisiestos hay en un rango de años.
        """
        bisiestos = calendar.leapdays(start_year, end_year)
        print(f"Años bisiestos entre {start_year} y {end_year}:", bisiestos)

    def primer_dia_mes_y_dias_totales(self):
        """
        Muestra el primer día de la semana y el número de días en un mes específico.
        """
        primer_dia, dias_totales = calendar.monthrange(self.year, self.month)
        print(f"Primer día del mes {self.month}/{self.year} (0=Lunes):", primer_dia)
        print(f"Número total de días en el mes {self.month}/{self.year}:", dias_totales)

    def generar_iterador_dias_mes(self):
        """
        Genera un iterador sobre las semanas de un mes específico.
        """
        print(f"Días del mes {self.month}/{self.year} organizados por semanas:")
        for semana in calendar.monthcalendar(self.year, self.month):
            print(semana)

    def establecer_primer_dia_semana(self):
        """
        Establece y muestra el primer día de la semana (por defecto Lunes=0).
        """
        calendar.setfirstweekday(calendar.SUNDAY)
        primer_dia_semana = calendar.firstweekday()
        print("Primer día de la semana establecido a Domingo (6):", primer_dia_semana)
        # Reiniciar al valor por defecto para no afectar otros ejemplos
        calendar.setfirstweekday(calendar.MONDAY)

    def obtener_nombre_dia_y_mes(self):
        """
        Muestra los nombres de los días de la semana y los meses del año.
        """
        print("Nombres de los días de la semana:")
        for dia in calendar.day_name:
            print(dia)

        print("\nNombres de los meses del año:")
        for mes in calendar.month_name:
            print(mes)

    def ejecutar_ejemplos(self):
        """
        Ejecuta todos los métodos de ejemplo para mostrar las funcionalidades del módulo calendar.
        """
        print("=== Calendario de un Mes ===")
        self.mostrar_calendario_mes()

        print("\n=== Calendario Completo del Año ===")
        self.mostrar_calendario_anio()

        print("\n=== Comprobación de Año Bisiesto ===")
        self.comprobar_bisiesto()

        print("\n=== Conteo de Años Bisiestos en un Rango ===")
        self.contar_bisiestos(2000, 2050)

        print("\n=== Primer Día del Mes y Total de Días ===")
        self.primer_dia_mes_y_dias_totales()

        print("\n=== Días del Mes Organizados por Semanas ===")
        self.generar_iterador_dias_mes()

        print("\n=== Configuración del Primer Día de la Semana ===")
        self.establecer_primer_dia_semana()

        print("\n=== Nombres de Días y Meses ===")
        self.obtener_nombre_dia_y_mes()


# Crear instancia de la clase y ejecutar ejemplos
ejemplos_calendar = CalendarExamples()
ejemplos_calendar.ejecutar_ejemplos()

from datetime import datetime, timedelta
from main import Brazil
import unittest

class TestMain(unittest.TestCase):
    def setUp(self):
        self.calendario = Brazil()
        self.date_format = "%d/%m/%Y"

    def test_diferenca_dias_corridos(self):
        data_um = datetime.strptime("01/01/2023", self.date_format)
        data_dois = datetime.strptime("10/01/2023", self.date_format)
        diferenca = data_dois - data_um
        self.assertEqual(diferenca.days, 9)

    def test_dias_uteis_sem_feriados(self):
        data_um = datetime.strptime("01/01/2023", self.date_format)
        data_dois = datetime.strptime("10/01/2023", self.date_format)
        diferenca = data_dois - data_um
        dia_util = 0
        for i in range(diferenca.days + 1):
            if (data_um + timedelta(days=i)).weekday() < 5:
                dia_util += 1
        self.assertEqual(dia_util, 7)

    def test_dias_uteis_com_feriados(self):
        data_um = datetime.strptime("01/01/2023", self.date_format)
        data_dois = datetime.strptime("10/01/2023", self.date_format)
        diferenca = data_dois - data_um
        feriados = self.calendario.holidays(data_um.year)
        novo_feriado = datetime.strptime("06/01/2023", self.date_format).date()
        feriados.append((novo_feriado, "Feriado Adicionado"))
        dia_util = 0
        for i in range(diferenca.days + 1):
            current_date = (data_um + timedelta(days=i)).date()
            if current_date.weekday() < 5 and current_date not in [holiday[0] for holiday in feriados]:
                dia_util += 1
        self.assertEqual(dia_util, 6)

if __name__ == "__main__":
    unittest.main()
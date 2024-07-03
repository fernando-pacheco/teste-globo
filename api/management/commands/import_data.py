import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import ProgramAudience, InventoryAvailability

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **kwargs):
        # Caminho do CSV de audiência
        audience_csv_path = 'api/utils/tvaberta_program_audience.csv'
        # Caminho do CSV de disponibilidade
        availability_csv_path = 'api/utils/tvaberta_inventory_availability.csv'

        def remove_bom(line):
            if line and line[0] == '\ufeff':
                return line[1:]
            return line

        # Importar dados de audiência
        with open(audience_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader((remove_bom(line) for line in csvfile), delimiter=',')
            next(reader)  # Pula o cabeçalho
            for row in reader:
                print(row)  # Debugging: Printa a linha atual do CSV
                program_audience = ProgramAudience(
                    signal=row[0],
                    program_code=row[1],
                    exhibition_date=datetime.strptime(row[2], '%Y-%m-%d').date(),
                    program_start_time=datetime.strptime(row[3], '%Y-%m-%dT%H:%M:%S.%fZ').time(),  # Converte para objeto time
                    average_audience=float(row[4])
                )
                program_audience.save()

        # Importar dados de disponibilidade
        with open(availability_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader((remove_bom(line) for line in csvfile), delimiter=';')
            next(reader)  # Pula o cabeçalho
            for row in reader:
                print(row)  # Debugging: Printa a linha atual do CSV
                inventory_availability = InventoryAvailability(
                    signal=row[0],
                    program_code=row[1],
                    date=datetime.strptime(row[2], '%d/%m/%Y').date(),
                    available_time=int(row[3])
                )
                inventory_availability.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV'))

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ProgramAudience, InventoryAvailability
from django.utils.dateparse import parse_date

class ProgramDataViewSet(viewsets.ViewSet):
    
    def list(self, request):
        return Response({'message': 'This is the list view. Please use specific endpoints.'})
    
    def retrieve(self, request, pk=None):
        return Response({'message': 'This is the retrieve view. Please use specific endpoints.'})
    
    @action(detail=False, methods=['get'], url_path='program/(?P<program_code>[^/.]+)/(?P<exhibition_date>[^/.]+)')
    def get_program_data(self, request, program_code=None, exhibition_date=None):
        date = parse_date(exhibition_date)
        availability = InventoryAvailability.objects.filter(program_code=program_code, date=date).first()
        if availability:
            audience = ProgramAudience.objects.filter(
                signal=availability.signal, 
                program_code=program_code, 
                exhibition_date=date
            ).first()
            predicted_audience = audience.predicted_audience if audience else None
            return Response({
                'available_time': availability.available_time,
                'predicted_audience': predicted_audience
            })
        return Response({'error': 'Data not found'}, status=404)

    @action(detail=False, methods=['get'], url_path='period/(?P<start_date>[^/.]+)/(?P<end_date>[^/.]+)')
    def get_period_data(self, request, start_date=None, end_date=None):
        start = parse_date(start_date)
        end = parse_date(end_date)
        availability = InventoryAvailability.objects.filter(date__range=[start, end])
        response_data = []
        for av in availability:
            audience = ProgramAudience.objects.filter(
                signal=av.signal, 
                program_code=av.program_code, 
                exhibition_date=av.date
            ).first()
            predicted_audience = audience.predicted_audience if audience else None
            response_data.append({
                'program_code': av.program_code,
                'date': av.date,
                'available_time': av.available_time,
                'predicted_audience': predicted_audience
            })
        return Response(response_data)

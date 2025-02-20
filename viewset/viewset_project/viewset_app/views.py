from django.shortcuts import render
from rest_framework import viewsets
from viewset_app.models import Patient
from viewset_app.serializers import PatientSerializer
from rest_framework.response import Response

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer 

    def list(self):
        patients = Patient.objects.all() 
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):  
        if pk is not None:
            patient = Patient.objects.get(id=pk)  
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        
    def create(self, request,):
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data Created'}, status=201)
            return Response(serializer.errors, status=400)   

    def update(self, request, pk=None):
        patient = Patient.objects.get(id=pk)
        serializer = PatientSerializer(instance=patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=400)    

    def destroy(self, pk=None):
        patient = Patient.objects.get(id=pk)
        patient.delete()
        return Response({'msg': 'Data deleted'})
            
    

    
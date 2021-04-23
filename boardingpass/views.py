from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import tiket, pengguna
from . import transformer, mqtt

import json

def response(values,message):
	return json.dumps({
		'values' : values,
		'message': message
		})

def index(request):
	daftar = []
	penumpang = tiket.objects.all().order_by('-updated_at')
	penumpang = transformer.transform(penumpang)
	
	return JsonResponse(json.loads(response(penumpang,'resp_daftar')))

def pantau(request, kode):
	if request.method == 'GET':
		try:
			boardingpass = tiket.objects.get(kode_booking=int(kode))
			boardingpass = transformer.singleTransform(boardingpass)
		except:
			return JsonResponse(json.loads(response('','Tiket tidak valid!')))

		return JsonResponse(json.loads(response(boardingpass,'valid')))

	if request.method == 'PUT':
		json_data = json.loads(request.body)
		try:
			boardingpass = tiket.objects.get(kode_booking=int(kode))
		except:
			return JsonResponse(json.loads(response('','')))

		boardingpass.status = json_data['status']
		boardingpass.save()
		boardingpass = transformer.singleTransform(boardingpass)

		daftar = tiket.objects.all().order_by('-updated_at')
		daftar = transformer.transform(daftar)
		payload = response(daftar,'resp_daftar')
		ret = mqtt.mqttc.publish('TugasAkhirAldiLugina',payload)

		return JsonResponse(json.loads(response(boardingpass,'berhasil')))
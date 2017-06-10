from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from . import models
from django.db import connection
from django.db.models.query import RawQuerySet
import time


#Controller functions
def index (request):
	content = {
	'name': 'index',
	'username': request.user.username
	}
	return render(request, 'reservations/home.html', content)

def dashboard(request):
	if not 'iniciativa_admin' in request.user.groups.values_list('name', flat=True):
		return redirect('/index/')
	else:

		if request.user.username == 'casd_admin':
			tableName = 'reservations_salacasd'
		elif request.user.username == 'casdvest_admin':
			tableName = 'reservations_salacasdvest'
		elif request.user.username == 'casdinho_admin':
			tableName = 'reservations_salacasdinho'
		elif request.user.username == 'depcult_admin':
			tableName = 'reservations_saladepcult'


		if request.method == "POST":
			deleteReserva(tableName, request.POST['id'])

		listaReservas = getReservas(tableName)

		content = {
		'name': 'dashboard',
		'username': request.user.username,
		'reservas': listaReservas
		}
		return render(request, 'reservations/dashboard.html', content)

def salaCasd(request):
	if request.method == "POST":
		makeReserva('reservations_salacasd', request.POST.get('comecoReserva'), request.POST.get('terminoReserva'), request.POST.get('donoReserva'))

	listaReservas = getReservas('reservations_salacasd')
	content = {
		'name': 'salaCasd',
		'username': request.user.username,
		'reservas': listaReservas
	}
	return render(request, 'reservations/makeReservation.html', content)


def salaCasdVest(request):
	if request.method == "POST":
		makeReserva('reservations_salacasdvest', request.POST.get('comecoReserva'), request.POST.get('terminoReserva'), request.POST.get('donoReserva'))

	listaReservas = getReservas('reservations_salacasdvest')
	content = {
		'name': 'salaCasdVest',
		'username': request.user.username,
		'reservas': listaReservas
	}
	return render(request, 'reservations/makeReservation.html', content)


def salaCasdinho(request):
	if request.method == "POST":
		makeReserva('reservations_salacasdinho', request.POST.get('comecoReserva'), request.POST.get('terminoReserva'), request.POST.get('donoReserva'))

	listaReservas = getReservas('reservations_salacasdinho')
	content = {
		'name': 'salaCasdinho',
		'username': request.user.username,
		'reservas': listaReservas
	}
	return render(request, 'reservations/makeReservation.html', content)


def salaDepCult(request):
	if request.method == "POST":
		makeReserva('reservations_depcult', request.POST.get('comecoReserva'), request.POST.get('terminoReserva'), request.POST.get('donoReserva'))

	listaReservas = getReservas('reservations_saladepcult')
	content = {
		'name': 'salaDepCult',
		'username': request.user.username,
		'reservas': listaReservas
	}
	return render(request, 'reservations/makeReservation.html', content)


#Auxiliary function
def getReservas(table):
	return models.salaCasd.objects.raw("SELECT id, comecoReserva, terminoReserva, donoReserva FROM "+table+" ORDER BY comecoReserva ASC")

def deleteReserva(table, itemId):
	with connection.cursor() as cursor:
		cursor.execute("DELETE FROM  "+table+" WHERE id = "+itemId)

def makeReserva(table, comecoReserva, terminoReserva, donoReserva):
	with connection.cursor() as cursor:
		cursor.execute("INSERT INTO "+table+" (comecoReserva, terminoReserva, donoReserva) VALUES ('"+comecoReserva+"', '"+terminoReserva+"', '"+donoReserva+"')")

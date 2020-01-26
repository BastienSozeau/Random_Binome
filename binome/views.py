from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse
from binome.models import Post
from django import forms


def binome_index(request):
	posts = Post.objects.order_by('-id')
	context = {
		"posts": posts,
	}
	return render(request, "index.html", context)

def submit(request):
	result = {}
	if request.method == 'POST':


		form = YourForm = (request.POST)
		liste = {'Imane' : form['select_Imane'],'Mohamed D' : form['select_Mohamed D'],'Yassine' : form['select_Yassine'],'Luis Felipe' : form['select_Luis Felipe'],'Cécile' : form['select_Cécile'],'Marc-Henri' : form['select_Marc-Henri'],'Gaëtan' : form['select_Gaëtan'],'Alexandre' : form['select_Alexandre'],'Tony' : form['select_Tony'],'Emmanuelle' : form['select_Emmanuelle'],'Nour' : form['select_Nour'],'Bastien' : form['select_Bastien'],'Mohamed S' : form['select_Mohamed S'],'Mathusha' : form['select_Mathusha'],'Laien' : form['select_Laien'],'Josef' : form['select_Josef'],'Nadia' : form['select_Nadia']}

		binomes,resultbin,sep,dispo,restdispo = [],'','—' * 30, [nom for nom in liste if liste[nom] == 'Disponible' ],[]
		for nom in range(len(dispo)): 
			while len(dispo) > 3:
				nom = random.sample(dispo,2)
				dispo.remove(nom[0])
				dispo.remove(nom[1])
				binomes.append(' & '.join(['<span class="rd"><i class="icon-user"></i>'+nom[0]+'</span>','<span class="rd"><i class="icon-user"></i>'+nom[1]+'</span>']))
		for nom in dispo: 
			restdispo.append('<span class="rd"><i class="icon-user"></i>'+nom+'</span>')
		binomes.append(' & '.join(restdispo))
		for i, binome in enumerate(binomes):
			resultbin += '<h4>' + str(i+1) + ' ' + binome + '</h4>'

		result = { 'binomes' : resultbin }
	return render(request, "submit.html",result )
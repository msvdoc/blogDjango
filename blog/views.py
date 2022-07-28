from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import MedicineFindForm

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
user = ua.ie
headerMy = {'User-Agent':str(user)}

FAKE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
AMURFARMA = 'https://amurfarma.ru/search'
medicine_name = 'Аспирин'

# Запускаю отладчик
# import pdb
# pdb.set_trace()


#Класс тупо выводит записи из базы данных. В данном случае из таблицы Post. В шаблоне можно выводятся
# все записи следующим образом:
# {% for post in object_list %}
# 	<p> {{ post.body }} </p>
# {% endfor %}
#Где object_list список всех записей.
class BlogListView(ListView):
	model = Post
	template_name = 'home.html'

#Класс для отображения содержимого записи по первичному ключу. К записи можно обращаться с помощью
# переменной, имеющей тоже имя, что и модель, только с маленькой буквы. Например: {{ post.title }}.
class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


# Класс для создания новой записи.
class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'body']

# Класс изменения записи.
class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	#Если написать - __all__, то все поля будут подлежать редактированию.
	fields = ['title', 'body']

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	#Пользователь не будет перенаправлен до тех пор пока не будет удалена запись.
	success_url = reverse_lazy('home')

class ResFind():
	def __init__(self, name, price):
		self.name = name
		self.price = price


def medicine(request):
	global medicine_name
	if request.method == 'POST':
		medicine_find_form = MedicineFindForm(request.POST)
		if medicine_find_form.is_valid():
			medicine_name = str(medicine_find_form.cleaned_data['medicine_name'])
			return HttpResponseRedirect(reverse('result_find') )
	else:
		medicine_find_form = MedicineFindForm(initial={'medicine_name': 'Дротаверин'})

	return render(request, 'medicine.html', {'form': medicine_find_form})


def result_find(request):
	global medicine_name
	global AMURFARMA
	global FAKE_USER_AGENT
	global  requests
	# address1 = AMURFARMA
	address1 = 'https://apteka.ru/search/?q=дротаверин'
	find1 = {'q': medicine_name}
	# response = requests.get(address1, headers=headerMy, params=find1)
	response = requests.get(address1, headers=headerMy)
	# response = requests.get(address1, headers = FAKE_USER_AGENT)
	soup = BeautifulSoup(response.text, 'lxml')
	result1 = soup.find_all('span', class_='catalog-card__name emphasis')

	result2 = soup.find_all('div', class_='offer__price-current')
	# name1 = soup.find_all('h5', class_='h5 catalog-item__name')
	# price1 = soup.find_all('span', class_='price')
	# res_find = []
	# for n, p in name1, price1:
	# 	res_find.append(ResFind(n, p)) 

	res_find  = [ResFind(result1, '100'), ResFind('Дротаверин', '200')]
	return render(request, 'result_find.html', {'res_find': res_find})
	# return render(request, 'result_find.html', {'res_find': res_find})
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from .views import medicine, result_find

urlpatterns=[
	#Удаление записи
	path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
	#Редактирование записи
	path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
	#Добавление записи.
	path('post/new/', BlogCreateView.as_view(), name="post_new"),
	#Отображение конкретной записи из блога на отдельной странице. Вызов по первичному ключу.
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
	# Агрегатор лекарств
	path('medicine/', medicine, name='medicine'),
	path('result_find/', result_find, name='result_find'),
	# Домашняя страница
	path('', BlogListView.as_view(), name='home'),
]
from django.urls import path
from .views import list_todos

from .views import add_todo, update_todo, delete_todo
from .views import hello_world  # adjust path if needed

urlpatterns = [
    path('hello/', hello_world),
    path('todos/', list_todos),
    path('todos/add', add_todo),
    path('todos/<int:pk>/update', update_todo),
    path('todos/<int:pk>/delete', delete_todo),
]


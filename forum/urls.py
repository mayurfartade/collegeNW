
from django.urls import path   #imported from urls.py original
from . import views  #added import views from current directory

urlpatterns = [
    path('', views.index, name='forum-home'),  #empty path means nothing passed through url, views.index means index function in views file
    path('view-diss/<int:forum_id>', views.viewDisscussion, name='forum-discussion'), #<int:forum_id> means passing parameter(forum_id) through url which is integer
]
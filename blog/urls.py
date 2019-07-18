# from django.conf.urls import include, url
# from . import views

# urlpatterns = [
# 	url('admin/', views.post_list),
# 	url('blog/',include('blog.urls'))
# ]

from django.conf.urls import url
from . import views
urlpatterns = [
url('', views.post_list),
]
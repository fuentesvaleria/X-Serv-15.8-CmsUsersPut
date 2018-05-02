from django.conf.urls import include, url
from django.contrib import admin

#https://stackoverflow.com/questions/46476918/login-and-logout-of-django-contrib-auth-views
#la parte de urls.py
from django.contrib.auth.views import logout, login

#from cmsUser import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cms_user.views.barra'), 
    #https://books.google.es/books?id=za4iT3GVf6oC&pg=PA289&lpg=PA289&dq=r%27%5Eaccounts/profile/$%27+urls.py&source=bl&ots=Mu9Ui4tcB5&sig=nkLHpvUxBM1RvsJfrYW3Z0T_Wyk&hl=es&sa=X&ved=0ahUKEwirxIfipefaAhVBmBQKHanjCXIQ6AEITjAE#v=onepage&q=r'%5Eaccounts%2Fprofile%2F%24'%20urls.py&f=false
    url(r'^accounts/profile/$', 'cms_user.views.barra'),
	url(r'^pages/(\d+)$', 'cms_user.views.pages'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', login),
    url(r'^logout', logout ),
]

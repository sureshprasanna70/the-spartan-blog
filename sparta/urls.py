from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'sparta.views.index'),
    url(r'^blog/', 'blog.views.index',name="blog home"),
    url(r'^$', 'sparta.views.index', name='home'),
    url(r'^superuser/$', 'blog.views.blogadmin', name='superuser'),

)

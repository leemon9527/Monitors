from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Monitors.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/',views.test),
    url(r'^memory/', views.TomcatMemory),
    url(r'^get', views.getTomcatMemory),

)



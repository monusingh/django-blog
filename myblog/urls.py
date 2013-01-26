from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
      (r'^$','blog.views.index'),
      (r'^about','blog.views.about'),
      (r'^resume','blog.views.resume'),
      (r'^contactus','blog.views.contactus'),
      (r'^home','blog.views.home'),
      (r'^(\d+)/$', 'blog.views.post'),
      (r'^add_comment/(\d+)/$', 'blog.views.add_comment'),
      (r'^contact/', include('contact_form.urls')),
    #  (r'^month/(\d+)/(\d+)/$', 'blog.views.month'),
    # (r'^my/', include('my.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      (r'^admin/', include(admin.site.urls)),
)

from django.urls import path, include
from . import views

urlpatterns=[path('apply_submit/', views.apply_submit, name ='Apply_submit'),
path('apply/', views.apply, name ='Apply'),
path('captcha/', include('captcha.urls')),
path('careers/', views.jobs, name ='jobs'),
path('careers/<int:id>', views.jobs_details, name ='jobs_des'),
path('', views.home,name="home"),
path('about/', views.about_us,name='about_us'),
path('contact/',views.contact_us,name="contact_us"),
path('privacypolicy/',views.privacy,name="privacy"),
path('jobs-filter/',views.jobs_filter,name="jobs_filter"),
]
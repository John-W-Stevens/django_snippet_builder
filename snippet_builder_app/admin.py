from django.contrib import admin
from django.urls import path, include

# Register your models here.
from snippet_builder_app.models import ErrorMessage

class ErrorMessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ErrorMessage, ErrorMessageAdmin)

# ****************
urlpatterns = [
# Your app's urls is lined to the project
    path('admin/',admin.site.urls),
    path('snippet_builder_app/', include('snippet_builder_app.urls')),
]
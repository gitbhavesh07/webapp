from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path("", views.trans, name="trans"),
	path("login", views.login, name="login"),
	path("register", views.register, name="register"),
	path("logout", views.logout, name="logout"),
	path("average", views.average, name="average"),
	path("profile", views.profile, name="profile"),
	path("index", views.index, name="index"),
	path("ticket_class_view", views.ticket_class_view, name="ticket_class_view"),
	path("display", views.display, name="display"),
	path("editdisplay", views.editdisplay, name="editdisplay"),
	path("updatedisplay", views.updatedisplay, name="updatedisplay"),
	path("upload", views.upload, name="upload"),
	path("list", views.list, name="list"),
	path("uploading", views.uploading, name="uploading"),
	path("delete_book/<int:pk>/", views.delete_book, name="delete_book")


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
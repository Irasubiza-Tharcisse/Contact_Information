from django.shortcuts import render
from .models import Photo


# Create your views here.
def all_photos_view(request):
  user_active = request.user.is_authenticated
  images = Photo.objects.filter(user=user_active)
  context = {'images': images}
  return render(request, 'photos/all_photos.html', context)

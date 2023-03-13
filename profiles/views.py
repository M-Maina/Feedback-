from django.shortcuts import render
from django.views import View
#from profiles.forms import ProfileForm
from .models import UserProfile
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunks in file.chunks():
#             dest.write(chunks)




class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.htm"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
    
# class CreateProfileView(View):
    
#     def get(self, request, *args, **kwargs):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.htm", {"form": form})
    
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         #request.POST is only for Non-file data
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
       
#         return render(request, "profiles/create_profile.htm", {"form": submitted_form})
    
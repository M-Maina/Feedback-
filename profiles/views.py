from django.shortcuts import render
from django.views import View

# Create your views here.
class CreateProfileView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, "profiles/create_profile.htm")
    
    def post(self, reuest):
        pass
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView #only return template with get_context_data
from django.views.generic import ListView, DetailView
from .models import Review
# Create your views here.



#  if form.is_valid():
#             review = Review(user_name=form.cleaned_data['user_name'],
#                             review_text=form.cleaned_data['review_text'],
#                             rating=form.cleaned_data['rating'])
 #review.save()


class ReviewView(View):
    def get(self, request, *args, **kwargs):
        form = ReviewForm()
        return render(request, 'reviews/review.htm', {'form':form})
    
    
        
    def post(self, request, *args, **kwargs):
         form = ReviewForm(request.POST)
         if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
         return render(request, 'reviews/review.htm', {'form':form})
    

# def review(request):
#     if request.method == 'POST':   #here we check the method request is working with either GET/POST/PUT/DELETE
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
           
#         #entered_username = request.POST['username'] saves data from the request method to a variable
#         #this username we passed it in the form as name
#         # if entered_username =="" and len(entered_username) >= 100:
#         #     return render(request, 'rev iews/review.htm', {'has_error': True})
#           #  print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review.htm', {'form':form})



# def thank_you(request):
#     return render(request,'reviews/thank_you.htm')


class ThankYouView(TemplateView):
   template_name = 'reviews/thank_you.htm'
   
   
   def get_context_data(self, **kwargs):   #This code get all the set context date that we can return in TempateView
       context = super().get_context_data(**kwargs)
       context["message"] = "This Works"
       return context
   
    
    
    
class ReviewListView(ListView):
    template_name = "reviews/review_list.htm"
    model = Review
    context_object_name = "reviews" #we setting this instead of object_list that django provides
    
    # def get_queryset(self): 
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3) very good to retrieve the needed ratings
    #     return data
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context
    
    
class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.htm'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"] #this is the id we passed in the urls
        selected_review = get_object_or_404(Review, pk=review_id)
        context["review"] = selected_review
        return context
    
    
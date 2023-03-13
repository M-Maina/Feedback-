from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == 'POST':   #here we check the method request is working with either GET/POST/PUT/DELETE
        form = ReviewForm(request.POST)
        if form.is_valid():
        #entered_username = request.POST['username'] saves data from the request method to a variable
        #this username we passed it in the form as name
        # if entered_username =="" and len(entered_username) >= 100:
        #     return render(request, 'rev iews/review.htm', {'has_error': True})
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.htm', {'form':form})



def thank_you(request):
    return render(request,'reviews/thank_you.htm')
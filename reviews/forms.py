from django import forms



class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=30, label="Your Name") 
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=100)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
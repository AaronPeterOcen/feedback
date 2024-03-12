from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    """view function to handle the form"""
    # pass
    if request.method  == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request,"reviews/thank_you.html" )
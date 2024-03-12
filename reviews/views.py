from django.shortcuts import render

# Create your views here.
def review(request):
    # pass
    return render(request, "reviews/review.html")
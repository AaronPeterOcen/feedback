# from typing import Any
from typing import Any
from django.db.models.query import QuerySet
from reviews.models import Review
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView, CreateView


from .forms import ReviewForm

# Create your views here.


class ReviewView(CreateView):
    # form_class = ReviewForm
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save()        
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {"form": form})

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Working!!"
        return context


class ReviesListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # to narrow down the query
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=4)
    #     return data


class SingleRevView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     # reviews = Review.objects.all()
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context


# def thank_you(request):
# def get(self, request):
#     return render(request, "reviews/thank_you.html")

from typing import Any

from django.db.models import F
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


# Create your views here.

def index(request):
    latest_question_list = get_list_or_404(Question)
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'
    template_name='polls/index.html'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name='polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name='polls/results.html'


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
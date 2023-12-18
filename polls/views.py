from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
       
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# @login_required
def deleteView(request, item_id):
    questions = Question.objects.raw(f"SELECT * FROM polls_question WHERE id={item_id};")
    for q in questions:
        q.delete()
    return redirect("/polls")
    # if request.user == q.owner:
        # q = Question.objects.get(pk=request.POST.get('id'))
        # q.delete()
        # return redirect('/')
    # else:
        # return HttpResponse("You are not the owner of this question.")
	
	    

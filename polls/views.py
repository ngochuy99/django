from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from polls.form import SignInForm
from .models import Customer, Address, Fullname


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            no = form.cleaned_data.get('number')
            street = form.cleaned_data.get('street')
            district = form.cleaned_data.get('district')
            city = form.cleaned_data.get('city')
            gender = form.cleaned_data.get('gender')
            dob = form.cleaned_data.get('dob')
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(password)
            #Save Fullname
            fn = Fullname(firstname=first_name,middlename=middle_name,lastname=last_name)
            fn.save()
            #Save Address
            addr = Address(no=no,street=street,district=district,city=city)
            addr.save()
            #Save Customer
            customer = Customer(gender=gender,dob=dob,phone=phone,fullname=fn,address=addr,username=username,password=password)
            customer.save()
    else:
        form = SignInForm()
    return render(request, 'polls/signin.html', {'form': form})



    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
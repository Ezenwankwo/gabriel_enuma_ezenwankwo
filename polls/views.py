from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import View, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Profile, Poll, Choice
from .forms import ProfileForm




# Create your views here.

class ProfileCreateView(SuccessMessageMixin, CreateView):

    form_class = ProfileForm
    template_name = 'polls/create_profile.html'
    success_message = 'Your profile is successfully saved'
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)


class IndexView(ListView):

    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'


class DetailView(LoginRequiredMixin, DetailView):

    model = Poll
    template_name = 'polls/detail.html'


def result_all(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/result_all.html', {'choices': choices, 'poll': p})

def result_male(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/male.html', {'choices': choices, 'poll': p}) 

def result_female(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/female.html', {'choices': choices, 'poll': p})

def result_age_18_24(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/age_18_24.html', {'choices': choices, 'poll': p})

def result_age_25_34(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/age_25_34.html', {'choices': choices, 'poll': p})


def result_age_35_44(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/age_35_44.html', {'choices': choices, 'poll': p})

def result_age_45_54(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/age_45_54.html', {'choices': choices, 'poll': p})

def result_age_55_64(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/age_55_64.html', {'choices': choices, 'poll': p})

def result_age_65_(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/age_65_.html', {'choices': choices, 'poll': p})

def result_hausa_fulani(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/hausa_fulani.html', {'choices': choices, 'poll': p})

def result_igbo(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/igbo.html', {'choices': choices, 'poll': p})

def result_yoruba(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/yoruba.html', {'choices': choices, 'poll': p})

def result_minority_south_south(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/minority_south_south.html', {'choices': choices, 'poll': p})

def result_minority_north_central(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/minority_north_central.html', {'choices': choices, 'poll': p})

def result_minority_north_east(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/minority_north_east.html', {'choices': choices, 'poll': p})

def result_north_west(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/north_west.html', {'choices': choices, 'poll': p})

def result_north_east(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/north_east.html', {'choices': choices, 'poll': p})

def result_north_central(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/north_central.html', {'choices': choices, 'poll': p})

def result_south_west(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/south_west.html', {'choices': choices, 'poll': p})

def result_south_east(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/south_east.html', {'choices': choices, 'poll': p})

def result_south_south(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/south_south.html', {'choices': choices, 'poll': p})

def result_diaspora(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/diaspora.html', {'choices': choices, 'poll': p})

def result_less_secondary(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/less_secondary.html', {'choices': choices, 'poll': p})

def result_secondary(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/secondary.html', {'choices': choices, 'poll': p})

def result_graduate(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/graduate.html', {'choices': choices, 'poll': p})

def result_postgraduate(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/postgraduate.html', {'choices': choices, 'poll': p})

def result_currently_unemployed(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/currently_unemployed.html', {'choices': choices, 'poll': p})

def result_employed_full_time(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/employed_full_time.html', {'choices': choices, 'poll': p})

def result_employed_part_time(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/employed_part_time.html', {'choices': choices, 'poll': p})

def result_self_employed(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/self_employed.html', {'choices': choices, 'poll': p})

def result_student(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/student.html', {'choices': choices, 'poll': p})

def result_retired(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/retired.html', {'choices': choices, 'poll': p})

def result_less_18000(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/less_18000.html', {'choices': choices, 'poll': p})

def result_18000_50000(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/_18000_50000.html', {'choices': choices, 'poll': p})

def result_51000_100000(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/_51000_100000.html', {'choices': choices, 'poll': p})

def result_101000_200000(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/_101000_200000.html', {'choices': choices, 'poll': p})

def result_201000_500000(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/_201000_500000.html', {'choices': choices, 'poll': p})

def result_500000(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/_500000.html', {'choices': choices, 'poll': p})

def result_single_never_married(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/single_never_married.html', {'choices': choices, 'poll': p})

def result_divorced_separated(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/divorced_separated.html', {'choices': choices, 'poll': p})

def result_married(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/married.html', {'choices': choices, 'poll': p})

def result_widowed(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/widowed.html', {'choices': choices, 'poll': p})

def result_christianity(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/christianity.html', {'choices': choices, 'poll': p})

def result_islam(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/islam.html', {'choices': choices, 'poll': p})

def result_other_religion(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    choices = p.choice_set.all()
    return render(request, 'polls/other_religion.html', {'choices': choices, 'poll': p})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)

    try:
        profile = request.user.profile
                
    except (KeyError, Profile.DoesNotExist):
            return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You must have a profile to vote.",
        })   
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    if request.user.profile.poll_set.filter(pk=poll_id).exists():
         return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You have voted on this poll already.",
        })   
    else:
        p.profile.add(request.user.profile)
        p.save()
        selected_choice.profile.add(request.user.profile)
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:result_all', args=(p.id,)))

def respondents(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)

    male_num = p.profile.filter(sex__iexact='Male').count()
    female_num = p.profile.filter(sex__iexact='Female').count()
    _18_24_num = p.profile.filter(age__iexact='18-24').count()
    _25_34_num = p.profile.filter(age__iexact='25-34').count()
    _35_44_num = p.profile.filter(age__iexact='35-44').count()
    _45_54_num = p.profile.filter(age__iexact='45-54').count()
    _55_64_num = p.profile.filter(age__iexact='55-64').count()
    _65_num = p.profile.filter(age__iexact='65+').count()
    hausa_fulani_num = p.profile.filter(ethnicity__iexact='Hausa/Fulani').count()
    igbo_num = p.profile.filter(ethnicity__iexact='Igbo').count()
    yoruba_num = p.profile.filter(ethnicity__iexact='Yoruba').count()
    minority_SS_num = p.profile.filter(ethnicity__iexact='Minority-South South').count()
    minority_NC_num = p.profile.filter(ethnicity__iexact='Minority-North Central').count()
    minority_NE_num = p.profile.filter(ethnicity__iexact='Minority-North East').count()
    north_west_num = p.profile.filter(residence__iexact='North West').count()
    north_east_num = p.profile.filter(residence__iexact='North East').count()
    north_central_num = p.profile.filter(residence__iexact='North Central').count()
    south_west_num = p.profile.filter(residence__iexact='South West').count()
    south_east_num = p.profile.filter(residence__iexact='South East').count()
    south_south_num = p.profile.filter(residence__iexact='South South').count()
    diaspora_num = p.profile.filter(residence__iexact='Diaspora').count()
    less_secondary_num = p.profile.filter(education__iexact='Less than secondary school').count()
    secondary_num = p.profile.filter(education__iexact='Secondary school').count()
    graduate_num = p.profile.filter(education__iexact='Graduate').count()
    postgraduate_num = p.profile.filter(education__iexact='Post graduate').count()
    currently_unemployed_num = p.profile.filter(employment__iexact='Currently unemployed').count()
    employed_full_time_num = p.profile.filter(employment__iexact='Employed full time').count()
    employed_part_time_num = p.profile.filter(employment__iexact='Employed part time').count()
    self_employed_num = p.profile.filter(employment__iexact='Self employed').count()
    student_num = p.profile.filter(employment__iexact='Student').count()
    retired_num = p.profile.filter(employment__iexact='Retired').count()
    less_18000_num = p.profile.filter(income__iexact='Less than 18,000').count()
    _18000_50000_num = p.profile.filter(income__iexact='18,000 - 50,000').count()
    _51000_100000_num = p.profile.filter(income__iexact='51,000 - 100,000').count()
    _101000_200000_num = p.profile.filter(income__iexact='101,000 - 200,000').count()
    _201000_500000_num = p.profile.filter(income__iexact='201,000 - 500,000').count()
    _500000_num = p.profile.filter(income__iexact='500,000+').count()
    single_never_married_num = p.profile.filter(marital_status__iexact='Single-never married').count()
    divorced_separated_num = p.profile.filter(marital_status__iexact='Divorced or Separated').count()
    married_num = p.profile.filter(marital_status__iexact='married').count()
    widowed_num = p.profile.filter(marital_status__iexact='Widowed').count()
    christianity_num = p.profile.filter(religion__iexact='Christianity').count()
    islam_num = p.profile.filter(religion__iexact='Islam').count()
    other_religion_num = p.profile.filter(religion__iexact='Other').count()

    context = {'male_num':male_num, 'female_num':female_num, '18_24_num':_18_24_num, '25_34_num':_25_34_num, '35_44_num':_35_44_num, '45_54_num':_45_54_num, '55_64_num':_55_64_num, '65_num':_65_num, 
    'hausa_fulani_num':hausa_fulani_num, 'igbo_num':igbo_num, 'yoruba_num':yoruba_num, 'minority_SS_num':minority_SS_num, 'minority_NC_num':minority_NC_num, 'minority_NE_num':minority_NE_num, 'north_west_num':north_west_num,
    'north_east_num':north_east_num, 'north_central_num':north_central_num, 'south_west_num':south_west_num, 'south_east_num':south_east_num, 'south_south_num':south_south_num, 'diaspora_num':diaspora_num, 'less_secondary_num':less_secondary_num,
    'secondary_num':secondary_num, 'graduate_num':graduate_num, 'postgraduate_num':postgraduate_num, 'currently_unemployed_num':currently_unemployed_num, 'employed_full_time_num':employed_full_time_num, 'employed_part_time_num':employed_part_time_num,
    'self_employed_num':self_employed_num, 'student_num':student_num, 'retired_num':retired_num, 'less_18000_num':less_18000_num, '18000_50000_num':_18000_50000_num, '51000_100000_num':_51000_100000_num, '101000_200000_num':_101000_200000_num,
    '201000_500000_num':_201000_500000_num, '500000_num':_500000_num, 'single_never_married_num':single_never_married_num, 'divorced_separated_num':divorced_separated_num, 'married_num':married_num, 'widowed_num':widowed_num,
    'christianity_num':christianity_num, 'islam_num':islam_num, 'other_religion_num':other_religion_num }

    return render (request, 'polls/respondent.html', context)





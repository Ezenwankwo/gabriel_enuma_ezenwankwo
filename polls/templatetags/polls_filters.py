from django import template
from django.shortcuts import get_object_or_404
from polls.models import Profile, Choice

register = template.Library()

#filter for all votes
@register.filter(name='result_percentage')
def result_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.count()
	choice_vote = Profile.objects.filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for male votes
@register.filter(name='male_votes')
def male_votes(value, arg):
	profile_num = Profile.objects.filter(sex__iexact='Male').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='male_percentage')
def male_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(sex__iexact='Male').count()
	choice_vote = Profile.objects.filter(sex__iexact='Male').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for female votes
@register.filter(name='female_votes')
def female_votes(value, arg):
	profile_num = Profile.objects.filter(sex__iexact='Female').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='female_percentage')
def female_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(sex__iexact='Female').count()
	choice_vote = Profile.objects.filter(sex__iexact='Female').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 18-24 votes
@register.filter(name='_18_24_votes')
def _18_24_votes(value, arg):
	profile_num = Profile.objects.filter(age__iexact='18-24').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_18_24_percentage')
def _18_24_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(age__iexact='18-24').count()
	choice_vote = Profile.objects.filter(age__iexact='18-24').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 25-34 votes
@register.filter(name='_25_34_votes')
def _25_34_votes(value, arg):
	profile_num = Profile.objects.filter(age__iexact='25-34').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_25_34_percentage')
def _25_34_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(age__iexact='25-34').count()
	choice_vote = Profile.objects.filter(age__iexact='25-34').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 35-44 votes
@register.filter(name='_35_44_votes')
def _35_44_votes(value, arg):
	profile_num = Profile.objects.filter(age__iexact='35-44').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_35_44_percentage')
def _35_44_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(age__iexact='35-44').count()
	choice_vote = Profile.objects.filter(age__iexact='35-44').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 45-54 votes
@register.filter(name='_45_54_votes')
def _45_54_votes(value, arg):
	profile_num = Profile.objects.filter(age__iexact='45-54').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_45_54_percentage')
def _45_54_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(age__iexact='45-54').count()
	choice_vote = Profile.objects.filter(age__iexact='45-54').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 55-64 votes
@register.filter(name='_55_64_votes')
def _55_64_votes(value, arg):
	profile_num = Profile.objects.filter(age__iexact='55-64').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_55_64_percentage')
def _55_64_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(age__iexact='55-64').count()
	choice_vote = Profile.objects.filter(age__iexact='55-64').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 65+ votes
@register.filter(name='_65_votes')
def _65_votes(value, arg):
	profile_num = Profile.objects.filter(age__iexact='65+').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_65_percentage')
def _65_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(age__iexact='65+').count()
	choice_vote = Profile.objects.filter(age__iexact='65+').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for hausa/fulani votes
@register.filter(name='hausa_fulani_votes')
def hausa_fulani_votes(value, arg):
	profile_num = Profile.objects.filter(ethnicity__iexact='Hausa/Fulani').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='hausa_fulani_percentage')
def hausa_fulani_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(ethnicity__iexact='Hausa/Fulani').count()
	choice_vote = Profile.objects.filter(ethnicity__iexact='Hausa/Fulani').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for igbo votes
@register.filter(name='igbo_votes')
def igbo_votes(value, arg):
	profile_num = Profile.objects.filter(ethnicity__iexact='Igbo').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='igbo_percentage')
def igbo_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(ethnicity__iexact='Igbo').count()
	choice_vote = Profile.objects.filter(ethnicity__iexact='Igbo').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for yoruba votes
@register.filter(name='yoruba_votes')
def yoruba_votes(value, arg):
	profile_num = Profile.objects.filter(ethnicity__iexact='Yoruba').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='yoruba_percentage')
def yoruba_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(ethnicity__iexact='Yoruba').count()
	choice_vote = Profile.objects.filter(ethnicity__iexact='Yoruba').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for minority south south votes
@register.filter(name='minority_south_south_votes')
def minority_south_south_votes(value, arg):
	profile_num = Profile.objects.filter(ethnicity__iexact='Minority-South South').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='minority_south_south_percentage')
def minority_south_south_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(ethnicity__iexact='Minority-South South').count()
	choice_vote = Profile.objects.filter(ethnicity__iexact='Minority-South South').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for minority north central votes
@register.filter(name='minority_north_central_votes')
def minority_north_central_votes(value, arg):
	profile_num = Profile.objects.filter(ethnicity__iexact='Minority-North Central').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='minority_north_central_percentage')
def minority_north_central_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(ethnicity__iexact='Minority-North Central').count()
	choice_vote = Profile.objects.filter(ethnicity__iexact='Minority-North Central').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for minority north east votes
@register.filter(name='minority_north_east_votes')
def minority_north_east_votes(value, arg):
	profile_num = Profile.objects.filter(ethnicity__iexact='Minority-North East').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='minority_north_east_percentage')
def minority_north_east_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(ethnicity__iexact='Minority-North East').count()
	choice_vote = Profile.objects.filter(ethnicity__iexact='Minority-North East').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for north west votes
@register.filter(name='north_west_votes')
def north_west_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='North West').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='north_west_percentage')
def north_west_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='North West').count()
	choice_vote = Profile.objects.filter(residence__iexact='North West').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for north east votes
@register.filter(name='north_east_votes')
def north_east_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='North East').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='north_east_percentage')
def north_east_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='North East').count()
	choice_vote = Profile.objects.filter(residence__iexact='North East').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for north central votes
@register.filter(name='north_central_votes')
def north_central_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='North Central').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='north_central_percentage')
def north_central_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='North Central').count()
	choice_vote = Profile.objects.filter(residence__iexact='North Central').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for south west votes
@register.filter(name='south_west_votes')
def south_west_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='South West').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='south_west_percentage')
def south_west_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='South West').count()
	choice_vote = Profile.objects.filter(residence__iexact='South West').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for south east votes
@register.filter(name='south_east_votes')
def south_east_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='South East').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='south_east_percentage')
def south_east_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='South East').count()
	choice_vote = Profile.objects.filter(residence__iexact='South East').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for south south votes
@register.filter(name='south_south_votes')
def south_south_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='South South').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='south_south_percentage')
def south_south_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='South South').count()
	choice_vote = Profile.objects.filter(residence__iexact='South South').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for diaspora votes
@register.filter(name='diaspora_votes')
def diaspora_votes(value, arg):
	profile_num = Profile.objects.filter(residence__iexact='Diaspora').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='diaspora_percentage')
def diaspora_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(residence__iexact='Diaspora').count()
	choice_vote = Profile.objects.filter(residence__iexact='Diaspora').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for less secondary votes
@register.filter(name='less_secondary_votes')
def less_secondary_votes(value, arg):
	profile_num = Profile.objects.filter(education__iexact='Less than secondary school').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='less_secondary_percentage')
def less_secondary_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(education__iexact='Less than secondary school').count()
	choice_vote = Profile.objects.filter(education__iexact='Less than secondary school').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for secondary votes
@register.filter(name='secondary_votes')
def secondary_votes(value, arg):
	profile_num = Profile.objects.filter(education__iexact='Secondary school').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='secondary_percentage')
def secondary_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(education__iexact='Secondary school').count()
	choice_vote = Profile.objects.filter(education__iexact='Secondary school').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for graduate votes
@register.filter(name='graduate_votes')
def graduate_votes(value, arg):
	profile_num = Profile.objects.filter(education__iexact='Graduate').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='graduate_percentage')
def graduate_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(education__iexact='Graduate').count()
	choice_vote = Profile.objects.filter(education__iexact='Graduate').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for postgraduate votes
@register.filter(name='post_graduate_votes')
def post_graduate_votes(value, arg):
	profile_num = Profile.objects.filter(education__iexact='Post graduate').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='post_graduate_percentage')
def post_graduate_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(education__iexact='Post graduate').count()
	choice_vote = Profile.objects.filter(education__iexact='Post graduate').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for currently unemployed votes
@register.filter(name='currently_unemployed_votes')
def currently_unemployed_votes(value, arg):
	profile_num = Profile.objects.filter(employment__iexact='Currently unemployed').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='currently_unemployed_percentage')
def currently_unemployed_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(employment__iexact='Currently unemployed').count()
	choice_vote = Profile.objects.filter(employment__iexact='Currently unemployed').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for employed full time votes
@register.filter(name='employed_full_time_votes')
def employed_full_time_votes(value, arg):
	profile_num = Profile.objects.filter(employment__iexact='Employed full time').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='employed_full_time_percentage')
def employed_full_time_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(employment__iexact='Employed full time').count()
	choice_vote = Profile.objects.filter(employment__iexact='Employed full time').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for employed part time votes
@register.filter(name='employed_part_time_votes')
def employed_part_time_votes(value, arg):
	profile_num = Profile.objects.filter(employment__iexact='Employed part time').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='employed_part_time_percentage')
def employed_part_time_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(employment__iexact='Employed part time').count()
	choice_vote = Profile.objects.filter(employment__iexact='Employed part time').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for self employed votes
@register.filter(name='self_employed_votes')
def self_employed_votes(value, arg):
	profile_num = Profile.objects.filter(employment__iexact='Self employed').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='self_employed_percentage')
def self_employed_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(employment__iexact='Self employed').count()
	choice_vote = Profile.objects.filter(employment__iexact='Self employed').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for student votes
@register.filter(name='student_votes')
def student_votes(value, arg):
	profile_num = Profile.objects.filter(employment__iexact='Student').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='student_percentage')
def student_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(employment__iexact='Student').count()
	choice_vote = Profile.objects.filter(employment__iexact='Student').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for retired votes
@register.filter(name='retired_votes')
def retired_votes(value, arg):
	profile_num = Profile.objects.filter(employment__iexact='Retired').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='retired_percentage')
def retired_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(employment__iexact='Retired').count()
	choice_vote = Profile.objects.filter(employment__iexact='Retired').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for less 18,000 votes
@register.filter(name='less_than_18000_votes')
def less_than_18000_votes(value, arg):
	profile_num = Profile.objects.filter(income__iexact='Less than 18,000').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='less_than_18000_percentage')
def less_than_18000_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(income__iexact='Less than 18,000').count()
	choice_vote = Profile.objects.filter(income__iexact='Less than 18,000').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 18,000-50,000
@register.filter(name='_18000_50000_votes')
def _18000_50000_votes(value, arg):
	profile_num = Profile.objects.filter(income__iexact='18,000 - 50,000').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_18000_50000_percentage')
def _18000_50000_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(income__iexact='18,000 - 50,000').count()
	choice_vote = Profile.objects.filter(income__iexact='18,000 - 50,000').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 51,000-100,000
@register.filter(name='_51000_100000_votes')
def _51000_100000_votes(value, arg):
	profile_num = Profile.objects.filter(income__iexact='51,000 - 100,000').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_51000_100000_percentage')
def _51000_100000_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(income__iexact='51,000 - 100,000').count()
	choice_vote = Profile.objects.filter(income__iexact='51,000 - 100,000').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 101,000-200000
@register.filter(name='_101000_200000_votes')
def _101000_200000_votes(value, arg):
	profile_num = Profile.objects.filter(income__iexact='101,000 - 200,000').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_101000_200000_percentage')
def _101000_200000_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(income__iexact='101,000 - 200,000').count()
	choice_vote = Profile.objects.filter(income__iexact='101,000 - 200,000').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 201,000-500,000 votes
@register.filter(name='_201000_500000_votes')
def _201000_500000_votes(value, arg):
	profile_num = Profile.objects.filter(income__iexact='201,000 - 500,000').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_201000_500000_percentage')
def _201000_500000_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(income__iexact='201,000 - 500,000').count()
	choice_vote = Profile.objects.filter(income__iexact='201,000 - 500,000').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for 500,000+ votes
@register.filter(name='_500000_votes')
def _500000_votes(value, arg):
	profile_num = Profile.objects.filter(income__iexact='500,000+').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='_500000_percentage')
def _500000_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(income__iexact='500,000+').count()
	choice_vote = Profile.objects.filter(income__iexact='500,000+').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for single votes
@register.filter(name='single_never_married_votes')
def single_never_married_votes(value, arg):
	profile_num = Profile.objects.filter(marital_status__iexact='Single-never married').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='single_never_married_percentage')
def single_never_married_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(marital_status__iexact='Single-never married').count()
	choice_vote = Profile.objects.filter(marital_status__iexact='Single-never married').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for divorced or separated
@register.filter(name='divorced_or_separated_votes')
def divorced_or_separated_votes(value, arg):
	profile_num = Profile.objects.filter(marital_status__iexact='Divorced or Separated').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='divorced_or_separated_percentage')
def divorced_or_separated_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(marital_status__iexact='Divorced or Separated').count()
	choice_vote = Profile.objects.filter(marital_status__iexact='Divorced or Separated').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for married votes
@register.filter(name='married_votes')
def married_votes(value, arg):
	profile_num = Profile.objects.filter(marital_status__iexact='Married').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='married_percentage')
def married_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(marital_status__iexact='Married').count()
	choice_vote = Profile.objects.filter(marital_status__iexact='Married').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for widowed votes
@register.filter(name='widowed_votes')
def widowed_votes(value, arg):
	profile_num = Profile.objects.filter(marital_status__iexact='Widowed').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='widowed_percentage')
def widowed_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(marital_status__iexact='Widowed').count()
	choice_vote = Profile.objects.filter(marital_status__iexact='Widowed').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for christianity votes
@register.filter(name='christianity_votes')
def christianity_votes(value, arg):
	profile_num = Profile.objects.filter(religion__iexact='Christianity').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='christianity_percentage')
def christianity_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(religion__iexact='Christianity').count()
	choice_vote = Profile.objects.filter(religion__iexact='Christianity').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for islam votes
@register.filter(name='islam_votes')
def islam_votes(value, arg):
	profile_num = Profile.objects.filter(religion__iexact='Islam').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='islam_percentage')
def islam_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(religion__iexact='Islam').count()
	choice_vote = Profile.objects.filter(religion__iexact='Islam').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)

#filters for other votes
@register.filter(name='other_votes')
def other_votes(value, arg):
	profile_num = Profile.objects.filter(religion__iexact='Other').filter(choice__id=arg).count()
	return profile_num

@register.filter(name='other_percentage')
def other_percentage(value, arg):
	choice = get_object_or_404(Choice, pk=arg)
	all_votes = choice.poll.profile.filter(religion__iexact='Other').count()
	choice_vote = Profile.objects.filter(religion__iexact='Other').filter(choice__id=arg).count()
	if choice_vote > 0:
		percentage = choice_vote/all_votes * 100
		return round(percentage)


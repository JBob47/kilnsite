from django.shortcuts import render
from .models import Event, Activity
from datetime import date
from .kiln import Kiln

def index(request):
	name = Kiln().name
	context = {'name': name }
	return render(request, 'events/index.html', context)

def event_detail(request, pk):
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	event = Event.objects.get(pk=pk)
	context = {
	'event': event,
	'num_visits': num_visits,
	}
	return render(request, 'events/event_detail.html', context)


from django.views import generic

class EventListView(generic.ListView):
	model = Event
	paginate_by = 10
	# context_object_name = 'my_book_list' #your name for ListView
	# queryset = Book.objects.filter(title__icontains='war')[:5] #Get 5 books containing the title war
	# template_name = 'books/my_arbitrary_template_name_list.html' #Specify your own template name/location
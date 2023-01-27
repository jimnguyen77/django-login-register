from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import EventForm, VenueForm
from django.http import HttpResponse
import csv

def home(request):
	return render(request, 'events/home.html')

def list_events(request):
	event_list = Event.objects.all().order_by('-name','venue')

	return render(request,
		'events/event_list.html', {
			'event_list': event_list
		}
	)

def add_event(request):
	submitted = False
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect('/add_event?submitted=True')
			return redirect('event-list')
	else:
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request,
		'events/add_event.html', {
			'form': form,
			'submitted': submitted
		}
	)

def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('event-list')

	return render(request,
		'events/update_event.html', {
			'event': event,
			'form': form,
		}
	)

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	return redirect('event-list')

def list_venues(request):
	venue_list = Venue.objects.all().order_by('name')

	return render(request,
		'events/venues.html', {
			'venue_list': venue_list
		}
	)

def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)

	return render(request,
		'events/show_venue.html', {
			'venue': venue
		}
	)

def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('venue-list')

	return render(request,
		'events/update_venue.html', {
			'venue': venue,
			'form': form,
		}
	)

def add_venue(request):
	submitted = False
	if request.method == 'POST':
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect('/add_venue?submitted=True')
			return redirect('venue-list')
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request,
		'events/add_venue.html', {
			'form': form,
			'submitted': submitted
		}
	)

def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('venue-list')

def search_venues(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)

		return render(request,
			'events/search_venues.html', {
				'searched': searched,
				'venues': venues
			}
		)
	else:
		return render(request,
			'events/search_venues.html', {
			}
		)

def calendar_view(
		request, 
		year=datetime.now().year, 
		month=datetime.now().strftime('%B') 
	):
	# Convert month from name to number
	month = month.title()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# Create a calendar
	cal = HTMLCalendar().formatmonth(year, month_number)

	# Get current year
	now = datetime.now()
	current_year = now.year

	# Get current time
	current_time = now.strftime('%I:%M %p')

	return render(request, 
		'events/calendar.html', {
			'year': year,
			'month': month,
			'month_number': month_number,
			'cal': cal,
			'current_year': current_year,
			'current_time': current_time,
		}
	)

# Generate Text File Venue List
def venue_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=venues.txt'

	# Designate the model
	venues = Venue.objects.all()

	lines = []
	# Loop through and output
	for venue in venues:
		lines.append(
			f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n'
		)

	# Write to text file
	response.writelines(lines)
	return response

# Generate CSV File Venue List
def venue_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=venues.csv'

	# Create a CSV writer
	writer = csv.writer(response)

	# Designate the model
	venues = Venue.objects.all()

	# Add column headings to the CSV file
	writer.writerow([
		'Venue Name',
		'Address',
		'Zip Code',
		'Phone',
		'Web Address',
		'Email'
	])

	# Loop through and output
	for venue in venues:
		writer.writerow([
			venue.name,
			venue.address,
			venue.zip_code,
			venue.phone,
			venue.web,
			venue.email_address
		])

	return response

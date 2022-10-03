from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from . models import Room, Booking
from . forms import AvailabilityForm
from booking.booking_functions.availability import check_availability
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def RooomListView(request):
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
    room_values = room_categories.values()
    room_list = []
    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url =reverse('booking:RoomDetailView', kwargs={'category':room_category})
        room_list.append((room, room_url))
    context = {
        "room_list":room_list,
    }
    return render(request, 'booking/room_list_view.html', context)





class BookingListView(ListView):
    model = Booking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list




class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'booking/avail_form.html'

    def form_valid(self, form):
        data = form.cleaned_data

        room_list = Room.objects.filter(category = data['room_category'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in_date'], data['check_in_time'], data['check_out_date'], data['check_out_time'], data['beds'], data['number_of_occupant']):
                available_rooms.append(room)
            if len(available_rooms) > 0:
                room = available_rooms[0]
                booking = Booking.objects.create(
                    user = self.request.user,
                    room = room,
                    check_in_date = data['check_in_date'], 
                    check_in_time = data['check_in_time'], 
                    check_out_date = data['check_out_date'], 
                    check_out_time =  data['check_out_time'],
                    beds = data['beds'], 
                    number_of_occupant = data['number_of_occupant'],
                )
                booking.save()
                return HttpResponse(booking)
            else:
                return HttpResponse(f"Sorry Dear {User} All this Category of rooms has been booked!! Please Try Another Catergory")




class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)
        
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'booking/room_detail_view.html', context)
        else:
            return HttpResponse("Category does not exist")

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data


        available_rooms = []
        for room in room_list:
            if check_availability(
                room, data['check_in_date'], data['check_in_time'], data['check_out_date'], data['check_out_time'], data['beds'], data['number_of_occupant']
            ):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in_date = data['check_in_date'], 
                check_in_time = data['check_in_time'], 
                check_out_date = data['check_out_date'], 
                check_out_time =  data['check_out_time'],
                beds = data['beds'], 
                number_of_occupant = data['number_of_occupant'],
                
            )
            if booking.beds > 2:
                return HttpResponse(f"Sorry Dear {User} Number of beds cannot be more than 2")
                
            if  booking.check_in_date > booking.check_out_date:
                return HttpResponse(f"Sorry Dear {User} Check In Date Cannot be greater than Check Out Date")
            booking.save()
            return HttpResponse(booking)
            
        else:
            return HttpResponse(f"Sorry Dear {User} All this Category of rooms has been booked!! Please Try Another Catergory")



class CancelBookingView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking:BookingListView')

# Create your views here.

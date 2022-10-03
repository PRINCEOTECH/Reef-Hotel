from booking.models import Room, Booking
from django.shortcuts import HttpResponse


def check_availability(room, checking_in_date, check_in_time, check_out_date, check_out_time, beds,  number_of_occupant):
    avail_list = []
    booking_list = Booking.objects.filter(room=room, beds=beds, check_in_time=check_in_time, number_of_occupant=number_of_occupant, check_out_time=check_out_time)
    for booking in booking_list:
        if booking.check_in_date > check_out_date or booking.check_out_date < checking_in_date:
            if booking.check_out_date > booking.checking_in_date:
                if booking.beds < 3:
                    avail_list.append(True)
                else:
                    avail_list.append(False)
            else:
                avail_list.append(False)
        else:
            avail_list.append(False)
    return all(avail_list)
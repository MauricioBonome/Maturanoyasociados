from django.shortcuts import render
from .models import Auction

def subastas(request):
    upcoming_auctions = Auction.objects.filter(is_completed=False).order_by('date')
    completed_auctions = Auction.objects.filter(is_completed=True).order_by('-date')
    context = {
        'upcoming_auctions': upcoming_auctions,
        'completed_auctions': completed_auctions,
    }
    return render(request, 'subastas/subastas.html', context)
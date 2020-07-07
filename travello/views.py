from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'Mayanagri, the home of Bollywood'
    # dest1.price = 100
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = 'Surat'
    # dest2.desc = 'Diamond City and Textile Hub'
    # dest2.price = 200
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = 'Delhi'
    # dest3.desc = 'Capital of India'
    # dest3.price = 300
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = True
    #
    # destinations = [dest1,dest2,dest3]

    destinations = Destination.objects.all()

    return render(request,'index.html',{'destinations':destinations})

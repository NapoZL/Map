from django.shortcuts import render
from django.http import HttpResponse
import folium
import folium.plugins

# Create your views here.
def index(request):
    return render(request, 'index.html')

def map(request):
    m = folium.Map()
    minimap = folium.plugins.MiniMap(toggle_display=True)
    m.add_child(minimap)
    #folium.plugins.ScrollZoomToggler().add_to(m)
    folium.plugins.Fullscreen(position='topright').add_to(m)
    m = m._repr_html_()
    
    context = {
        'm': m
    }
    return render(request, 'map.html', context)
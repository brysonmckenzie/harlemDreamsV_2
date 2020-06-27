from django.shortcuts import render, redirect, HttpResponse

from .models import Event, Player, Photo, Notice, SiteConfiguration, Video

from django.core.mail import send_mail

from django.conf import settings


def index(request):
    event_message = 'Join us, check Events for more information'
    home_notice = Notice.objects.all()
    carousel = Photo.objects.all()
    site = SiteConfiguration.objects.get(id=1)
    c_off = site.carousel_off

    # links = SiteLink.objects.all()

    # for link in links:

    #     facebook = link.facebook
    #     instagram = link.instagram
    #     twitter = link.twitter
    #     home_phone = link.homepage_phone

    context = {
        'message': event_message,
        'photos': Photo.objects.all(),
        'notice': home_notice,
        'c_off': c_off,
        'site_config': SiteConfiguration.objects.all(),
        'facebook': site.facebook,
        'instagram': site.instagram,
        'twitter': site.twitter,
        'phone': site.homepage_phone,
       
    }


    return render(request, 'dream_app/index.html', context)


def jobs(request):

    return render(request, 'dream_app/job-openings.html')


def job_process(request):

    server_name = request.POST['client_name']
    server_position = request.POST['client_position']
    server_address = request.POST['client_address']
    server_address2 = request.POST['client_address2']
    server_city = request.POST['client_city']
    server_state = request.POST['client_state']
    server_zip = request.POST['client_zip']
    server_age = request.POST['client_age']
    server_email = request.POST['client email']
    server_q1 = request.POST['client_q1']
    server_q2 = request.POST['client_q2']
    server_q3 = request.POST['client_q3']

    return redirect('/')


def about(request):

    return render(request, 'dream_app/about.html')


def shop(request):

    return render(request, 'dream_app/shop.html')


def events(request):

    no_event_message = "Updates are coming soon. Stay tuned!"

    context = {
        'events': Event.objects.all(),
        'no_event': no_event_message
    }

    return render(request, 'dream_app/events.html', context)


def newsletter(request):

    return render(request, 'dream_app/newsletter.html')


def team(request):

    active_players = Player.objects.all()
    hdp = Player.objects.all()

    for index in hdp:
        print(index.active)
        if index.active == True:
            active_players = True

    print(active_players)

    context = {
        'players': Player.objects.all(),
        'active': active_players,
    }

    # print(hdp)


    return render(request, 'dream_app/team.html', context)


def contact(request):
    c_site = SiteConfiguration.objects.get(id=1)
    contact_phone = c_site.contact_page_phone
    contact_email = c_site.contact_email

    context = {
        'phone': contact_phone,
        'email': contact_email,
    }


    return render(request, 'dream_app/contact.html', context)


def sponsors(request):

    return render(request, 'dream_app/sponsors.html')


def founder(request):

    return render(request, 'dream_app/founders.html')


def media(request):
    videos = Video.objects.all()
    

    context = {
        "videos":videos,
    }


    return render(request, 'dream_app/media.html', context)


def media(request):
    videos = Video.objects.all()
    

    context = {
        "videos":videos,
    }


    return render(request, 'dream_app/media-photo.html', context)


def process_contact(request):

    if request.method == 'POST':

        server_name = request.POST['client_name']
        server_subject = request.POST['client_subject']
        server_email = request.POST['client_email']
        server_message = request.POST['client_message']
        from_email = settings.EMAIL_HOST_USER

        send_mail(server_subject, server_message, server_email, [
                  'contact@harlemdreams.net'], fail_silently=False,)

        print('***** New Contact Info has Arrived *****')
        print(""" Success! Email Worked """)

        return redirect('/')




def camp(request):


    context = {
        
    }

    return render(request, 'dream_app/camp.html', context)
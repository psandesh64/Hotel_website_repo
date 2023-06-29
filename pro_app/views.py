from django.shortcuts import render,redirect
from pro_app.models import *

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    customers = Customer.objects.all()
    videos = Videos.objects.get(name='process-behind')
    key = settings.GOOGLE_API_KEY
    return render(request, 'index.html', {'categories': categories,'customers':customers,'videos': videos,'key':key})

def about_us(request):
    videos = Videos.objects.get(name='process-behind')
    bstaffs = Business_staff.objects.all()
    tstaffs = Team_staff.objects.all()
    print(videos.video)
    return render(request,'about-us.html',{'videos':videos,'bstaffs':bstaffs,'tstaffs':tstaffs})

def get_in_touch(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        choose_option = request.POST['choose_option']
        phone = request.POST['phone']
        message = request.POST['text_area']
        user_contact=GetInTouch(first_name=first_name,last_name=last_name,
                                email=email,choose_option=choose_option,phone=phone,text_area=message)
        user_contact.save()

        subject = f'{choose_option}'
        message = f'Thank you for gettin in touch with us Mr/Mrs. {first_name} {last_name}. Your queries have been registered. Our team will reach you out shortly.'
        email_from = settings.EMAIL_HOST_USER
        print(subject,message,email_from)
        send_mail(subject, message, email_from, [email])

    return redirect('index')



def our_menu(request):
    categories = Category.objects.all()
    return render(request,'our-menu.html',{'categories':categories})

def our_services(request):
    videos = Videos.objects.get(name='process-behind')
    return render(request,'our-services.html',{'videos':videos})

def allergy_advice(request):
    return render(request,'allergy-advice.html')

def contact_us(request):
    return render(request,'contact-us.html')
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

from apps.models import Lead
from django.contrib.auth.hashers import make_password

# Create your views here.


# Authentication

def login(request):
    if request.method == "POST":
        print(request.POST)  # Debugging: See what data is received

        username = request.POST.get("username")  # Use .get() to avoid errors
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Username and password are required")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'auth/login.html')
    
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Ensure all fields are filled
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("register")

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect("register")

        # Create and save the user
        user = User.objects.create(username=username, email=email)
        user.password=make_password(password)
        user.save()

        # Log in the new user and redirect to dashboard
        return redirect("login")

    return render(request, "auth/register.html")

 
def forgot_password(request):
    return render(request, 'auth/forgot-password.html')
 
def reset_password(request):
    return render(request, 'auth/reset-password.html')
 
def email_verification(request):
    return render(request, 'auth/email-verification.html')
 
def two_step_verification(request):
    return render(request, 'auth/email-verification.html')
 
def lock_screen(request):
    return render(request, 'auth/lock-screen.html')
 
def success(request):
    return render(request, 'auth/success.html')
 
 
# Pages

def error_404(request):
    return render(request, 'pages/pages/error/error-404.html')

def error_500(request):
    return render(request, 'pages/pages/error/error-500.html')

def coming_soon(request):
    return render(request, 'pages/pages/coming-soon.html')
 
def blank_page(request):
    return render(request, 'pages/pages/blank-page.html')
 
def under_maintenance(request):
    return render(request, 'pages/pages/under-maintenance.html')

# Application
 
def chat(request):
    return render(request, 'pages/application/chat.html')
 
def video_call(request):
    return render(request, 'pages/application/call/video-call.html')
 
def audio_call(request):
    return render(request, 'pages/application/call/audio-call.html')
 
def call_history(request):
    return render(request, 'pages/application/call/call-history.html')

def calendar(request):
    return render(request, 'pages/application/calendar.html')

def email(request):
    return render(request, 'pages/application/email.html')

def todo(request):
    return render(request, 'pages/application/todo.html')

def notes(request):
    return render(request, 'pages/application/notes.html')

def file_manager(request):
    return render(request, 'pages/application/file-manager.html')

# CRM

def contacts(request):
    contacts = [
        {
            "Customer_Name": "Darlee Robertson",
            "Customer_Image": "assets/img/profiles/avatar-19.jpg",
            "Customer_No": "Facility Manager",
            "Phone": "1234567890",
            "Email": "robertson@example.com",
            "Location": "Germany",
            "Tag": "Collab",
            "Rating": "4.2",
            "Owner": "Hendry",
            "Status": "Active"
        },
        {
            "Customer_Name": "Sharon Roy",
            "Customer_Image": "assets/img/profiles/avatar-20.jpg",
            "Customer_No": "Installer",
            "Phone": "+1 989757485",
            "Email": "sharon@example.com",
            "Location": "USA",
            "Tag": "Promotion",
            "Rating": "5.0",
            "Owner": "Guillory",
            "Status": "Inactive"
        },
        {
            "Customer_Name": "Vaughan",
            "Customer_Image": "assets/img/profiles/avatar-21.jpg",
            "Customer_No": "Senior  Manager",
            "Phone": "+1 546555455",
            "Email": "vaughan12@example.com",
            "Location": "Canada",
            "Tag": "Collab",
            "Rating": "3.5",
            "Owner": "Jami",
            "Status": "Active"
        },
        {
            "Customer_Name": "Jessica",
            "Customer_Image": "assets/img/profiles/avatar-23.jpg",
            "Customer_No": "Test Engineer",
            "Phone": "+1 454478787",
            "Email": "jessica13@example.com",
            "Location": "India",
            "Tag": "Rated",
            "Rating": "4.5",
            "Owner": "Theresa",
            "Status": "Active"
        },
        {
            "Customer_Name": "Carol Thomas",
            "Customer_Image": "assets/img/profiles/avatar-16.jpg",
            "Customer_No": "UI /UX Designer",
            "Phone": "+1 124547845",
            "Email": "caroltho3@example.com",
            "Location": "China",
            "Tag": "Collab",
            "Rating": "4.7",
            "Owner": "Espinosa",
            "Status": "Active"
        },
        {
            "Customer_Name": "Dawn Mercha",
            "Customer_Image": "assets/img/profiles/avatar-22.jpg",
            "Customer_No": "Technician",
            "Phone": "+1 478845447",
            "Email": "dawnmercha@example.com",
            "Location": "Japan",
            "Tag": "Rated",
            "Rating": "5.0",
            "Owner": "Japan",
            "Status": "Active"
        },
        {
            "Customer_Name": "Rachel Hampton",
            "Customer_Image": "assets/img/profiles/avatar-24.jpg",
            "Customer_No": "Software Developer",
            "Phone": "+1 215544845",
            "Email": "rachel@example.com",
            "Location": "Indonesia",
            "Tag": "Promotion",
            "Rating": "3.1",
            "Owner": "Newell",
            "Status": "Active"
        },
        {
            "Customer_Name": "Jonelle Curtiss",
            "Customer_Image": "assets/img/profiles/avatar-25.jpg",
            "Customer_No": "Supervisor",
            "Phone": "+1 121145471",
            "Email": "jonelle@example.com",
            "Location": "Cuba",
            "Tag": "Rating",
            "Rating": "5.0",
            "Owner": "Janet",
            "Status": "Active"
        },
        {
            "Customer_Name": "Jonathan",
            "Customer_Image": "assets/img/profiles/avatar-26.jpg",
            "Customer_No": "Team Lead Dev",
            "Phone": "+1 321454789",
            "Email": "jonathan@example.com",
            "Location": "Isreal",
            "Tag": "Collab",
            "Rating": "2.7",
            "Owner": "Craig",
            "Status": "Active"
        },
        {
            "Customer_Name": "Brook",
            "Customer_Image": "assets/img/profiles/avatar-01.jpg",
            "Customer_No": "Team Lead Dev ",
            "Phone": "+1 278907145",
            "Email": "brook@example.com",
            "Location": "Colombia",
            "Tag": "Promotion",
            "Rating": "3.0",
            "Owner": "Daniel",
            "Status": "Active"
        },
        {
            "Customer_Name": "Eric Adams",
            "Customer_Image": "assets/img/profiles/avatar-06.jpg",
            "Customer_No": "HR Manager",
            "Phone": "+1 19023-78104",
            "Email": "ericadams@example.com",
            "Location": "France",
            "Tag": "Rated",
            "Rating": "3.0",
            "Owner": "Daniel",
            "Status": "Active"
        },
        {
            "Customer_Name": "Richard Cooper",
            "Customer_Image": "assets/img/profiles/avatar-05.jpg",
            "Customer_No": "Devops Engineer",
            "Phone": "+1 18902-63904",
            "Email": "richard@example.com",
            "Location": "Belgium",
            "Tag": "Rated",
            "Rating": "3.0",
            "Owner": "Daniel",
            "Status": "Active"
        },
    ]
    return render(request, 'pages/crm/contacts.html', { 'contacts' : contacts })

def contact_grid(request):
    contact_grid = [
        {
            "customer_name": "Darlee Robertson",
            "customer_image": "assets/img/profiles/avatar-19.jpg",
            "customer_no": "Facility Manager",
            "phone": "1234567890",
            "email": "robertson@example.com",
            "location": "Germany",
            "rating": "4.2",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Sharon Roy",
            "customer_image": "assets/img/profiles/avatar-20.jpg",
            "customer_no": "Installer",
            "phone": "+1 989757485",
            "email": "sharon@example.com",
            "location": "USA",
            "rating": "5.0",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Vaughan",
            "customer_image": "assets/img/profiles/avatar-21.jpg",
            "customer_no": "Senior  Manager",
            "phone": "+1 546555455",
            "email": "vaughan12@example.com",
            "location": "Canada",
            "rating": "3.5",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Jessica",
            "customer_image": "assets/img/profiles/avatar-23.jpg",
            "customer_no": "Test Engineer",
            "phone": "+1 454478787",
            "email": "jessica13@example.com",
            "location": "India",
            "rating": "4.5",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Carol Thomas",
            "customer_image": "assets/img/profiles/avatar-16.jpg",
            "customer_no": "UI /UX Designer",
            "phone": "+1 124547845",
            "email": "caroltho3@example.com",
            "location": "China",
            "rating": "4.7",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Dawn Mercha",
            "customer_image": "assets/img/profiles/avatar-22.jpg",
            "customer_no": "Technician",
            "phone": "+1 478845447",
            "email": "dawnmercha@example.com",
            "location": "Japan",
            "rating": "5.0",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Rachel Hampton",
            "customer_image": "assets/img/profiles/avatar-24.jpg",
            "customer_no": "Software Developer",
            "phone": "+1 215544845",
            "email": "rachel@example.com",
            "location": "Indonesia",
            "rating": "3.1",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Jonelle Curtiss",
            "customer_image": "assets/img/profiles/avatar-25.jpg",
            "customer_no": "Supervisor",
            "phone": "+1 121145471",
            "email": "jonelle@example.com",
            "location": "Cuba",
            "rating": "5.0",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Jonathan",
            "customer_image": "assets/img/profiles/avatar-26.jpg",
            "customer_no": "Team Lead Dev",
            "phone": "+1 321454789",
            "email": "jonathan@example.com",
            "location": "Isreal",
            "rating": "2.7",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Brook",
            "customer_image": "assets/img/profiles/avatar-01.jpg",
            "customer_no": "Team Lead Dev ",
            "phone": "+1 278907145",
            "email": "brook@example.com",
            "location": "Colombia",
            "rating": "3.0",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Eric Adams",
            "customer_image": "assets/img/profiles/avatar-06.jpg",
            "customer_no": "HR Manager",
            "phone": "+1 19023-78104",
            "email": "ericadams@example.com",
            "location": "France",
            "rating": "3.0",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        },
        {
            "customer_name": "Richard Cooper",
            "customer_image": "assets/img/profiles/avatar-05.jpg",
            "customer_no": "Devops Engineer",
            "phone": "+1 18902-63904",
            "email": "richard@example.com",
            "location": "Belgium",
            "rating": "3.0",
            "owner_image": "assets/img/profiles/avatar-14.jpg"
        }
    ]
    return render(request, 'pages/crm/contact-grid.html', {'contact_grid' : contact_grid})

def contact_details(request):
    return render(request, 'pages/crm/contact-details.html')

def companies(request):
    companies = [
        {
            "company_name": "NovaWave LLC",
            "company_image": "assets/img/icons/company-icon-01.svg",
            "phone": "+1 875455453",
            "email": "robertson@example.com",
            "location": "Germany",
            "tag": "Promotion",
            "rating": "4.2",
            "owner": "Hendry",
            "status": "Active"
        },
        {
            "company_name": "BlueSky Industries",
            "company_image": "assets/img/icons/company-icon-02.svg",
            "phone": "+1 989757485",
            "email": "sharon@example.com",
            "location": "USA",
            "tag": "Rated",
            "rating": "5.0",
            "owner": "Guillory",
            "status": "Inactive"
        },
        {
            "company_name": "SilverHawk",
            "company_image": "assets/img/icons/company-icon-03.svg",
            "phone": "+1 546555455",
            "email": "vaughan12@example.com",
            "location": "Canada",
            "tag": "Promotion",
            "rating": "3.5",
            "owner": "Jami",
            "status": "Active"
        },
        {
            "company_name": "SummitPeak",
            "company_image": "assets/img/icons/company-icon-04.svg",
            "phone": "+1 454478787",
            "email": "jessica13@example.com",
            "location": "India",
            "tag": "Promotion",
            "rating": "4.5",
            "owner": "Theresa",
            "status": "Active"
        },
        {
            "company_name": "RiverStone Ventur",
            "company_image": "assets/img/icons/company-icon-05.svg",
            "phone": "+1 124547845",
            "email": "caroltho3@example.com",
            "location": "China",
            "tag": "Promotion",
            "rating": "4.7",
            "owner": "Espinosa",
            "status": "Active"
        },
        {
            "company_name": "Bright Bridge Grp",
            "company_image": "assets/img/icons/company-icon-06.svg",
            "phone": "+1 478845447",
            "email": "dawnmercha@example.com",
            "location": "Japan",
            "tag": "Promotion",
            "rating": "5.0",
            "owner": "Martin",
            "status": "Active"
        },
        {
            "company_name": "CoastalStar Co.",
            "company_image": "assets/img/icons/company-icon-07.svg",
            "phone": "+1 215544845",
            "email": "rachel@example.com",
            "location": "Indonesia",
            "tag": "Promotion",
            "rating": "3.1",
            "owner": "Newell",
            "status": "Active"
        },
        {
            "company_name": "HarborView",
            "company_image": "assets/img/icons/company-icon-08.svg",
            "phone": "+1 121145471",
            "email": "jonelle@example.com",
            "location": "Cuba",
            "tag": "Promotion",
            "rating": "5.0",
            "owner": "Janet",
            "status": "Active"
        },
        {
            "company_name": "Golden Gate Ltd",
            "company_image": "assets/img/icons/company-icon-09.svg",
            "phone": "+1 321454789",
            "email": "jonathan@example.com",
            "location": "Isreal",
            "tag": "Promotion",
            "rating": "2.7",
            "owner": "Craig",
            "status": "Active"
        },
        {
            "company_name": "Redwood Inc",
            "company_image": "assets/img/icons/company-icon-10.svg",
            "phone": "+1 278907145",
            "email": "brook@example.com",
            "location": "Colombia",
            "tag": "Promotion",
            "rating": "3.0",
            "owner": "Daniel",
            "status": "Active"
        },
        {
            "company_name": "SilverHawk",
            "company_image": "assets/img/icons/company-icon-03.svg",
            "phone": "+1 546555455",
            "email": "vaughan12@example.com",
            "location": "Canada",
            "tag": "Promotion",
            "rating": "3.5",
            "owner": "Jami",
            "status": "Active"
        },
        {
            "company_name": "SummitPeak",
            "company_image": "assets/img/icons/company-icon-04.svg",
            "phone": "+1 454478787",
            "email": "jessica13@example.com",
            "location": "India",
            "tag": "Promotion",
            "rating": "4.5",
            "owner": "Theresa",
            "status": "Active"
        },
    ]
    return render(request, 'pages/crm/companies.html', {'companies' : companies})

def companies_grid(request):
    companies_grid = [
        {
            "company_name" : "NovaWave LLC",
            "company_image" : "assets/img/icons/company-icon-01.svg",
            "phone" : "+1 875455453",
            "email" : "robertson@example.com",
            "location" : "Germany",
            "rating" : "4.2"
        },
        {
            "company_name" : "BlueSky Industries",
            "company_image" : "assets/img/icons/company-icon-02.svg",
            "phone" : "+1 989757485",
            "email" : "sharon@example.com",
            "location" : "USA",
            "rating" : "5.0"
        },
        {
            "company_name" : "SilverHawk",
            "company_image" : "assets/img/icons/company-icon-03.svg",
            "phone" : "+1 546555455",
            "email" : "vaughan12@example.com",
            "location" : "Canada",
            "rating" : "3.5"
        },
        {
            "company_name" : "SummitPeak",
            "company_image" : "assets/img/icons/company-icon-04.svg",
            "phone" : "+1 454478787",
            "email" : "jessica13@example.com",
            "location" : "India",
            "rating" : "4.5"
        },
        {
            "company_name" : "RiverStone Ventur",
            "company_image" : "assets/img/icons/company-icon-05.svg",
            "phone" : "+1 124547845",
            "email" : "caroltho3@example.com",
            "location" : "China",
            "rating" : "4.7"
        },
        {
            "company_name" : "Bright Bridge Grp",
            "company_image" : "assets/img/icons/company-icon-06.svg",
            "phone" : "+1 478845447",
            "email" : "dawnmercha@example.com",
            "location" : "Japan",
            "rating" : "5.0"
        },
        {
            "company_name" : "CoastalStar Co.",
            "company_image" : "assets/img/icons/company-icon-07.svg",
            "phone" : "+1 215544845",
            "email" : "rachel@example.com",
            "location" : "Indonesia",
            "rating" : "3.1"
        },
        {
            "company_name" : "HarborView",
            "company_image" : "assets/img/icons/company-icon-08.svg",
            "phone" : "+1 121145471",
            "email" : "jonelle@example.com",
            "location" : "Cuba",
            "rating" : "5.0"
        },
        {
            "company_name" : "Golden Gate Ltd",
            "company_image" : "assets/img/icons/company-icon-09.svg",
            "phone" : "+1 321454789",
            "email" : "jonathan@example.com",
            "location" : "Isreal",
            "rating" : "2.7"
        },
        {
            "company_name" : "Redwood Inc",
            "company_image" : "assets/img/icons/company-icon-10.svg",
            "phone" : "+1 278907145",
            "email" : "brook@example.com",
            "location" : "Colombia",
            "rating" : "3.0"
        },
        {
            "company_name" : "SilverHawk",
            "company_image" : "assets/img/icons/company-icon-03.svg",
            "phone" : "+1 546555455",
            "email" : "vaughan12@example.com",
            "location" : "Canada",
            "rating" : "3.5"
        },
        {
            "company_name" : "SummitPeak",
            "company_image" : "assets/img/icons/company-icon-04.svg",
            "phone" : "+1 454478787",
            "email" : "jessica13@example.com",
            "location" : "India",
            "rating" : "4.5"
        }
    ]
    return render(request, 'pages/crm/companies-grid.html', { 'companies_grid' : companies_grid })

def company_details(request):
    return render(request, 'pages/crm/company-details.html')

def deals(request):
    deals = [
        {
            "Deal_Name": "Collins",
            "Stage": "Qualify To Buy",
            "Deal_Value": "$04,51,000",
            "Tag": "Collab",
            "Close_date": "25 Sep 2023",
            "Owner": "Hendry",
            "Probability": "90%",
            "Status": "Won"
        },
        {
            "Deal_Name": "Konopelski",
            "Stage": "Proposal Made",
            "Deal_Value": "$03,12,500",
            "Tag": "Rated",
            "Close_date": "29 Sep 2023",
            "Owner": "Guillory",
            "Probability": "15 %",
            "Status": "Lost"
        },
        {
            "Deal_Name": "Adams",
            "Stage": "Contact Made",
            "Deal_Value": "$04,14,800",
            "Tag": "Rejected",
            "Close_date": "04 Oct 2023",
            "Owner": "Jami",
            "Probability": "95 %",
            "Status": "Won"
        },
        {
            "Deal_Name": "Schumm",
            "Stage": "Qualify To Buy",
            "Deal_Value": "$11,14,400",
            "Tag": "Collab",
            "Close_date": "15 Oct 2023",
            "Owner": "Therasa",
            "Probability": "99 %",
            "Status": "Won"
        },
        {
            "Deal_Name": "Wisozk",
            "Stage": "Presentation",
            "Deal_Value": "$16,11,400",
            "Tag": "Rated",
            "Close_date": "27 Oct 2023",
            "Owner": "Espinosa",
            "Probability": "10 %",
            "Status": "Open"
        },
        {
            "Deal_Name": "Heller",
            "Stage": "Appointment",
            "Deal_Value": "$78,11,800",
            "Tag": "Rated",
            "Close_date": "07 Nov 2023",
            "Owner": "Martin",
            "Probability": "70 %",
            "Status": "Won"
        },
        {
            "Deal_Name": "Gutkowski",
            "Stage": "Proposal Made",
            "Deal_Value": "$09,05,947",
            "Tag": "Promotion",
            "Close_date": "12 Nov 2023",
            "Owner": "Newell",
            "Probability": "10 %",
            "Status": "Open"
        },
        {
            "Deal_Name": "Walter",
            "Stage": "Qualify To Buy",
            "Deal_Value": "$04,51,000",
            "Tag": "Rejected",
            "Close_date": "23 Nov 2023",
            "Owner": "Janet",
            "Probability": "90 %",
            "Status": "Won"
        },
        {
            "Deal_Name": "Hansen",
            "Stage": "Appointment",
            "Deal_Value": "$72,14,078",
            "Tag": "Collab",
            "Close_date": "11 Dec 2023",
            "Owner": "Craig",
            "Probability": "40 %",
            "Status": "Won"
        },
        {
            "Deal_Name": "Leuschke",
            "Stage": "Proposal Made",
            "Deal_Value": "$09,05,947",
            "Tag": "Rated",
            "Close_date": "17 Dec 2023",
            "Owner": "Daniel",
            "Probability": "47 %",
            "Status": "Lost"
        },
    ]
    return render(request, 'pages/crm/deals.html', {'deals' : deals})

def deals_kanban(request):
    return render(request, 'pages/crm/deals-kanban.html')

def deals_details(request):
    return render(request, 'pages/crm/deals-details.html')



def leads(request):
    lead_data = Lead.objects.all()
    return render(request, 'pages/crm/leads.html', {'leads': lead_data})

from django.shortcuts import render, redirect
from .models import Lead

def add_lead(request):
    if request.method == "POST":
        print("✅ POST Data Received:", request.POST)  # Debugging
        print("✅ FILES Received:", request.FILES)  # Debugging

        name = request.POST.get("name")
        lead_type = request.POST.get("lead_type")
        company_name = request.POST.get("company_name")
        company_image = request.FILES.get("company_image")
        # company_address = request.POST.get("company_address")
        value = request.POST.get("value")
        currency = request.POST.get("currency")
        phone = request.POST.get("phone")
        phone_type = request.POST.get("phone_type")
        email = request.POST.get("email") or "test.gmail.com"
        source = request.POST.get("source")
        industry = request.POST.get("industry")
        owner = request.POST.get("owner")
        tags = request.POST.get("tags")
        description = request.POST.get("description")
        visibility = request.POST.get("visibility")
        status = request.POST.get("status", "new")

        # If no data is received, return an error response
        if not name:
            return render(request, "pages/crm/add_lead.html", {"error": "No data received!"})

        # Creating the lead object
        lead = Lead.objects.create(
            name=name,
            lead_type=lead_type,
            company_name=company_name,
            company_image=company_image,
            # company_address=company_address,
            value=value,
            currency=currency,
            phone=phone,
            phone_type=phone_type,
            email=email,
            source=source,
            industry=industry,
            owner=owner,
            tags=tags,
            description=description,
            # visibility=visibility,
            status=status
        )
        print("✅ Lead Created Successfully:", lead)

        return redirect('leads')

    return render(request, 'pages/crm/add_lead.html')


def leads_details(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)  # Fetch the lead based on ID
    return render(request, 'pages/crm/leads.html', {'lead': lead})


def pipeline(request):
    pipeline = [
        {
            "name": "Sales",
            "deal_value": "$4,50,664",
            "no_deal": "315",
            "stage": "Win",
            "createdate": "25 Sep 2023",
            "status": "Active"
        },
        {
            "name": "Marketing",
            "deal_value": "$3,12,893",
            "no_deal": "447",
            "stage": "Win",
            "createdate": "29 Sep 2023",
            "status": "Active"
        },
        {
            "name": "Email",
            "deal_value": "$2,89,274",
            "no_deal": "654",
            "stage": "In Pipeline",
            "createdate": "15 Oct 2023",
            "status": "Active"
        },
        {
            "name": "Chats",
            "deal_value": "$1,59,326",
            "no_deal": "768",
            "stage": "Win",
            "createdate": "29 Oct 2023",
            "status": "Active"
        },
        {
            "name": "Operational",
            "deal_value": "$2,90,173",
            "no_deal": "142",
            "stage": "Win",
            "createdate": "03 Nov 2023",
            "status": "Inactive"
        },
        {
            "name": "Collaborative",
            "deal_value": "$4,51,417",
            "no_deal": "315",
            "stage": "Conversation",
            "createdate": "17 Nov 2023",
            "status": "Active"
        },
        {
            "name": "Differentiate",
            "deal_value": "$3,17,589",
            "no_deal": "478",
            "stage": "Lost",
            "createdate": "23 Nov 2023",
            "status": "Active"
        },
        {
            "name": "Interact ",
            "deal_value": "$1,69,146",
            "no_deal": "664",
            "stage": "Lost",
            "createdate": "09 Dec 2023",
            "status": "Active"
        },
    ]
    return render(request, 'pages/crm/pipeline.html', {'pipeline' : pipeline })

def campaign(request):
    campaign = [
        {
            "name": "Distribution",
            "type": "Public Relations",
            "mem_image1": "assets/img/profiles/avatar-14.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "25 Sep 2023",
            "end_date": "29 Sep 2023",
            "created_date": "25 Sep 2023",
            "open": "40.5%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Success"
        },
        {
            "name": "Merchandising",
            "type": "Content Marketing",
            "mem_image1": "assets/img/profiles/avatar-03.jpg",
            "mem_image2": "assets/img/profiles/avatar-05.jpg",
            "mem_image3": "assets/img/profiles/avatar-06.jpg",
            "start_date": "03 Oct 2023",
            "end_date": "16 Oct 2023",
            "created_date": "03 Oct 2023",
            "open": "65.5%",
            "close": "83.5%",
            "unscubscribe": "67.5%",
            "delivered": "32.0%",
            "converstion": "22.5%",
            "status": "Pending"
        },
        {
            "name": "Pricing",
            "type": "Social Marketing",
            "mem_image1": "assets/img/profiles/avatar-04.jpg",
            "mem_image2": "assets/img/profiles/avatar-01.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "17 Oct 2023",
            "end_date": "28 Oct 2023",
            "created_date": "17 Oct 2023",
            "open": "64.0%",
            "close": "97.0%",
            "unscubscribe": "14.5%",
            "delivered": "38.5%",
            "converstion": "53.0%",
            "status": "Success",
        },
        {
            "name": "Increased sales",
            "type": "Brand",
            "mem_image1": "assets/img/profiles/avatar-12.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-13.jpg",
            "start_date": "07 Nov 2023",
            "end_date": "14 Nov 2023",
            "created_date": "07 Nov 2023",
            "open": "32.5%",
            "close": "57.0%",
            "unscubscribe": "26.3%",
            "delivered": "65.8%",
            "converstion": "17.4%",
            "status": "Bounced"
        },
        {
            "name": "Brand recognition",
            "type": "Sales",
            "mem_image1": "assets/img/profiles/avatar-10.jpg",
            "mem_image2": "assets/img/profiles/avatar-11.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "19 Nov 2023",
            "end_date": "26 Nov 2023",
            "created_date": "19 Nov 2023",
            "open": "72.6%",
            "close": "53.5%",
            "unscubscribe": "16.5%",
            "delivered": "83.0%",
            "converstion": "29.3%",
            "status": "Running"
        },
        {
            "name": "Enhanced brand",
            "type": "Media",
            "mem_image1": "assets/img/profiles/avatar-14.jpg",
            "mem_image2": "assets/img/profiles/avatar-09.jpg",
            "mem_image3": "assets/img/profiles/avatar-08.jpg",
            "start_date": "02 Dec 2023",
            "end_date": "13 Dec 2023",
            "created_date": "02 Dec 2023",
            "open": "56.3%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Paused"
        },
        {
            "name": "Repeat customers",
            "type": "Rebranding",
            "mem_image1": "assets/img/profiles/avatar-06.jpg",
            "mem_image2": "assets/img/profiles/avatar-07.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "17 Dec 2023",
            "end_date": "27 Dec 2023",
            "created_date": "17 Dec 2023",
            "open": "63.2%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "87.8%",
            "status": "Success"
        },
        {
            "name": "Competitor ",
            "type": "Product launch",
            "mem_image1": "assets/img/profiles/avatar-04.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-05.jpg",
            "start_date": "06 Jan 2024",
            "end_date": "17 Jan 2024",
            "created_date": "06 Jan 2024",
            "open": "40.5%",
            "close": "52.7%",
            "unscubscribe": "13.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Paused"
        }
    ]
    return render(request, 'pages/crm/campaign.html', { 'campaign' : campaign })

def campaign_complete(request):
    campaign_complete = [
        {
            "name": "Distribution",
            "type": "Public Relations",
            "mem_image1": "assets/img/profiles/avatar-14.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "25 Sep 2023",
            "end_date": "29 Sep 2023",
            "created_date": "25 Sep 2023",
            "open": "40.5%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Success"
        },
        {
            "name": "Merchandising",
            "type": "Content Marketing",
            "mem_image1": "assets/img/profiles/avatar-03.jpg",
            "mem_image2": "assets/img/profiles/avatar-05.jpg",
            "mem_image3": "assets/img/profiles/avatar-06.jpg",
            "start_date": "03 Oct 2023",
            "end_date": "16 Oct 2023",
            "created_date": "03 Oct 2023",
            "open": "65.5%",
            "close": "83.5%",
            "unscubscribe": "67.5%",
            "delivered": "32.0%",
            "converstion": "22.5%",
            "status": "Pending"
        },
        {
            "name": "Pricing",
            "type": "Social Marketing",
            "mem_image1": "assets/img/profiles/avatar-04.jpg",
            "mem_image2": "assets/img/profiles/avatar-01.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "17 Oct 2023",
            "end_date": "28 Oct 2023",
            "created_date": "17 Oct 2023",
            "open": "64.0%",
            "close": "97.0%",
            "unscubscribe": "14.5%",
            "delivered": "38.5%",
            "converstion": "53.0%",
            "status": "Success",
        },
        {
            "name": "Increased sales",
            "type": "Brand",
            "mem_image1": "assets/img/profiles/avatar-12.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-13.jpg",
            "start_date": "07 Nov 2023",
            "end_date": "14 Nov 2023",
            "created_date": "07 Nov 2023",
            "open": "32.5%",
            "close": "57.0%",
            "unscubscribe": "26.3%",
            "delivered": "65.8%",
            "converstion": "17.4%",
            "status": "Bounced"
        },
        {
            "name": "Brand recognition",
            "type": "Sales",
            "mem_image1": "assets/img/profiles/avatar-10.jpg",
            "mem_image2": "assets/img/profiles/avatar-11.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "19 Nov 2023",
            "end_date": "26 Nov 2023",
            "created_date": "19 Nov 2023",
            "open": "72.6%",
            "close": "53.5%",
            "unscubscribe": "16.5%",
            "delivered": "83.0%",
            "converstion": "29.3%",
            "status": "Running"
        },
        {
            "name": "Enhanced brand",
            "type": "Media",
            "mem_image1": "assets/img/profiles/avatar-14.jpg",
            "mem_image2": "assets/img/profiles/avatar-09.jpg",
            "mem_image3": "assets/img/profiles/avatar-08.jpg",
            "start_date": "02 Dec 2023",
            "end_date": "13 Dec 2023",
            "created_date": "02 Dec 2023",
            "open": "56.3%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Paused"
        },
        {
            "name": "Repeat customers",
            "type": "Rebranding",
            "mem_image1": "assets/img/profiles/avatar-06.jpg",
            "mem_image2": "assets/img/profiles/avatar-07.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "17 Dec 2023",
            "end_date": "27 Dec 2023",
            "created_date": "17 Dec 2023",
            "open": "63.2%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "87.8%",
            "status": "Success"
        },
        {
            "name": "Competitor ",
            "type": "Product launch",
            "mem_image1": "assets/img/profiles/avatar-04.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-05.jpg",
            "start_date": "06 Jan 2024",
            "end_date": "17 Jan 2024",
            "created_date": "06 Jan 2024",
            "open": "40.5%",
            "close": "52.7%",
            "unscubscribe": "13.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Paused"
        }
    ]
    return render(request, 'pages/crm/campaign-complete.html', { 'campaign_complete' : campaign_complete })

def campaign_archieve(request):
    campaign_archieve = [
        {
            "name": "Distribution",
            "type": "Public Relations",
            "mem_image1": "assets/img/profiles/avatar-14.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "25 Sep 2023",
            "end_date": "29 Sep 2023",
            "created_date": "25 Sep 2023",
            "open": "40.5%",
            "close": "20.5%",
            "unscubscribe": "30.5%",
            "delivered": "70.5%",
            "converstion": "35.0%",
            "status": "Success"
        },
        {
            "name": "Merchandising",
            "type": "Content Marketing",
            "mem_image1": "assets/img/profiles/avatar-03.jpg",
            "mem_image2": "assets/img/profiles/avatar-05.jpg",
            "mem_image3": "assets/img/profiles/avatar-06.jpg",
            "start_date": "03 Oct 2023",
            "end_date": "16 Oct 2023",
            "created_date": "03 Oct 2023",
            "open": "65.5%",
            "close": "83.5%",
            "unscubscribe": "67.5%",
            "delivered": "32.0%",
            "converstion": "22.5%",
            "status": "Pending"
        },
        {
            "name": "Pricing",
            "type": "Social Marketing",
            "mem_image1": "assets/img/profiles/avatar-04.jpg",
            "mem_image2": "assets/img/profiles/avatar-01.jpg",
            "mem_image3": "assets/img/profiles/avatar-16.jpg",
            "start_date": "17 Oct 2023",
            "end_date": "28 Oct 2023",
            "created_date": "17 Oct 2023",
            "open": "64.0%",
            "close": "97.0%",
            "unscubscribe": "14.5%",
            "delivered": "38.5%",
            "converstion": "53.0%",
            "status": "Success"
        },
        {
            "name": "Increased sales",
            "type": "Brand",
            "mem_image1": "assets/img/profiles/avatar-12.jpg",
            "mem_image2": "assets/img/profiles/avatar-15.jpg",
            "mem_image3": "assets/img/profiles/avatar-13.jpg",
            "start_date": "07 Nov 2023",
            "end_date": "14 Nov 2023",
            "created_date": "07 Nov 2023",
            "open": "32.5%",
            "close": "57.0%",
            "unscubscribe": "26.3%",
            "delivered": "65.8%",
            "converstion": "17.4%",
            "status": "Bounced"
        }
    ]
    return render(request, 'pages/crm/campaign-archieve.html', { 'campaign_archieve' : campaign_archieve })

def projects(request):
    projects = [
        {
            "name": "Truelysell",
            "client": "NovaWave LLC",
            "pro_img": "assets/img/priority/truellysel.svg",
            'client_img': "assets/img/icons/company-icon-01.svg",
            "priority": "High",
            "start_date": "25 Sep 2023",
            "end_date": "15 Oct 2023",
            "stage": "Plan",
            "type": "Web App",
            "status": "Active"
        },
        {
            "name": "Dreamschat",
            "client": "BlueSky Industries",
            "pro_img": "assets/img/priority/dreamchat.svg",
            'client_img': "assets/img/icons/company-icon-02.svg",
            "priority": "Medium",
            "start_date": "29 Sep 2023",
            "end_date": "19 Oct 2023",
            "stage": "Develop",
            "type": "Web App",
            "status": "Inactive"
        },
        {
            "name": "Truelysell",
            "client": "SilverHawk",
            "pro_img": "assets/img/priority/truellysell.svg",
            'client_img': "assets/img/icons/company-icon-03.svg",
            "priority": "High",
            "start_date": "05 Oct 2023",
            "end_date": "12 Oct 2023",
            "stage": "Completed",
            "type": "Web App",
            "status": "Active"
        },
        {
            "name": "Servbook",
            "client": "SummitPeak",
            "pro_img": "assets/img/priority/servbook.svg",
            'client_img': "assets/img/icons/company-icon-04.svg",
            "priority": "Medium",
            "start_date": "14 Oct 2023",
            "end_date": "24 Oct 2023",
            "stage": "Design",
            "type": "Web App",
            "status": "Inactive"
        },
        {
            "name": "DreamPOS",
            "client": "RiverStone Ventur",
            "pro_img": "assets/img/priority/dream-pos.svg",
            'client_img': "assets/img/icons/company-icon-05.svg",
            "priority": "Low",
            "start_date": "15 Nov 2023",
            "end_date": "22 Nov 2023",
            "stage": "Design",
            "type": "Web App",
            "status": "Inactive"
        },
        {
            "name": "Kofejob",
            "client": "CoastalStar Co.",
            "pro_img": "assets/img/priority/project-01.svg",
            'client_img': "assets/img/icons/company-icon-06.svg",
            "priority": "High",
            "start_date": "25 Nov 2023",
            "end_date": "09 Dec 2023",
            "stage": "Develop",
            "type": "Meeting",
            "status": "Active"
        },
        {
            "name": "Doccure",
            "client": "HarborView",
            "pro_img": "assets/img/priority/project-02.svg",
            'client_img': "assets/img/icons/company-icon-07.svg",
            "priority": "Medium",
            "start_date": "08 Dec 2023",
            "end_date": "16 Dec 2023",
            "stage": "Completed",
            "type": "Web App",
            "status": "Inactive"
        },
        {
            "name": "Best@laundry",
            "client": "Golden Gate Ltd",
            "pro_img": "assets/img/priority/best.svg",
            'client_img': "assets/img/icons/company-icon-08.svg",
            "priority": "Low",
            "start_date": "21 Dec 2023",
            "end_date": "13 Jan 2024",
            "stage": "Completed",
            "type": "Meeting",
            "status": "Inactive"
        },
        {
            "name": "POS",
            "client": "CoastalStar Inc",
            "pro_img": "assets/img/priority/dream-pos.svg",
            'client_img': "assets/img/icons/company-icon-06.svg",
            "priority": "Medium",
            "start_date": "01 Jan 2024",
            "end_date": "11 Jan 2024",
            "stage": "Develop",
            "type": "Web App",
            "status": "Inactive"
        },
        {
            "name": "Bookserv",
            "client": "Redwood Inc",
            "pro_img": "assets/img/priority/servbook.svg",
            'client_img': "assets/img/icons/company-icon-09.svg",
            "priority": "Medium",
            "start_date": "12 Jan 2024",
            "end_date": "29 Jan 2024",
            "stage": "Develop",
            "type": "Meeting",
            "status": "Inactive"
        },
        {
            "name": "Dreamchat",
            "client": "Redwood Inc",
            "pro_img": "assets/img/priority/sports.svg",
            'client_img': "assets/img/icons/company-icon-09.svg",
            "priority": "Medium",
            "start_date": "16 Jan 2024",
            "end_date": "25 Jan 2024",
            "stage": "Develop",
            "type": "Meeting",
            "status": "Inactive"
        },
        {
            "name": "Sports",
            "client": "Ventur",
            "pro_img": "assets/img/priority/best.svg",
            'client_img': "assets/img/icons/company-icon-08.svg",
            "priority": "Medium",
            "start_date": "12 Jan 2024",
            "end_date": "29 Jan 2024",
            "stage": "Develop",
            "type": "Web App",
            "status": "Inactive"
        }
    ]
    return render(request, 'pages/crm/projects.html', { 'projects' : projects })

def project_grid(request):
    project_grid = [
	{
	  "id": "#12145",
	  "name": "Truelysell",
	  "client": "NovaWave LLC",
	  "pro_img": "assets/img/priority/truellysel.svg",
      "client_img": "assets/img/icons/company-icon-01.svg",
	  "start_date": "25 Sep 2023",
	  "end_date": "15 Oct 2023",
	  "type": "Web App",
	  "value": "$03,50,000",
	  "hrs": "100",
	  "mem_image1": "assets/img/profiles/avatar-14.jpg",
	  "mem_image2": "assets/img/profiles/avatar-15.jpg",
	  "mem_image3": "assets/img/profiles/avatar-16.jpg"
	},
	{
	  "id": "#12146",
	  "name": "Dreamschat",
	  "client": "BlueSky Industries",
	  "pro_img": "assets/img/priority/dreamchat.svg",
      "client_img": "assets/img/icons/company-icon-02.svg",
	  "start_date": "29 Sep 2023",
	  "end_date": "19 Oct 2023",
	  "type": "Web App",
	  "value": "$02,15,000",
	  "hrs": "80",
	  "mem_image1": "assets/img/profiles/avatar-03.jpg",
	  "mem_image2": "assets/img/profiles/avatar-05.jpg",
	  "mem_image3": "assets/img/profiles/avatar-06.jpg"
	},
	{
	  "id": "#12147",
	  "name": "Truelysell",
	  "client": "SilverHawk",
	  "pro_img": "assets/img/priority/truellysell.svg",
      "client_img": "assets/img/icons/company-icon-03.svg",
	  "start_date": "05 Oct 2023",
	  "end_date": "12 Oct 2023",
	  "type": "Web App",
	  "value": "$01,45,000",
	  "hrs": "75",
	  "mem_image1": "assets/img/profiles/avatar-04.jpg",
	  "mem_image2": "assets/img/profiles/avatar-01.jpg",
	  "mem_image3": "assets/img/profiles/avatar-16.jpg"
	},
	{
	  "id": "#12148",
	  "name": "Servbook",
	  "client": "SummitPeak",
	  "pro_img": "assets/img/priority/servbook.svg",
      "client_img": "assets/img/icons/company-icon-04.svg",
	  "start_date": "14 Oct 2023",
	  "end_date": "24 Oct 2023",
	  "type": "Web App",
	  "value": "$02,15,000",
	  "hrs": "60",
	  "mem_image1": "assets/img/profiles/avatar-12.jpg",
	  "mem_image2": "assets/img/profiles/avatar-15.jpg",
	  "mem_image3": "assets/img/profiles/avatar-13.jpg"
	},
	{
	  "id": "#12149",
	  "name": "DreamPOS",
	  "client": "RiverStone Ventur",
	  "pro_img": "assets/img/priority/dream-pos.svg",
      "client_img": "assets/img/icons/company-icon-05.svg",
	  "start_date": "15 Nov 2023",
	  "end_date": "22 Nov 2023",
	  "type": "Web App",
	  "value": "$03,64,000",
	  "hrs": "72",
	  "mem_image1": "assets/img/profiles/avatar-10.jpg",
	  "mem_image2": "assets/img/profiles/avatar-11.jpg",
	  "mem_image3": "assets/img/profiles/avatar-16.jpg"
	},
	{
	  "id": "#12150",
	  "name": "Kofejob",
	  "client": "CoastalStar Co.",
	  "pro_img": "assets/img/priority/project-01.svg",
      "client_img": "assets/img/icons/company-icon-06.svg",
	  "start_date": "25 Nov 2023",
	  "end_date": "09 Dec 2023",
	  "type": "Meeting",
	  "value": "$02,12,000",
	  "hrs": "96",
	  "mem_image1": "assets/img/profiles/avatar-14.jpg",
	  "mem_image2": "assets/img/profiles/avatar-09.jpg",
	  "mem_image3": "assets/img/profiles/avatar-08.jpg"
	},
	{
	  "id": "#12151",
	  "name": "Doccure",
	  "client": "HarborView",
	  "pro_img": "assets/img/priority/project-02.svg",
      "client_img": "assets/img/icons/company-icon-07.svg",
	  "start_date": "08 Dec 2023",
	  "end_date": "16 Dec 2023",
	  "type": "Web App",
	  "value": "$04,18,000",
	  "hrs": "85",
	  "mem_image1": "assets/img/profiles/avatar-06.jpg",
	  "mem_image2": "assets/img/profiles/avatar-07.jpg",
	  "mem_image3": "assets/img/profiles/avatar-16.jpg"
	},
	{
	  "id": "#12152",
	  "name": "Best@laundry",
	  "client": "Golden Gate Ltd",
	  "pro_img": "assets/img/priority/best.svg",
      "client_img": "assets/img/icons/company-icon-08.svg",
	  "start_date": "21 Dec 2023",
	  "end_date": "13 Jan 2024",
	  "type": "Meeting",
	  "value": "$01,23,000",
	  "hrs": "65",
	  "mem_image1": "assets/img/profiles/avatar-04.jpg",
	  "mem_image2": "assets/img/profiles/avatar-15.jpg",
	  "mem_image3": "assets/img/profiles/avatar-05.jpg"
	},
	{
	  "id": "#12153",
	  "name": "POS",
	  "client": "CoastalStar Inc",
	  "pro_img": "assets/img/priority/dream-pos.svg",
      "client_img": "assets/img/icons/company-icon-06.svg",
	  "start_date": "01 Jan 2024",
	  "end_date": "11 Jan 2024",
	  "type": "Web App",
	  "value": "$03,64,000",
	  "hrs": "60",
	  "mem_image1": "assets/img/profiles/avatar-08.jpg",
	  "mem_image2": "assets/img/profiles/avatar-12.jpg",
	  "mem_image3": "assets/img/profiles/avatar-04.jpg"
	},
	{
	  "id": "#12153",
	  "name": "Bookserv",
	  "client": "Redwood Inc",
	  "pro_img": "assets/img/priority/servbook.svg",
      "client_img": "assets/img/icons/company-icon-09.svg",
	  "start_date": "12 Jan 2024",
	  "end_date": "29 Jan 2024",
	  "type": "Meeting",
	  "value": " $04,10,000",
	  "hrs": "56",
	  "mem_image1": "assets/img/profiles/avatar-12.jpg",
	  "mem_image2": "assets/img/profiles/avatar-14.jpg",
	  "mem_image3": "assets/img/profiles/avatar-01.jpg"
	},
	{
	  "id": "#12153",
	  "name": "Dreamchat",
	  "client": "Redwood Inc",
	  "pro_img": "assets/img/priority/sports.svg",
      "client_img": "assets/img/icons/company-icon-09.svg",
	  "start_date": "16 Jan 2024",
	  "end_date": "25 Jan 2024",
	  "type": "Meeting",
	  "value": "$02,19,000",
	  "hrs": "55",
	  "mem_image1": "assets/img/profiles/avatar-08.jpg",
	  "mem_image2": "assets/img/profiles/avatar-15.jpg",
	  "mem_image3": "assets/img/profiles/avatar-12.jpg"
	},
	{
	  "id": "#12153",
	  "name": "Sports",
	  "client": "Ventur",
	  "pro_img": "assets/img/priority/best.svg",
      "client_img": "assets/img/icons/company-icon-08.svg",
	  "start_date": "12 Jan 2024",
	  "end_date": "29 Jan 2024",
	  "type": "Web App",
	  "value": "$01,23,000",
	  "hrs": "63",
	  "mem_image1": "assets/img/profiles/avatar-01.jpg",
	  "mem_image2": "assets/img/profiles/avatar-11.jpg",
	  "mem_image3": "assets/img/profiles/avatar-14.jpg"
	}
]
    return render(request, 'pages/crm/project-grid.html', { 'project_grid' : project_grid })

def project_details(request):
    return render(request, 'pages/crm/project-details.html')

def tasks(request):
    return render(request, 'pages/crm/tasks.html')

def tasks_important(request):
    return render(request, 'pages/crm/tasks-important.html')

def tasks_completed(request):
    return render(request, 'pages/crm/tasks-completed.html')

def proposals(request):
    proposals = [
        {
            "Proposals_ID": "#1493024",
            "Subject": "SEO Proposal",
            "Send_To": "NovaWave LLC",
            "Send_Image": "assets/img/icons/company-icon-01.svg",
            "Total_Value": "$2,05,426",
            "Date": "15 May 2024",
            "Open_till": "15 Aug 2023",
            "Project": "Truelysell",
            "Project_Image": "assets/img/priority/truellysel.svg",
            "Created_Date": "21 May 2024",
            "Status": "Accepted"
        },
        {
            "Proposals_ID": "#1493023",
            "Subject": "Web Design",
            "Send_To": "Redwood Inc",
            "Send_Image": "assets/img/icons/company-icon-10.svg",
            "Total_Value": "$2,105",
            "Date": "16 Jan 2024",
            "Open_till": "15 Sep 2024",
            "Project": "Dreamsports",
            "Project_Image": "assets/img/priority/project-01.svg",
            "Created_Date": "15 Apr 2024",
            "Status": "Declined"
        },
        {
            "Proposals_ID": "#1493022",
            "Subject": "Logo & Branding",
            "Send_To": "HarborView",
            "Send_Image": "assets/img/icons/company-icon-08.svg",
            "Total_Value": "$4,05,656",
            "Date": "17 Sep 2024",
            "Open_till": "15 Nov 2024",
            "Project": "Best@laundry",
            "Project_Image": "assets/img/priority/best.svg",
            "Created_Date": "12 Mar 2024",
            "Status": "Deleted"
        },
        {
            "Proposals_ID": "#1493021",
            "Subject": "Development",
            "Send_To": "CoastalStar Co.",
            "Send_Image": "assets/img/icons/company-icon-07.svg",
            "Total_Value": "$2,05,426",
            "Date": "18 May 2024",
            "Open_till": "15 Jun 2024",
            "Project": "Doccure",
            "Project_Image": "assets/img/priority/project-02.svg",
            "Created_Date": "15 Feb 2024",
            "Status": "Draft"
        },
        {
            "Proposals_ID": "#1493020",
            "Subject": "SEO Proposal",
            "Send_To": "RiverStone Ventur",
            "Send_Image": "assets/img/icons/company-icon-05.svg",
            "Total_Value": "$3,15,145",
            "Date": "19 Aug 2024",
            "Open_till": "15 Oct 2024",
            "Project": "Kofejob",
            "Project_Image": "assets/img/priority/project-01.svg",
            "Created_Date": "15 Jan 2024",
            "Status": "Sent"
        },
        {
            "Proposals_ID": "#1493019",
            "Subject": "Web Design",
            "Send_To": "Summit Peak",
            "Send_Image": "assets/img/icons/company-icon-04.svg",
            "Total_Value": "$6,154",
            "Date": "20 May 2024",
            "Open_till": "08 Aug 2024",
            "Project": "DreamPOS",
            "Project_Image": "assets/img/priority/dream-pos.svg",
            "Created_Date": "15 Dec 2023",
            "Status": "Draft"
        },
        {
            "Proposals_ID": "#1493018",
            "Subject": "Logo",
            "Send_To": "Silver Hawk",
            "Send_Image": "assets/img/icons/company-icon-03.svg",
            "Total_Value": "$1,457",
            "Date": "22 Aug 2024",
            "Open_till": "25 Jan 2025",
            "Project": "Servbook",
            "Project_Image": "assets/img/priority/servbook.svg",
            "Created_Date": "15 Nov 2023",
            "Status": "Paused"
        },
        {
            "Proposals_ID": "#1493017",
            "Subject": "Branding",
            "Send_To": "BlueSky Industries",
            "Send_Image": "assets/img/icons/company-icon-02.svg",
            "Total_Value": "$2,01,464",
            "Date": "15 May 2024",
            "Open_till": "12 Aug 2024",
            "Project": "Truelysell",
            "Project_Image": "assets/img/priority/truellysell.svg",
            "Created_Date": "15 Sep 2023",
            "Status": "Accepted"
        },
        {
            "Proposals_ID": "#1493018",
            "Subject": "Development",
            "Send_To": "Golden Gate Ltd",
            "Send_Image": "assets/img/icons/company-icon-09.svg",
            "Total_Value": "$1,10,145",
            "Date": "14 Aug 2024",
            "Open_till": "07 Dec 2024",
            "Project": "Dreamschat",
            "Project_Image": "assets/img/priority/dreamchat.svg",
            "Created_Date": "15 Aug 2023",
            "Status": "Declined"
        },
    ]
    return render(request, 'pages/crm/proposals.html', { 'proposals' : proposals})

def proposals_grid(request):
    proposals_grid = [
    {
        "Image": "assets/img/icons/company-icon-01.svg",
        "Badge": "Accepted"
    },
    {
        "Image": "assets/img/icons/company-icon-02.svg",
        "Badge": "Deleted"
    },
    {
        "Image": "assets/img/icons/company-icon-03.svg",
        "Badge": "Draft"
    },
    {
        "Image": "assets/img/icons/company-icon-04.svg",
        "Badge": "Declined"
    },
    {
        "Image": "assets/img/icons/company-icon-05.svg",
        "Badge": "Declined"
    },
    {
        "Image": "assets/img/icons/company-icon-06.svg",
        "Badge": "Sent"
    },
    {
        "Image": "assets/img/icons/company-icon-07.svg",
        "Badge": "Deleted"
    },
    {
        "Image": "assets/img/icons/company-icon-08.svg",
        "Badge": "Draft"
    }
]
    return render(request, 'pages/crm/proposals-grid.html', { 'proposals_grid' : proposals_grid })

def contracts(request):
    contracts = [
        {
            "ContractID": "#1493024",
            "Subject": "SEO Proposal",
            "Customer": "NovaWave LLC",
            "Image": "assets/img/icons/company-icon-01.svg",
            "ContractValue": "$2,05,426",
            "ContractType": "Contracts under Seal",
            "StartDate": "15 Aug 2024",
            "EndDate": "15 May 2024",
        },
        {
            "ContractID": "#1493023",
            "Subject": "Web Design",
            "Customer": "Redwood Inc",
            "Image": "assets/img/icons/company-icon-10.svg",
            "ContractValue": "$2,105",
            "ContractType": "Implied Contracts",
            "StartDate": "15 Sep 2024",
            "EndDate": "15 Apr 2024",
        },
        {
            "ContractID": "#1493022",
            "Subject": "Logo & Branding",
            "Customer": "HarborView",
            "Image": "assets/img/icons/company-icon-08.svg",
            "ContractValue": "$4,05,656",
            "ContractType": "Implied Contracts",
            "StartDate": "15 Nov 2024",
            "EndDate": "15 Mar 2024",
        },
        {
            "ContractID": "#1493021",
            "Subject": "Development",
            "Customer": "CoastalStar Co.",
            "Image": "assets/img/icons/company-icon-07.svg",
            "ContractValue": "$2,05,426",
            "ContractType": "Executory Contracts",
            "StartDate": "15 Jun 2024",
            "EndDate": "15 Feb 2024",
        },
        {
            "ContractID": "#1493020",
            "Subject": "SEO Proposal",
            "Customer": "RiverStone Ventur",
            "Image": "assets/img/icons/company-icon-05.svg",
            "ContractValue": "$3,15,145",
            "ContractType": "Voidable Contracts",
            "StartDate": "15 Oct 2024",
            "EndDate": "15 Jan 2024",
        },
        {
            "ContractID": "#1493019",
            "Subject": "Web Design",
            "Customer": "Summit Peak",
            "Image": "assets/img/icons/company-icon-04.svg",
            "ContractValue": "$6,154",
            "ContractType": "Unilateral Contracts",
            "StartDate": "08 Aug 2024",
            "EndDate": "15 Dec 2023",
        },
        {
            "ContractID": "#1493018",
            "Subject": "Logo",
            "Customer": "Silver Hawk",
            "Image": "assets/img/icons/company-icon-03.svg",
            "ContractValue": "$1,457",
            "ContractType": "Unconscionable",
            "StartDate": "25 Jan 2025",
            "EndDate": "15 Nov 2023",
        },
        {
            "ContractID": "#1493017",
            "Subject": "Branding",
            "Customer": "BlueSky Industries",
            "Image": "assets/img/icons/company-icon-02.svg",
            "ContractValue": "$2,01,464",
            "ContractType": "Express Contracts",
            "StartDate": "12 Aug 2024",
            "EndDate": "15 Sep 2023",
        },
        {
            "ContractID": "#1493018",
            "Subject": "Development",
            "Customer": "Golden Gate Ltd",
            "Image": "assets/img/icons/company-icon-09.svg",
            "ContractValue": "$1,10,145",
            "ContractType": "Contracts under Seal",
            "StartDate": "07 Dec 2024",
            "EndDate": "15 Aug 2023",
        },
    ]
    return render(request, 'pages/crm/contracts.html', { 'contracts' : contracts })

def contracts_grid(request):
    contracts_grid = [
        {
            "Title": "SEO Contracts",
            "Content": "Category : Contracts under Seal",
            "Image": "assets/img/icons/company-icon-01.svg",
            "Company": "NovaWave LLC"
        },
        {
            "Title": "Redwood Inc",
            "Content": "Category : Contracts under Seal",
            "Image": "assets/img/icons/company-icon-02.svg",
            "Company": "NovaWave LLC"
        },
        {
            "Title": "HarborView",
            "Content": "Implied Contracts",
            "Image": "assets/img/icons/company-icon-03.svg",
            "Company": "Development"
        },
        {
            "Title": "Executory Contracts",
            "Content": "Category : under Seal",
            "Image": "assets/img/icons/company-icon-05.svg",
            "Company": "Unconscionable"
        },
        {
            "Title": "SEO Contracts",
            "Content": "Category : Contracts under Seal",
            "Image": "assets/img/icons/company-icon-01.svg",
            "Company": "NovaWave LLC"
        },
        {
            "Title": "Redwood Inc",
            "Content": "Category : Contracts under Seal",
            "Image": "assets/img/icons/company-icon-02.svg",
            "Company": "Unconscionable"
        },
        {
            "Title": "HarborView",
            "Content": "Implied Contracts",
            "Image": "assets/img/icons/company-icon-03.svg",
            "Company": "Development"
        },
        {
            "Title": "Executory Contracts",
            "Content": "Category : under Seal",
            "Image": "assets/img/icons/company-icon-05.svg",
            "Company": "NovaWave LLC"
        }
    ]
    return render(request, 'pages/crm/contracts-grid.html', { 'contracts_grid' : contracts_grid })

def estimations(request):
    estimations = [
        {
            "ClientImage": "assets/img/icons/company-icon-01.svg",
            "ProjectImage": "assets/img/priority/truellysel.svg",
            "AvatarImage": "assets/img/profiles/avatar-19.jpg",
            "EstimationsID": "#274738",
            "Client": "NovaWave LLC",
            "Amount": "$2,15,000",
            "Project": "Truelysell",
            "Date": "15 Oct 2023",
            "ExpiryDate": "25 Sep 2023",
            "EstimationBy": "Darlee Robertson",
            "Role": "Facility Manager",
            "Status": "Sent"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-02.svg",
            "ProjectImage": "assets/img/priority/dreamchat.svg",
            "AvatarImage": "assets/img/profiles/avatar-20.jpg",
            "EstimationsID": "#274737",
            "Client": "BlueSky Industries",
            "Amount": "$1,45,000",
            "Project": "Dreamschat",
            "Date": "19 Oct 2023",
            "ExpiryDate": "10 Sep 2028",
            "EstimationBy": "Sharon Roy",
            "Role": "Installer",
            "Status": "Accepted"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-03.svg",
            "ProjectImage": "assets/img/priority/truellysell.svg",
            "AvatarImage": "assets/img/profiles/avatar-21.jpg",
            "EstimationsID": "#274736",
            "Client": "Silver Hawk",
            "Amount": "$2,15,000",
            "Project": "Truelysell",
            "Date": "24 Oct 2023",
            "ExpiryDate": "20 Oct 2026",
            "EstimationBy": "Vaughan",
            "Role": "Senior Manager",
            "Status": "Draft"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-04.svg",
            "ProjectImage": "assets/img/priority/servbook.svg",
            "AvatarImage": "assets/img/profiles/avatar-23.jpg",
            "EstimationsID": "#274735",
            "Client": "Summit Peak",
            "Amount": "$4,80,380",
            "Project": "Servbook",
            "Date": "10 Nov 2023",
            "ExpiryDate": "07 Oct 2028",
            "EstimationBy": "Jessica",
            "Role": "Test Engineer",
            "Status": "Accepted"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-05.svg",
            "ProjectImage": "assets/img/priority/dream-pos.svg",
            "AvatarImage": "assets/img/profiles/avatar-16.jpg",
            "EstimationsID": "#274734",
            "Client": "RiverStone Ventur",
            "Amount": "$2,12,000",
            "Project": "DreamPOS",
            "Date": "18 Nov 2023",
            "ExpiryDate": "10 Oct 2026",
            "EstimationBy": "Carol Thomas",
            "Role": "UI /UX Designer",
            "Status": "Declined"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-07.svg",
            "ProjectImage": "assets/img/priority/project-01.svg",
            "AvatarImage": "assets/img/profiles/avatar-22.jpg",
            "EstimationsID": "#274733",
            "Client": "CoastalStar Co.",
            "Amount": "$3,50,000",
            "Project": "Kofejob",
            "Date": "20 Nov 2023",
            "ExpiryDate": "18 Oct 2027",
            "EstimationBy": "Dawn Mercha",
            "Role": "Technician",
            "Status": "Draft"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-08.svg",
            "ProjectImage": "assets/img/priority/project-02.svg",
            "AvatarImage": "assets/img/profiles/avatar-24.jpg",
            "EstimationsID": "#274732",
            "Client": "HarborView",
            "Amount": "$1,23,000",
            "Project": "Doccure",
            "Date": "07 Dec 2023",
            "ExpiryDate": "05 Nov 2026",
            "EstimationBy": "Rachel Hampton",
            "Role": "Software Developer",
            "Status": "Sent",
        },
        {
            "ClientImage": "assets/img/icons/company-icon-09.svg",
            "ProjectImage": "assets/img/priority/best.svg",
            "AvatarImage": "assets/img/profiles/avatar-24.jpg",
            "EstimationsID": "#274731",
            "Client": "Golden Gate Ltd",
            "Amount": "$3,12,50",
            "Project": "Best@laundry",
            "Date": "14 Dec 2023",
            "ExpiryDate": "11 Nov 2028",
            "EstimationBy": "Jonelle Curtiss",
            "Role": "Supervisor",
            "Status": "Accepted"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-10.svg",
            "ProjectImage": "assets/img/priority/project-01.svg",
            "AvatarImage": "assets/img/profiles/avatar-26.jpg",
            "EstimationsID": "#274730",
            "Client": "Golden Gate Ltd",
            "Amount": "$4,18,000",
            "Project": "Dreamsports",
            "Date": "22 Dec 2023",
            "ExpiryDate": "20 Nov 2027",
            "EstimationBy": "Jonathan",
            "Role": "Team Lead Dev",
            "Status": "Declined"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-01.svg",
            "ProjectImage": "assets/img/priority/truellysel.svg",
            "AvatarImage": "assets/img/profiles/avatar-01.jpg",
            "EstimationsID": "#274729",
            "Client": "NovaWave LLC",
            "Amount": "$4,80,380",
            "Project": "Truelysell",
            "Date": "28 Dec 2023",
            "ExpiryDate": "25 Nov 2026",
            "EstimationBy": "Brook",
            "Role": "Team Lead Dev",
            "Status": "Accepted"
        }
    ]
    return render(request, 'pages/crm/estimations.html', { 'estimations' : estimations })

def estimations_kanban(request):
    return render(request, 'pages/crm/estimations-kanban.html')

def invoices(request):
    invoices = [
        {
            "ClientImage": "assets/img/icons/company-icon-01.svg",
            "ProjectImage": "assets/img/priority/truellysel.svg",
            "InvoiceID": "#1254058",
            "Client": "NovaWave LLC",
            "Project": "Truelysell",
            "DueDate": "21 May 2024",
            "Amount": "$2,15,000",
            "PaidAmount": "$2,15,000",
            "BalanceAmount": "$0",
            "Status": "Partially Paid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-10.svg",
            "ProjectImage": "assets/img/priority/project-01.svg",
            "InvoiceID": "#1254057",
            "Client": "BlueSky Industries",
            "Project": "Dreamschat",
            "DueDate": "19 Oct 2023",
            "Amount": "$1,45,000",
            "PaidAmount": "$1,45,000",
            "BalanceAmount": "$0",
            "Status": "Paid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-08.svg",
            "ProjectImage": "assets/img/priority/best.svg",
            "InvoiceID": "#1254056",
            "Client": "Silver Hawk",
            "Project": "Truelysell",
            "DueDate": "24 Oct 2023",
            "Amount": "$2,15,000",
            "PaidAmount": "$1,00,000",
            "BalanceAmount": "$1,15,000",
            "Status": "Partially Paid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-07.svg",
            "ProjectImage": "assets/img/priority/project-02.svg",
            "InvoiceID": "#1254055",
            "Client": "Summit Peak",
            "Project": "Servbook",
            "DueDate": "10 Nov 2023",
            "Amount": "$4,80,380",
            "PaidAmount": "$4,80,380",
            "BalanceAmount": "$0",
            "Status": "Paid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-05.svg",
            "ProjectImage": "assets/img/priority/project-01.svg",
            "InvoiceID": "#1254054",
            "Client": "RiverStone Ventur",
            "Project": "DreamPOS",
            "DueDate": "18 Nov 2023",
            "Amount": "$2,12,000",
            "PaidAmount": "$0",
            "BalanceAmount": "$2,12,000",
            "Status": "Unpaid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-04.svg",
            "ProjectImage": "assets/img/priority/dream-pos.svg",
            "InvoiceID": "#1254053",
            "Client": "CoastalStar Co.",
            "Project": "Kofejob",
            "DueDate": "20 Nov 2023",
            "Amount": "$3,50,000",
            "PaidAmount": "$1,50,000",
            "BalanceAmount": "$2,00,000",
            "Status": "Partially Paid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-03.svg",
            "ProjectImage": "assets/img/priority/servbook.svg",
            "InvoiceID": "#1254052",
            "Client": "HarborView",
            "Project": "Doccure",
            "DueDate": "07 Dec 2023",
            "Amount": "$1,23,000",
            "PaidAmount": "$1,23,000",
            "BalanceAmount": "$1,23,000",
            "Status": "Overdue"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-02.svg",
            "ProjectImage": "assets/img/priority/truellysell.svg",
            "InvoiceID": "#1254051",
            "Client": "Golden Gate Ltd",
            "Project": "Best@laundry",
            "DueDate": "14 Dec 2023",
            "Amount": "$3,12,500",
            "PaidAmount": "$3,12,500",
            "BalanceAmount": "$0",
            "Status": "Paid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-09.svg",
            "ProjectImage": "assets/img/priority/dreamchat.svg",
            "InvoiceID": "#1254050",
            "Client": "Redwood Inc",
            "Project": "Dreamsports",
            "DueDate": "22 Dec 2023",
            "Amount": "$4,18,000",
            "PaidAmount": "$0",
            "BalanceAmount": "$4,18,000",
            "Status": "Unpaid"
        },
        {
            "ClientImage": "assets/img/icons/company-icon-01.svg",
            "ProjectImage": "assets/img/priority/dreamchat.svg",
            "InvoiceID": "#1254049",
            "Client": "NovaWave LLC",
            "Project": "Truelysell",
            "DueDate": "28 Dec 2023",
            "Amount": "$5,00,000",
            "PaidAmount": "$5,00,000",
            "BalanceAmount": "$0",
            "Status": "Paid"
        },
    ]
    return render(request, 'pages/crm/invoices.html', { 'invoices' : invoices })

def invoice_grid(request):
    invoice_grid = [
        {
            "Badge": "Partially Paid",
            "Image": "assets/img/priority/truellysel.svg",
            "Title": "Truelysell",
            "Company": "assets/img/icons/company-icon-01.svg",
            "Client_name": "NovaWave LLC"
        },
        {
            "Badge": "Paid",
            "Image": "assets/img/priority/dreamchat.svg",
            "Title": "Dreamschat",
            "Company": "assets/img/icons/company-icon-02.svg",
            "Client_name": "Silver Hawk"
        },
        {
            "Badge": "Partially Paid",
            "Image": "assets/img/priority/truellysell.svg",
            "Title": "Truelysell",
            "Company": "assets/img/icons/company-icon-03.svg",
            "Client_name": "Summit Peak"
        },
        {
            "Badge": "Paid",
            "Image": "assets/img/priority/servbook.svg",
            "Title": "Servbook",
            "Company": "assets/img/icons/company-icon-04.svg",
            "Client_name": "RiverStone Ventur"
        },
        {
            "Badge": "Unpaid",
            "Image": "assets/img/priority/dream-pos.svg",
            "Title": "DreamPOS",
            "Company": "assets/img/icons/company-icon-05.svg",
            "Client_name": "Harbor View"      
        },
        {
            "Badge": "Partially Paid",
            "Image": "assets/img/priority/project-01.svg",
            "Title": "Kofejob",
            "Company": "assets/img/icons/company-icon-06.svg",
            "Client_name": "Harbor View"
        },
        {
            "Badge": "Overdue",
            "Image": "assets/img/priority/project-02.svg",
            "Title": "Doccure",
            "Company": "assets/img/icons/company-icon-07.svg",
            "Client_name": "Summit Peak"
        },
        {
            "Badge": "Paid",
            "Image": "assets/img/priority/best.svg",
            "Title": "Best@laundry",
            "Company": "assets/img/icons/company-icon-08.svg",
            "Client_name": "Best@laundry"
        }
    ]
    return render(request, 'pages/crm/invoice-grid.html', { 'invoice_grid' : invoice_grid })

def payments(request):
    payments = [
        {
            "InvoiceId": "#1254058",
            "Customer": "NovaWave LLC",
            "ClientImg": "assets/img/icons/company-icon-01.svg",
            "Amount": "$2500",
            "DueDate": "15 Oct 2023",
            "PaymentMethod": "Cash",
            "TransactionId": "TXNID1234567890",
        },
        {
            "InvoiceId": "#1254057",
            "Customer": "BlueSky Industries",
            "ClientImg": "assets/img/icons/company-icon-02.svg",
            "Amount": "$1450",
            "DueDate": "19 Oct 2023",
            "PaymentMethod": "Credit",
            "TransactionId": "TXNID9876543210",
        },
        {
            "InvoiceId": "#1254056",
            "Customer": "Silver Hawk",
            "ClientImg": "assets/img/icons/company-icon-03.svg",
            "Amount": "$2100",
            "DueDate": "24 Oct 2023",
            "PaymentMethod": "Cash",
            "TransactionId": "TXNID2468135790",
        },
        {
            "InvoiceId": "#1254055",
            "Customer": "Summit Peak",
            "ClientImg": "assets/img/icons/company-icon-04.svg",
            "Amount": "$4000",
            "DueDate": "10 Nov 2023",
            "PaymentMethod": "Credit",
            "TransactionId": "TXNID1357924680",
        },
        {
            "InvoiceId": "#1254054",
            "Customer": "RiverStone Ventur",
            "ClientImg": "assets/img/icons/company-icon-05.svg",
            "Amount": "$2120",
            "DueDate": "18 Nov 2023",
            "PaymentMethod": "Cash",
            "TransactionId": "TXNID0123456789",
        },
        {
            "InvoiceId": "#1254053",
            "Customer": "CoastalStar Co.",
            "ClientImg": "assets/img/icons/company-icon-04.svg",
            "Amount": "$3500",
            "DueDate": "20 Nov 2023",
            "PaymentMethod": "Credit",
            "TransactionId": "TXNIDABCDE12345",
        },
        {
            "InvoiceId": "#1254052",
            "Customer": "HarborView",
            "ClientImg": "assets/img/icons/company-icon-03.svg",
            "Amount": "$1230",
            "DueDate": "07 Dec 2023",
            "PaymentMethod": "Cash",
            "TransactionId": "TXNID54321XYZ789",
        },
        {
            "InvoiceId": "#1254051",
            "Customer": "Golden Gate Ltd",
            "ClientImg": "assets/img/icons/company-icon-02.svg",
            "Amount": "$3125",
            "DueDate": "14 Dec 2023",
            "PaymentMethod": "Credit",
            "TransactionId": "TXNIDQWERTY0987",
        },
        {
            "InvoiceId": "#1254050",
            "Customer": "Redwood Inc",
            "ClientImg": "assets/img/icons/company-icon-10.svg",
            "Amount": "$4180",
            "DueDate": "22 Dec 2023",
            "PaymentMethod": "Cash",
            "TransactionId": "TXNID98765ASDF43",
        },
        {
            "InvoiceId": "#1254049",
            "Customer": "NovaWave LLC",
            "ClientImg": "assets/img/icons/company-icon-05.svg",
            "Amount": "$5000",
            "DueDate": "28 Dec 2023",
            "PaymentMethod": "Cash",
            "TransactionId": "TXNID1A2B3C4D5E6",
        }
    ]
    return render(request,  'pages/crm/payments.html', { 'payments' : payments })

def analytics(request):
    analytics = [
        {
            "id" : 1,
            "lead_name" : "NovaWaveLLC",
            "lead_img" : "company-icon-01.svg",
            "phone" : "+1 124547845",
            "email" : "caroo3@example.com",
            "date" : "25 Sep 2023, 12:12 pm"
        },
        {
            "id" : 2,
            "lead_name" : "SilverHawk",
            "lead_img" : "company-icon-03.svg",
            "phone" : "+1 478845447",
            "email" : "dercha@example.com",
            "date" : "27 Sep 2023, 11:23 pm"
        },
        {
            "id" : 3,
            "lead_name" : "SummitPeak",
            "lead_img" : "company-icon-04.svg",
            "phone" : "+1 215544845",
            "email" : "rael@example.com",
            "date" : "04 Oct 2023, 04:12 pm"
        },
        {
            "id" : 4,
            "lead_name" : "RiverStone Ventur",
            "lead_img" : "company-icon-05.svg",
            "phone" : "+1 124547845",
            "email" : "joe@example.com",
            "date" : "17 Oct 2023, 11:34 am"
        },
        {
            "id" : 5,
            "lead_name" : "CoastalStar Co.",
            "lead_img" : "company-icon-07.svg",
            "phone" : "+1 124547845",
            "email" : "joe@example.com",
            "date" : "17 Oct 2023, 11:34 am"
        },
        {
            "id" : 6,
            "lead_name" : "Redwood Inc",
            "lead_img" : "company-icon-10.svg",
            "phone" : "+1 466701256",
            "email" : "sharon@example.com",
            "date" : "15 Nov 2023, 07:26 pm"
        }
    ],
    return render(request, 'pages/crm/analytics.html', { 'analytics' : analytics })

def activities(request):
    activities = [
        {
            "title": "We scheduled a meeting for next week",
            "due_date": "25 Sep 2023, 12:12 pm",
            "owner": "Hendry",
            "created_date": "22 Sep 2023, 10:14 am",
            "status": "Meeting"
        },
        {
            "title": "Had conversation with Fred regarding task",
            "due_date": "29 Sep 2023, 04:12 pm",
            "owner": "Monty Beer",
            "created_date": "27 Sep 2023, 03:26 pm",
            "status": "Calls"
        },
        {
            "title": "Analysing latest time estimation for new project",
            "due_date": "11 Oct 2023, 05:00 pm",
            "owner": "Bradtke",
            "created_date": "03 Oct 2023, 03:53 pm",
            "status": "Email"
        },
        {
            "title": "Store and manage contact data",
            "due_date": "19 Oct 2023, 02:35 pm",
            "owner": "Swaniawski",
            "created_date": "14 Oct 2023, 01:25 pm",
            "status": "Tasks"
        },
        {
            "title": "Will have a meeting before project start",
            "due_date": "27 Oct 2023, 12:30 pm",
            "owner": "Sally",
            "created_date": "21 Oct 2023, 03:00 pm",
            "status": "Meeting"
        },
        {
            "title": "Call John and discuss about project",
            "due_date": "12 Nov 2023, 10:20 pm",
            "owner": "Itzel",
            "created_date": "02 Nov 2023, 05:35 pm",
            "status": "Calls"
        },
        {
            "title": "Built landing pages",
            "due_date": "25 Nov 2023, 01:40 pm",
            "owner": "Danny",
            "created_date": "20 Nov 2023, 08:20 am",
            "status": "Tasks"
        },
        {
            "title": "Regarding latest updates in project",
            "due_date": "30 Nov 2023, 09:20 pm",
            "owner": " Lynch",
            "created_date": "25 Nov 2023, 07:20 pm",
            "status": "Email"
        },
        {
            "title": "Discussed budget proposal with Edwin",
            "due_date": "08 Dec 2023, 04:35 pm",
            "owner": "Merwin",
            "created_date": "01 Dec 2023, 10:45 am",
            "status": "Calls"
        },
        {
            "title": "Attach final proposal for upcoming project",
            "due_date": "19 Dec 2023, 02:20 pm",
            "owner": " Andrew",
            "created_date": "10 Dec 2023, 06:30 pm",
            "status": "Email"
        },
        {
            "title": "Discussed budget proposal with Edwin",
            "due_date": "26 Dec 2023, 08:30 am",
            "owner": "Clausen",
            "created_date": "18 Dec 2023, 05:00 pm",
            "status": "Calls"
        }
    ]
    return render(request, 'pages/crm/activities.html', { 'activities' : activities })

def activity_calls(request):
    activity_calls = [
        {
            "title": "Had conversation with Fred regarding task",
            "due_date": "29 Sep 2023, 04:12 pm",
            "owner": "Monty Beer",
            "created_date": "27 Sep 2023, 03:26 pm",
            "status": "Calls"
        },
        {
            "title": "Call John and discuss about project",
            "due_date": "12 Nov 2023, 10:20 pm",
            "owner": "Itzel",
            "created_date": "02 Nov 2023, 05:35 pm",
            "status": "Calls"
        },
        {
            "title": "Discussed budget proposal with Edwin",
            "due_date": "08 Dec 2023, 04:35 pm",
            "owner": "Merwin",
            "created_date": "01 Dec 2023, 10:45 am",
            "status": "Calls"
        },
        {
            "title": "Discussed budget proposal with Edwin",
            "due_date": "26 Dec 2023, 08:30 am",
            "owner": "Clausen",
            "created_date": "18 Dec 2023, 05:00 pm",
            "status": "Calls"
        }
    ]
    return render(request, 'pages/crm/activity-calls.html', { 'activity_calls' : activity_calls })

def activity_mail(request):
    activity_mail = [
        {
            "title": "Analysing latest time estimation for new project",
            "due_date": "11 Oct 2023, 05:00 pm",
            "owner": "Bradtke",
            "created_date": "03 Oct 2023, 03:53 pm",
            "status": "Email"
        },
        {
            "title": "Regarding latest updates in project",
            "due_date": "30 Nov 2023, 09:20 pm",
            "owner": " Lynch",
            "created_date": "25 Nov 2023, 07:20 pm",
            "status": "Email"
        },
        {
            "title": "Attach final proposal for upcoming project",
            "due_date": "19 Dec 2023, 02:20 pm",
            "owner": " Andrew",
            "created_date": "10 Dec 2023, 06:30 pm",
            "status": "Email"
        }
    ]
    return render(request, 'pages/crm/activity-mail.html', {'activity_mail' : activity_mail})

def activity_task(request):
    activity_task = [
        {
            "Title": "Store and manage contact data",
            "DueDate": "19 Oct 2023, 02:35 pm",
            "Owner": "Swaniawski",
            "CreatedDate": "14 Oct 2023, 01:25 pm",
        },
        {
            "Title": "Built landing pages",
            "DueDate": "25 Nov 2023, 01:40 pm",
            "Owner": "Danny",
            "CreatedDate": "20 Nov 2023, 08:20 am",
        },
    ]
    return render(request, 'pages/crm/activity-task.html',{'activity_task' : activity_task})

def activity_meeting(request):
    activity_meeting = [
         {
            "Title": "We scheduled a meeting for next week",
            "DueDate": "25 Sep 2023, 12:12 pm",
            "Owner": "Hendry",
            "CreatedDate": "22 Sep 2023, 10:14 am",
        },
        {
            "Title": "Will have a meeting before project start",
            "DueDate": "27 Oct 2023, 12:30 pm",
            "Owner": "Sally",
            "CreatedDate": "21 Oct 2023, 03:00 pm",
        },
    ]
    return render(request, 'pages/crm/activity-meeting.html',{'activity_meeting' : activity_meeting})

# Settings

def profile(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    return render(request, 'pages/settings/general-settings/profile.html', {'user': request.user})

def security(request):
    return render(request, 'pages/settings/general-settings/security.html')

def notifications(request):
    return render(request, 'pages/settings/general-settings/notifications.html')

def connected_apps(request):
    return render(request, 'pages/settings/general-settings/connected-apps.html')

def company_settings(request):
    return render(request, 'pages/settings/website-settings/company-settings.html')

def localization(request):
    return render(request, 'pages/settings/website-settings/localization.html')

def prefixes(request):
    return render(request, 'pages/settings/website-settings/prefixes.html')

def preference(request):
    return render(request, 'pages/settings/website-settings/preference.html')

def appearance(request):
    return render(request, 'pages/settings/website-settings/appearance.html')
 
def language(request):
    language = [
        {
            "Language": "English",
            "Image": "assets/img/icons/flag-01.svg",
            "Code": "en",
            "Total": "3481",
            "Done": "2861",
            "For": "English",
            "Id": "English",
            "Progress": "80%",
        },
        {
            "Language": "Arabic",
            "Image": "assets/img/icons/flag-02.svg",
            "Code": "ar",
            "Total": "4815",
            "Done": "4815",
            "For": "Arabic",
            "Id": "Arabic",
            "Progress": "100%",
        },
        {
            "Language": "Chinese",
            "Image": "assets/img/icons/flag-01.svg",
            "Code": "zh",
            "Total": "2590",
            "Done": "250",
            "For": "Chinese",
            "Id": "Chinese",
            "Progress": "5%",
        },
        {
            "Language": "Hindi",
            "Image": "assets/img/icons/flag-01.svg",
            "Code": "hi",
            "Total": "1892",
            "Done": "387",
            "For": "Hindi",
            "Id": "Hindi",
            "Progress": "40%",
        },
    ]
    return render(request, 'pages/settings/website-settings/language.html', {"language": language})

def language_web(request):
    language_web = [
        {
            "Medium": "Web",
            "File": "Inventory",
            "Total": "3481",
            "Done": "2861",
            "Progress": "80%",
        },
        {
            "Medium": "Web",
            "File": "Expense",
            "Total": "4815",
            "Done": "4815",
            "Progress": "100%",
        },
        {
            "Medium": "Web",
            "File": "Product",
            "Total": "2590",
            "Done": "250",
            "Progress": "5%",
        },
        {
            "Medium": "Web",
            "File": "Settings",
            "Total": "1892",
            "Done": "387",
            "Progress": "40%",
        },
    ]
    return render(request, 'pages/settings/website-settings/language-web.html', {"language_web": language_web})

def invoice_settings(request):
    return render(request, 'pages/settings/app-settings/invoice-settings.html')

def printers(request):
    return render(request, 'pages/settings/app-settings/printers.html')

def custom_fields(request):
    return render(request, 'pages/settings/app-settings/custom-fields.html')

def email_settings(request):
    return render(request, 'pages/settings/system-settings/email-settings.html')

def sms_gateways(request):
    return render(request, 'pages/settings/system-settings/sms-gateways.html')

def gdpr_cookies(request):
    return render(request, 'pages/settings/system-settings/gdpr-cookies.html')

def payment_gateways(request):
    return render(request, 'pages/settings/financial-settings/payment-gateways.html')

def bank_accounts(request):
    return render(request, 'pages/settings/financial-settings/bank-accounts.html')

def tax_rates(request):
    return render(request, 'pages/settings/financial-settings/tax-rates.html')

def currencies(request):
    return render(request, 'pages/settings/financial-settings/currencies.html')

def storage(request):
    return render(request, 'pages/settings/others-settings/storage.html')

def ban_ip_address(request):
    return render(request, 'pages/settings/others-settings/ban-ip-address.html')

def chat(request):
    return render(request, 'pages/application/chat.html')

def invoices(request):
    return render(request, 'pages/application/invoices.html')

def invoice_details(request):
    return render(request, 'pages/application/invoice-details.html')

def kanban_view(request):
    return render(request, 'pages/application/kanban-view.html')

def social_feed(request):
    return render(request, 'pages/application/social-feed.html')
 
def video_call(request):
    return render(request, 'pages/application/call/video-call.html')
 
def audio_call(request):
    return render(request, 'pages/application/call/audio-call.html')

# Super Admin
 
def layout_mini(request):
    return render(request, 'pages/layouts/layout-mini.html')
 
def layout_horizontal_single(request):
    return render(request, 'pages/layouts/layout-horizontal-single.html')
 
def layout_without_header(request):
    return render(request, 'pages/layouts/layout-without-header.html')
 
def layout_rtl(request):
    return render(request, 'pages/layouts/layout-rtl.html')
 
def layout_detached(request):
    return render(request, 'pages/layouts/layout-detached.html')
 
def layout_dark(request):
    return render(request, 'pages/layouts/layout-dark.html')

# Super Admin
 
def dashboard(request):
    return render(request, 'pages/superadmin/dashboard.html')
 
def domain(request):
    return render(request, 'pages/superadmin/domain.html')
 
def company(request):
    return render(request, 'pages/superadmin/company.html')
 
def packages(request):
    return render(request, 'pages/superadmin/packages.html')
 
def packages_grid(request):
    return render(request, 'pages/superadmin/packages-grid.html')
 
def purchase_transaction(request):
    return render(request, 'pages/superadmin/purchase-transaction.html')
 
def subscription(request):
    return render(request, 'pages/superadmin/subscription.html')

# Support

def tickets(request):
    tickets = [
        {
            "TicketId": "#4987",
            "Subject": "Support for theme",
            "AssignedName": "Richard",
            "AssignedImage": "assets/img/profiles/avatar-02.jpg",
            "AssignedDate": "22 Sep 2023",
            "Created": "25 Sep 2023, 12:12 pm",
            "DueDate": "25 Dec 2023",
            "CustomerName": "Darlee Robertson",
            "CustomerImage": "assets/img/profiles/avatar-19.jpg",
            "CustomerNo": "Facility Manager",
            "Priority" : "Medium",
            "Status" : "Resolved",
            "ReplyDate": "27 Sep 2023",
        },
        {
            "TicketId": "#4988",
            "Subject": "verify your email",
            "AssignedName": "Elizabeth",
            "AssignedImage": "assets/img/profiles/avatar-01.jpg",
            "AssignedDate": "23 Sep 2023",
            "Created": "26 Sep 2023, 12:12 pm",
            "DueDate": "30 Dec 2023",
            "CustomerName": "Sharon Roy",
            "CustomerImage": "assets/img/profiles/avatar-20.jpg",
            "CustomerNo": "Installer",
            "Priority" : "Low",
            "Status" : "Closed",
            "ReplyDate": "30 Sep 2023",
        },
        {
            "TicketId": "#4989",
            "Subject": "Calling for help",
            "AssignedName": "Michel",
            "AssignedImage": "assets/img/profiles/avatar-04.jpg",
            "AssignedDate": "24 Sep 2023",
            "Created": "27 Sep 2023, 12:12 pm",
            "DueDate": "25 Jan 2024",
            "CustomerName": "Vaughan",
            "CustomerImage": "assets/img/profiles/avatar-21.jpg",
            "CustomerNo": "Senior  Manager",
            "Priority" : "High",
            "Status" : "Pending",
            "ReplyDate": "01 Oct 2023",
        },
        {
            "TicketId": "#4990",
            "Subject": "Management",
            "AssignedName": "Esther",
            "AssignedImage": "assets/img/profiles/avatar-03.jpg",
            "AssignedDate": "30 Sep 2023",
            "Created": "05 Oct 2023, 11:10 pm",
            "DueDate": "31 Jan 2023",
            "CustomerName": "Jessica",
            "CustomerImage": "assets/img/profiles/avatar-23.jpg",
            "CustomerNo": "Test Engineer",
            "Priority" : "Medium",
            "Status" : "Resolved",
            "ReplyDate": "10 Oct 2023",
        },
        {
            "TicketId": "#4991",
            "Subject": "Calling for help",
            "AssignedName": "Wilson",
            "AssignedImage": "assets/img/profiles/avatar-05.jpg",
            "AssignedDate": "22 Sep 2023",
            "Created": "25 Sep 2023, 12:12 pm",
            "DueDate": "25 Dec 2023",
            "CustomerName": "Carol Thomas",
            "CustomerImage": "assets/img/profiles/avatar-16.jpg",
            "CustomerNo": "UI /UX Designer",
            "Priority" : "Low",
            "Status" : "Open",
            "ReplyDate": "27 Sep 2023",
        },
        {
            "TicketId": "#4992",
            "Subject": "Support for theme",
            "AssignedName": "Walter",
            "AssignedImage": "assets/img/profiles/avatar-06.jpg",
            "AssignedDate": "30 Sep 2023",
            "Created": "05 Oct 2023, 12:12 pm",
            "DueDate": "25 Dec 2023",
            "CustomerName": "Dawn Mercha",
            "CustomerImage": "assets/img/profiles/avatar-22.jpg",
            "CustomerNo": "Technician",
            "Priority" : "High",
            "Status" : "Closed",
            "ReplyDate": "07 Oct 2023",
        },
    ]
    return render(request, 'pages/support/tickets.html', {"tickets": tickets})

def contact_messages(request):
    contact_messages = [
        {
			"CustomerName" : "Darlee Robertson",
			"CustomerImage" : "assets/img/profiles/avatar-19.jpg",
			"CustomerNo" : "Facility Manager",
			"Phone" : "1234567890",
			"Email" : "robertson@example.com",
			"Message" : "Duis aute irure dolor in reprehenderit",
			"Created" : "25 Sep 2023, 12:12 pm",
		},
		{
			"CustomerName" : "Sharon Roy",
			"CustomerImage" : "assets/img/profiles/avatar-20.jpg",
			"CustomerNo" : "Installer",
			"Phone" : "+1 989757485",
			"Email" : "sharon@example.com",
			"Message" : "Excepteur sint occaecat cupidatat",
			"Created" : "27 Sep 2023, 07:40 am",
		},
		{
			"CustomerName" : "Vaughan",
			"CustomerImage" : "assets/img/profiles/avatar-21.jpg",
			"CustomerNo" : "Senior  Manager",
			"Phone" : "+1 546555455",
			"Email" : "vaughan12@example.com",
			"Message" : "Lorem ipsum dolor sit consectetur",
			"Created" : "29 Sep 2023, 08:20 am",
		},
		{
			"CustomerName" : "Jessica",
			"CustomerImage" : "assets/img/profiles/avatar-23.jpg",
			"CustomerNo" : "Test Engineer",
			"Phone" : "+1 454478787",
			"Email" : "jessica13@example.com",
			"Message" : "Nemo enim ipsam voluptatem quia",
			"Created" : "25 Sep 2023, 12:12 pm",
		},
		{
			"CustomerName" : "Carol Thomas",
			"CustomerImage" : "assets/img/profiles/avatar-16.jpg",
			"CustomerNo" : "UI /UX Designer",
			"Phone" : "+1 124547845",
			"Email" : "caroltho3@example.com",
			"Message" : "Sed ut perspiciatis unde omnis iste",
			"Created" : "02 Oct 2023, 10:10 am",
		},
		{
			"CustomerName" : "Dawn Mercha",
			"CustomerImage" : "assets/img/profiles/avatar-22.jpg",
			"CustomerNo" : "Technician",
			"Phone" : "+1 478845447",
			"Email" : "dawnmercha@example.com",
			"Message" : "Ut enim ad minim veniam, quis",
			"Created" : "17 Oct 2023, 04:25 pm",
		},
		{
			"CustomerName" : "Rachel Hampton",
			"CustomerImage" : "assets/img/profiles/avatar-24.jpg",
			"CustomerNo" : "Software Developer",
			"Phone" : "+1 215544845",
			"Email" : "rachel@example.com",
			"Message" : "Duis aute irure dolor in reprehenderit",
			"Created" : "28 Oct 2023, 07:16 am",
		},
		{
			"CustomerName" : "Jonelle Curtiss",
			"CustomerImage" : "assets/img/profiles/avatar-25.jpg",
			"CustomerNo" : "Supervisor",
			"Phone" : "+1 121145471",
			"Email" : "jonelle@example.com",
			"Message" : "Ut enim ad minim veniam, quis",
			"Created" : "08 Nov 2023, 06:10 am",
		},
		{
			"CustomerName" : "Jonathan",
			"CustomerImage" : "assets/img/profiles/avatar-26.jpg",
			"CustomerNo" : "Team Lead Dev",
			"Phone" : "+1 321454789",
			"Email" : "jonathan@example.com",
			"Message" : "Excepteur sint occaecat cupidatat",
			"Created" : "15 Nov 2023, 11:50 am",
		},
		{
			"CustomerName" : "Brook",
			"CustomerImage" : "assets/img/profiles/avatar-01.jpg",
			"CustomerNo" : "Team Lead Dev ",
			"Phone" : "+1 278907145",
			"Email" : "brook@example.com",
			"Message" : "Ut enim ad minim veniam, quis",
			"Created" : "25 Nov 2023, 06:34 pm",
		}
    ]
    return render(request, 'pages/support/contact-messages.html', {'contact_messages' : contact_messages})

# CRM Settings

def sources(request):
    sources = [
        {
            "Title": "Phone Calls",
            "CreatedDate": "25 Sep 2023, 01:22 pm",
            "Status": "Active"
        },
        {
            "Title": "Social Media",
            "CreatedDate": "29 Sep 2023, 04:15 pm",
            "Status": "Active"
        },
        {
            "Title": "Referral Sites",
            "CreatedDate": "04 Oct 2023, 10:18 am",
            "Status": "Active"
        },
        {
            "Title": "Web Analytics",
            "CreatedDate": "17 Oct 2023, 03:31 pm",
            "Status": "Inactive"
        },
        {
            "Title": "Previous Purchases",
            "CreatedDate": "24 Oct 2023, 09:14 pm",
            "Status": "Active"
        },
        {
            "Title": "Lead & Opportunity",
            "CreatedDate": "08 Nov 2023, 09:56 am",
            "Status": "Active"
        },
        {
            "Title": "Image-based Features",
            "CreatedDate": "14 Nov 2023, 04:19 pm",
            "Status": "Active"
        },
        {
            "Title": "Bots",
            "CreatedDate": "23 Nov 2023, 11:14 pm",
            "Status": "Active"
        },
        {
            "Title": "Insights",
            "CreatedDate": "10 Dec 2023, 06:43 am",
            "Status": "Active"
        },
        {
            "Title": "Commerce",
            "CreatedDate": "25 Dec 2023, 08:17 pm",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/crm-settings/sources.html', {'sources' : sources})

def lost_reason(request):
    lost_reason = [
        {
            "Title": "Client went silent",
            "CreatedAt": "25 Sep 2023, 01:22 pm",
            "Status": "Active",
        },
        {
            "Title": "Don't have the budget",
            "CreatedAt": "29 Sep 2023, 10:20 pm",
            "Status": "Active",
        },
        {
            "Title": "Doesn't pick up the phone, doesn't respond",
            "CreatedAt": "04 Oct 2023, 08:30 am",
            "Status": "Active",
        },
        {
            "Title": "Lack of expertise",
            "CreatedAt": "17 Oct 2023, 11:45 am",
            "Status": "Inactive",
        },
        {
            "Title": "Not responsible",
            "CreatedAt": "26 Oct 2023, 04:10 pm",
            "Status": "Active",
        },
        {
            "Title": "They couldn't afford our services",
            "CreatedAt": "08 Nov 2023, 05:23 am",
            "Status": "Active",
        },
        {
            "Title": "Went with our competitor",
            "CreatedAt": "11 Nov 2023, 02:32 pm",
            "Status": "Active",
        },
    ]
    return render(request, 'pages/crm-settings/lost-reason.html',{'lost_reason' : lost_reason}) 
  
def contact_stage(request):
    contact_stage = [
        {
            "Title": "Contacted",
            "CreatedAt": "25 Sep 2023, 01:22 pm",
            "Status": "Inactive",
        },
        {
            "Title": "Not Contacted",
            "CreatedAt": "29 Sep 2023, 10:20 pm",
            "Status": "Inactive",
        },
        {
            "Title": "Closed",
            "CreatedAt": "04 Oct 2023, 08:30 am",
            "Status": "Inactive",
        },
        {
            "Title": "Lost",
            "CreatedAt": "17 Oct 2023, 11:45 am",
            "Status": "Inactive",
        },
    ]
    return render(request, 'pages/crm-settings/contact-stage.html', {'contact_stage' : contact_stage})

def industry(request):
    industry = [
        {
            "Title": "Retail Industry",
            "CreatedAt": "25 Sep 2023, 01:22 pm",
            "Status": "Active",
        },
        {
            "Title": "Banking",
            "CreatedAt": "29 Sep 2023, 10:20 pm",
            "Status": "Active",
        },
        {
            "Title": "Hotels",
            "CreatedAt": "04 Oct 2023, 08:30 am",
            "Status": "Active",
        },
        {
            "Title": "Financial Services",
            "CreatedAt": "17 Oct 2023, 11:45 am",
            "Status": "Inactive",
        },
        {
            "Title": "Insurance",
            "CreatedAt": "26 Oct 2023, 04:10 pm",
            "Status": "Inactive",
        },
        {
            "Title": "Consulting",
            "CreatedAt": "08 Nov 2023, 05:23 am",
            "Status": "Inactive",
        },
        {
            "Title": "Agriculture",
            "CreatedAt": "11 Nov 2023, 02:32 pm",
            "Status": "Inactive",
        },
    ]
    return render(request, 'pages/crm-settings/industry.html', {'industry' : industry})

def calls(request):
    calls = [
        {
            "Title": "Busy",
            "CreatedAt": "25 Sep 2023, 01:22 pm",
            "Status": "Active",
        },
        {
            "Title": "No Answer",
            "CreatedAt": "29 Sep 2023, 10:20 pm",
            "Status": "Active",
        },
        {
            "Title": "Wrong Number",
            "CreatedAt": "04 Oct 2023, 08:30 am",
            "Status": "Active",
        },
        {
            "Title": "Unavailable",
            "CreatedAt": "17 Oct 2023, 11:45 am",
            "Status": "Inactive",
        },
]
    return render(request, 'pages/crm-settings/calls.html',{'calls' : calls})

# Reports

def lead_reports(request):
    lead_reports = [
        {
            "LeadName" : "Collins",
            "CompanyName" : "NovaWave LLC",
            "CompanyImage" : "assets/img/icons/company-icon-01.svg",
            "CompanyAddress" : "Newyork, USA",
            "Phone" : "+1 875455453",
            "Email" : "robertson@example.com",
            "CreatedDate" : "25 Sep 2023, 01:22 pm",
            "Owner" : "Hendry",
            "Source" : "Paid Social",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Konopelski",
            "CompanyName" : "BlueSky Industries",
            "CompanyImage" : "assets/img/icons/company-icon-02.svg",
            "CompanyAddress" : "Winchester, KY",
            "Phone" : "+1 989757485",
            "Email" : "sharon@example.com",
            "CreatedDate" : "29 Sep 2023, 04:15 pm",
            "Owner" : "Guillory",
            "Source" : "Referrals",
            "Status" : "Not Contacted",
        },
        {
            "LeadName" : "Adams",
            "CompanyName" : "SilverHawk",
            "CompanyImage" : "assets/img/icons/company-icon-03.svg",
            "CompanyAddress" : "Jametown, NY",
            "Phone" : "+1 546555455",
            "Email" : "vaughan12@example.com",
            "CreatedDate" : "04 Oct 2023, 10:18 am",
            "Owner" : "Jami",
            "Source" : "Campaigns",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Schumm",
            "CompanyName" : "SummitPeak",
            "CompanyImage" : "assets/img/icons/company-icon-04.svg",
            "CompanyAddress" : "Compton, RI",
            "Phone" : "+1 454478787",
            "Email" : "jessica13@example.com",
            "CreatedDate" : "17 Oct 2023, 03:31 pm",
            "Owner" : "Theresa",
            "Source" : "Google",
            "Status" : "Contacted",
        },
        {
            "LeadName" : "Wisozk",
            "CompanyName" : "RiverStone Ventur",
            "CompanyImage" : "assets/img/icons/company-icon-05.svg",
            "CompanyAddress" : "Dayton, OH",
            "Phone" : "+1 124547845",
            "Email" : "caroltho3@example.com",
            "CreatedDate" : "24 Oct 2023, 09:14 pm",
            "Owner" : "Espinosa",
            "Source" : "Paid Social",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Heller",
            "CompanyName" : "Bright Bridge Grp",
            "CompanyImage" : "assets/img/icons/company-icon-06.svg",
            "CompanyAddress" : "Lafayette, LA",
            "Phone" : "+1 478845447",
            "Email" : "dawnmercha@example.com",
            "CreatedDate" : "08 Nov 2023, 09:56 am",
            "Owner" : "Martin",
            "Source" : "Referrals",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Gutkowski",
            "CompanyName" : "CoastalStar Co.",
            "CompanyImage" : "assets/img/icons/company-icon-07.svg",
            "CompanyAddress" : "Centerville, VA",
            "Phone" : "+1 215544845",
            "Email" : "rachel@example.com",
            "CreatedDate" : "14 Nov 2023, 04:19 pm",
            "Owner" : "Newell",
            "Source" : "Campaigns",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Walter",
            "CompanyName" : "HarborView",
            "CompanyImage" : "assets/img/icons/company-icon-08.svg",
            "CompanyAddress" : "Providence, RI",
            "Phone" : "+1 121145471",
            "Email" : "jonelle@example.com",
            "CreatedDate" : "23 Nov 2023, 11:14 pm",
            "Owner" : "Janet",
            "Source" : "Google",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Hansen",
            "CompanyName" : "Golden Gate Ltd",
            "CompanyImage" : "assets/img/icons/company-icon-09.svg",
            "CompanyAddress" : "Swayzee, IN",
            "Phone" : "+1 321454789",
            "Email" : "jonathan@example.com",
            "CreatedDate" : "10 Dec 2023, 06:43 am",
            "Owner" : "Craig",
            "Source" : "Paid Social",
            "Status" : "Closed",
        },
        {
            "LeadName" : "Leuschke",
            "CompanyName" : "Redwood Inc",
            "CompanyImage" : "assets/img/icons/company-icon-10.svg",
            "CompanyAddress" : "Florida City, FL",
            "Phone" : "+1 278907145",
            "Email" : "brook@example.com",
            "CreatedDate" : "25 Dec 2023, 08:17 pm",
            "Owner" : "Daniel",
            "Source" : "Referrals",
            "Status" : "Closed",
        }
    ]
    return render(request, 'pages/reports/lead-reports.html',{'lead_reports' : lead_reports})

def deal_reports(request):
    deal_reports = [
        {
            "DealName": "Collins",
            "Stage": "Qualify To Buy",
            "DealValue": "$04,51,000",
            "Tag1": "Collab",
            "CloseDate": "25 Sep 2023",
            "CreatedDate" : "25 Sep 2023, 01:22 pm",
            "Owner" : "Hendry",
            "Source" : "Paid Social",
            "Probability": "90%",
            "Status": "Won"
        },
        {
            "DealName": "Konopelski",
            "Stage": "Proposal Made",
            "DealValue": "$03,12,500",
            "Tag1": "Rated",
            "CloseDate": "29 Sep 2023",
            "CreatedDate" : "29 Sep 2023, 04:15 pm",
            "Owner" : "Guillory",
            "Source" : "Referrals",
            "Probability": "15 %",
            "Status": "Lost"
        },
        {
            "DealName": "Adams",
            "Stage": "Contact Made",
            "DealValue": "$04,14,800",
            "Tag1": "Rejected",
            "CloseDate": "04 Oct 2023",
            "CreatedDate" : "04 Oct 2023, 10:18 am",
            "Owner" : "Jami",
            "Source" : "Campaigns",
            "Probability": "95 %",
            "Status": "Won"
        },
        {
            "DealName": "Schumm",
            "Stage": "Qualify To Buy",
            "DealValue": "$11,14,400",
            "Tag1": "Collab",
            "CloseDate": "15 Oct 2023",
            "CreatedDate" : "17 Oct 2023, 03:31 pm",
            "Owner" : "Theresa",
            "Source" : "Google",
            "Probability": "99 %",
            "Status": "Won"
        },
        {
            "DealName": "Wisozk",
            "Stage": "Presentation",
            "DealValue": "$16,11,400",
            "Tag1": "Rated",
            "CloseDate": "27 Oct 2023",
            "CreatedDate" : "24 Oct 2023, 09:14 pm",
            "Owner" : "Espinosa",
            "Source" : "Paid Social",
            "Probability": "10 %",
            "Status": "Open"
        },
        {
            "DealName": "Heller",
            "Stage": "Appointment",
            "DealValue": "$78,11,800",
            "Tag1": "Rated",
            "CloseDate": "07 Nov 2023",
            "CreatedDate" : "08 Nov 2023, 09:56 am",
            "Owner" : "Martin",
            "Source" : "Referrals",
            "Probability": "70 %",
            "Status": "Won"
        },
        {
            "DealName": "Gutkowski",
            "Stage": "Proposal Made",
            "DealValue": "$09,05,947",
            "Tag1": "Promotion",
            "CloseDate": "12 Nov 2023",
            "CreatedDate" : "14 Nov 2023, 04:19 pm",
            "Owner" : "Newell",
            "Source" : "Campaigns",
            "Probability": "10 %",
            "Status": "Open"
        },
        {
            "DealName": "Walter",
            "Stage": "Qualify To Buy",
            "DealValue": "$04,51,000",
            "Tag1": "Rejected",
            "CloseDate": "23 Nov 2023",
            "CreatedDate" : "23 Nov 2023, 11:14 pm",
            "Owner" : "Janet",
            "Source" : "Google",
            "Probability": "90 %",
            "Status": "Won"
        },
        {
            "DealName": "Hansen",
            "Stage": "Appointment",
            "DealValue": "$72,14,078",
            "Tag1": "Collab",
            "CloseDate": "11 Dec 2023",
            "CreatedDate" : "10 Dec 2023, 06:43 am",
            "Owner" : "Craig",
            "Source" : "Paid Social",
            "Probability": "40 %",
            "Status": "Won"
        },
        {
            "DealName": "Leuschke",
            "Stage": "Proposal Made",
            "DealValue": "$09,05,947",
            "Tag1": "Rated",
            "CloseDate": "17 Dec 2023",
            "CreatedDate" : "25 Dec 2023, 08:17 pm",
            "Owner" : "Daniel",
            "Source" : "Referrals",
            "Probability": "47 %",
            "Status": "Lost"
        }
    ]
    return render(request, 'pages/reports/deal-reports.html', {'deal_reports' : deal_reports})

def contact_reports(request):
    contact_reports = [
        {
            "CustomerName" : "Darlee Robertson",
            "CustomerImage" : "assets/img/profiles/avatar-19.jpg",
            "CustomerNo" : "Facility Manager",
            "Phone" : "1234567890",
            "Email" : "robertson@example.com",
            "CreatedDate" : "25 Sep 2023, 01:22 pm",
            "Owner" : "Hendry",
            "Source" : "Paid Social",
            "CompanyName" : "NovaWave LLC",
            "CompanyImage" : "assets/img/icons/company-icon-01.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Retail Industry",
            "Type" : "Customer",
        },
        {
            "CustomerName" : "Sharon Roy",
            "CustomerImage" : "assets/img/profiles/avatar-20.jpg",
            "CustomerNo" : "Installer",
            "Phone" : "+1 989757485",
            "Email" : "sharon@example.com",
            "CreatedDate" : "29 Sep 2023, 04:15 pm",
            "Owner" : "Guillory",
            "Source" : "Referrals",
            "CompanyName" : "BlueSky Industries",
            "CompanyImage" : "assets/img/icons/company-icon-02.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Banking",
            "Type" : "Accounts",
        },
        {
            "CustomerName" : "Vaughan",
            "CustomerImage" : "assets/img/profiles/avatar-21.jpg",
            "CustomerNo" : "Senior  Manager",
            "Phone" : "+1 546555455",
            "Email" : "vaughan12@example.com",
            "CreatedDate" : "04 Oct 2023, 10:18 am",
            "Owner" : "Jami",
            "Source" : "Campaigns",
            "CompanyName" : "SilverHawk",
            "CompanyImage" : "assets/img/icons/company-icon-03.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Hotels",
            "Type" : "Partner",
        },
        {
            "CustomerName" : "Jessica",
            "CustomerImage" : "assets/img/profiles/avatar-23.jpg",
            "CustomerNo" : "Test Engineer",
            "Phone" : "+1 454478787",
            "Email" : "jessica13@example.com",
            "CreatedDate" : "17 Oct 2023, 03:31 pm",
            "Owner" : "Theresa",
            "Source" : "Google",
            "CompanyName" : "SummitPeak",
            "CompanyImage" : "assets/img/icons/company-icon-04.svg",
            "Owner_image": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Financial Services",
            "Type" : "Prospect",
        },
        {
            "CustomerName" : "Carol Thomas",
            "CustomerImage" : "assets/img/profiles/avatar-16.jpg",
            "CustomerNo" : "UI /UX Designer",
            "Phone" : "+1 124547845",
            "Email" : "caroltho3@example.com",
            "CreatedDate" : "24 Oct 2023, 09:14 pm",
            "Owner" : "Espinosa",
            "Source" : "Paid Social",
            "CompanyName" : "RiverStone Ventur",
            "CompanyImage" : "assets/img/icons/company-icon-05.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Insurance",
            "Type" : "Lead",
        },
        {
            "CustomerName" : "Dawn Mercha",
            "CustomerImage" : "assets/img/profiles/avatar-22.jpg",
            "CustomerNo" : "Technician",
            "Phone" : "+1 478845447",
            "Email" : "dawnmercha@example.com",
            "CreatedDate" : "08 Nov 2023, 09:56 am",
            "Owner" : "Martin",
            "Source" : "Referrals",
            "CompanyName" : "Bright Bridge Grp",
            "CompanyImage" : "assets/img/icons/company-icon-06.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Consulatation",
            "Type" : "Influencer",
        },
        {
            "CustomerName" : "Rachel Hampton",
            "CustomerImage" : "assets/img/profiles/avatar-24.jpg",
            "CustomerNo" : "Software Developer",
            "Phone" : "+1 215544845",
            "Email" : "rachel@example.com",
            "CreatedDate" : "14 Nov 2023, 04:19 pm",
            "Owner" : "Newell",
            "Source" : "Campaigns",
            "CompanyName" : "CoastalStar Co.",
            "CompanyImage" : "assets/img/icons/company-icon-07.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Agriculture",
            "Type" : "Vendor",
        },
        {
            "CustomerName" : "Jonelle Curtiss",
            "CustomerImage" : "assets/img/profiles/avatar-25.jpg",
            "CustomerNo" : "Supervisor",
            "Phone" : "+1 121145471",
            "Email" : "jonelle@example.com",
            "CreatedDate" : "23 Nov 2023, 11:14 pm",
            "Owner" : "Janet",
            "Source" : "Google",
            "CompanyName" : "HarborView",
            "CompanyImage" : "assets/img/icons/company-icon-08.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Insurance",
            "Type" : "Customer",
        },
        {
            "CustomerName" : "Jonathan",
            "CustomerImage" : "assets/img/profiles/avatar-26.jpg",
            "CustomerNo" : "Team Lead Dev",
            "Phone" : "+1 321454789",
            "Email" : "jonathan@example.com",
            "CreatedDate" : "10 Dec 2023, 06:43 am",
            "Owner" : "Craig",
            "Source" : "Paid Social",
            "CompanyName" : "Golden Gate Ltd",
            "CompanyImage" : "assets/img/icons/company-icon-09.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Banking",
            "Type" : "Accounts",
        },
        {
            "CustomerName" : "Brook",
            "CustomerImage" : "assets/img/profiles/avatar-01.jpg",
            "CustomerNo" : "Team Lead Dev ",
            "Phone" : "+1 278907145",
            "Email" : "brook@example.com",
            "CreatedDate" : "25 Dec 2023, 08:17 pm",
            "Owner" : "Daniel",
            "Source" : "Referrals",
            "CompanyName" : "Redwood Inc",
            "CompanyImage" : "assets/img/icons/company-icon-10.svg",
            "OwnerImage": "assets/img/profiles/avatar-14.jpg",
            "Industry" : "Financial Services",
            "Type" : "Influencer",
        }
    ]
    return render(request, 'pages/reports/contact-reports.html',{'contact_reports' : contact_reports})

def company_reports(request):
    company_reports = [
        {
            "CompanyName" : "NovaWave LLC",
            "CompanyImage" : "assets/img/icons/company-icon-01.svg",
            "Phone" : "+1 875455453",
            "Email" : "robertson@example.com",
            "Location" : "Germany",
            "Owner" : "Hendry",
            "Source": "Paid Social",
            "WonDeals": "5 Deals, $100000",
            "LostDeals": "2 Deals, $80000",
            "CreatedDate": "25 Sep 2023, 01:22 pm"
        },
        {
            "CompanyName" : "BlueSky Industries",
            "CompanyImage" : "assets/img/icons/company-icon-02.svg",
            "Phone" : "+1 989757485",
            "Email" : "sharon@example.com",
            "Location" : "USA",
            "Owner" : "Guillory",
            "Source": "Referrals",
            "WonDeals": "4 Deals, $120000",
            "LostDeals": "3 Deals, $90000",
            "CreatedDate": "29 Sep 2023, 04:15 pm"
        },
        {
            "CompanyName" : "SilverHawk",
            "CompanyImage" : "assets/img/icons/company-icon-03.svg",
            "Phone" : "+1 546555455",
            "Email" : "vaughan12@example.com",
            "Location" : "Canada",
            "Owner" : "Jami",
            "Source": "Campaigns",
            "WonDeals": "3 Deals, $110000",
            "LostDeals": "2 Deals, $70000",
            "CreatedDate": "04 Oct 2023, 10:18 am"
        },
        {
            "CompanyName" : "SummitPeak",
            "CompanyImage" : "assets/img/icons/company-icon-04.svg",
            "Phone" : "+1 454478787",
            "Email" : "jessica13@example.com",
            "Location" : "India",
            "Owner" : "Theresa",
            "Source": "Google",
            "WonDeals": "6 Deals, $200000",
            "LostDeals": "3 Deals, $100000",
            "CreatedDate": "17 Oct 2023, 03:31 pm"
        },
        {
            "CompanyName" : "RiverStone Ventur",
            "CompanyImage" : "assets/img/icons/company-icon-05.svg",
            "Phone" : "+1 124547845",
            "Email" : "caroltho3@example.com",
            "Location" : "China",
            "Owner" : "Espinosa",
            "Source": "Paid Social",
            "WonDeals": "3 Deals, $80000",
            "LostDeals": "1 Deal, $40000",
            "CreatedDate": "24 Oct 2023, 09:14 pm"
        },
        {
            "CompanyName" : "Bright Bridge Grp",
            "CompanyImage" : "assets/img/icons/company-icon-06.svg",
            "Phone" : "+1 478845447",
            "Email" : "dawnmercha@example.com",
            "Location" : "Japan",
            "Owner" : "Martin",
            "Source": "Referrals",
            "WonDeals": "5 Deals, $95000",
            "LostDeals": "2 Deals, $60000",
            "CreatedDate": "08 Nov 2023, 09:56 am"
        },
        {
            "CompanyName" : "CoastalStar Co.",
            "CompanyImage" : "assets/img/icons/company-icon-07.svg",
            "Phone" : "+1 215544845",
            "Email" : "rachel@example.com",
            "Location" : "Indonesia",
            "Owner" : "Newell",
            "Source": "Campaigns",
            "WonDeals": "4 Deals, $100000",
            "LostDeals": "1 Deal, $50000",
            "CreatedDate": "14 Nov 2023, 04:19 pm"
        },
        {
            "CompanyName" : "HarborView",
            "CompanyImage" : "assets/img/icons/company-icon-08.svg",
            "Phone" : "+1 121145471",
            "Email" : "jonelle@example.com",
            "Location" : "Cuba",
            "Owner" : "Janet",
            "Source": "Google",
            "WonDeals": "3 Deals, $70000",
            "LostDeals": "3 Deals, $80000",
            "CreatedDate": "23 Nov 2023, 11:14 pm"
        },
        {
            "CompanyName" : "Golden Gate Ltd",
            "CompanyImage" : "assets/img/icons/company-icon-09.svg",
            "Phone" : "+1 321454789",
            "Email" : "jonathan@example.com",
            "Location" : "Isreal",
            "Owner" : "Craig",
            "Source": "Referrals",
            "WonDeals": "6 Deals, $130000",
            "LostDeals": "4 Deals, $100000",
            "CreatedDate": "10 Dec 2023, 06:43 am"
        },
        {
            "CompanyName" : "Redwood Inc",
            "CompanyImage" : "assets/img/icons/company-icon-10.svg",
            "Phone" : "+1 278907145",
            "Email" : "brook@example.com",
            "Location" : "Colombia",
            "Owner" : "Daniel",
            "Source": "Campaigns",
            "WonDeals": "5 Deals, $90000",
            "LostDeals": "2 Deals, $55000",
            "CreatedDate": "25 Dec 2023, 08:17 pm"
        },
        {
            "CompanyName" : "SilverHawk",
            "CompanyImage" : "assets/img/icons/company-icon-03.svg",
            "Phone" : "+1 546555455",
            "Email" : "vaughan12@example.com",
            "Location" : "Canada",
            "Owner" : "Jami",
            "Source": "Paid Social",
            "WonDeals": "5 Deals, $100000",
            "LostDeals": "2 Deals, $80000",
            "CreatedDate": "25 Sep 2023, 01:22 pm"
        },
        {
            "CompanyName" : "SummitPeak",
            "CompanyImage" : "assets/img/icons/company-icon-04.svg",
            "Phone" : "+1 454478787",
            "Email" : "jessica13@example.com",
            "Location" : "India",
            "Owner" : "Theresa",
            "Source": "Google",
            "WonDeals": "3 Deals, $70000",
            "LostDeals": "3 Deals, $80000",
            "CreatedDate": "23 Nov 2023, 11:14 pm"
        }
    ]
    return render(request, 'pages/reports/company-reports.html',{'company_reports' : company_reports})

def project_reports(request):
    project_reports = [
         {
            "NameImage": "assets/img/priority/truellysel.svg",
            "CompanyImage": "assets/img/icons/company-icon-01.svg",
            "Name": "Truelysell",
            "Client": "NovaWave LLC",
            "Priority": "High",
            "StartDate": "25 Sep 2023",
            "EndDate": "15 Oct 2023",
            "Type": "Web App",
            "PipelineStage": "Plan",
            "BudgetValue": "$200000",
            "CurrentlySpend": "$40000",
        },
        {
            "NameImage": "assets/img/priority/dreamchat.svg",
            "CompanyImage": "assets/img/icons/company-icon-02.svg",
            "Name": "Dreamschat",
            "Client": "BlueSky Industries",
            "Priority": "Medium",
            "StartDate": "29 Sep 2023",
            "EndDate": "19 Oct 2023",
            "Type": "Web App",
            "PipelineStage": "Develop",
            "BudgetValue": "$300000",
            "CurrentlySpend": "$120000",
        },
        {
            "NameImage": "assets/img/priority/truellysell.svg",
            "CompanyImage": "assets/img/icons/company-icon-03.svg",
            "Name": "Truelysell",
            "Client": "SilverHawk",
            "Priority": "High",
            "StartDate": "05 Oct 2023",
            "EndDate": "12 Oct 2023",
            "Type": "Web App",
            "PipelineStage": "Completed",
            "BudgetValue": "$200000",
            "CurrentlySpend": "$200000",
        },
        {
            "NameImage": "assets/img/priority/servbook.svg",
            "CompanyImage": "assets/img/icons/company-icon-04.svg",
            "Name": "Servbook",
            "Client": "SummitPeak",
            "Priority": "Medium",
            "StartDate": "14 Oct 2023",
            "EndDate": "24 Oct 2023",
            "Type": "Web App",
            "PipelineStage": "Design",
            "BudgetValue": "$300000",
            "CurrentlySpend": "$60000",
        },
        {
            "NameImage": "assets/img/priority/dream-pos.svg",
            "CompanyImage": "assets/img/icons/company-icon-05.svg",
            "Name": "DreamPOS",
            "Client": "RiverStone Ventur",
            "Priority": "Low",
            "StartDate": "15 Nov 2023",
            "EndDate": "22 Nov 2023",
            "Type": "Web App",
            "PipelineStage": "Design",
            "BudgetValue": "$120000",
            "CurrentlySpend": "$40000",
        },
        {
            "NameImage": "assets/img/priority/project-01.svg",
            "CompanyImage": "assets/img/icons/company-icon-06.svg",
            "Name": "Kofejob",
            "Client": "CoastalStar Co.",
            "Priority": "High",
            "StartDate": "25 Nov 2023",
            "EndDate": "09 Dec 2023",
            "Type": "Meeting",
            "PipelineStage": "Develop",
            "BudgetValue": "$200000",
            "CurrentlySpend": "$90000",
        },
        {
            "NameImage": "assets/img/priority/project-02.svg",
            "CompanyImage": "assets/img/icons/company-icon-07.svg",
            "Name": "Doccure",
            "Client": "HarborView",
            "Priority": "Medium",
            "StartDate": "08 Dec 2023",
            "EndDate": "16 Dec 2023",
            "Type": "Web App",
            "PipelineStage": "Completed",
            "BudgetValue": "$200000",
            "CurrentlySpend": "$195000",
        },
        {
            "NameImage": "assets/img/priority/best.svg",
            "CompanyImage": "assets/img/icons/company-icon-08.svg",
            "Name": "Best@laundry",
            "Client": "Golden Gate Ltd",
            "Priority": "Low",
            "StartDate": "21 Dec 2023",
            "EndDate": "13 Jan 2024",
            "Type": "Meeting",
            "PipelineStage": "Completed",
            "BudgetValue": "$230000",
            "CurrentlySpend": "$220000",
        },
        {
            "NameImage": "assets/img/priority/dream-pos.svg",
            "CompanyImage": "assets/img/icons/company-icon-06.svg",
            "Name": "POS",
            "Client": "CoastalStar Inc",
            "Priority": "Medium",
            "StartDate": "01 Jan 2024",
            "EndDate": "11 Jan 2024",
            "Type": "Web App",
            "PipelineStage": "Develop",
            "BudgetValue": "$200000",
            "CurrentlySpend": "$177777",
        },
        {
            "NameImage": "assets/img/priority/servbook.svg",
            "CompanyImage": "assets/img/icons/company-icon-09.svg",
            "Name": "Bookserv",
            "Client": "Redwood Inc",
            "Priority": "Medium",
            "StartDate": "12 Jan 2024",
            "EndDate": "29 Jan 2024",
            "Type": "Meeting",
            "PipelineStage": "Develop",
            "BudgetValue": "$300000",
            "CurrentlySpend": "$100000",
        },
    ]
    return render(request, 'pages/reports/project-reports.html',{'project_reports' : project_reports})

def task_reports(request):
    task_reports = [
        {
            "TaskName": "Add a form to Update Task",
            "AssignedTo": "Adrian Davies",
            "Priority": "High",
            "DueDate": "25 Sep 2023",
            "Type": "Calls",
            "Status": "Inprogress",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "25 Sep 2023, 01:22 pm",
        },
        {
            "TaskName": "Make all strokes thinner",
            "AssignedTo": "Adrian Davies",
            "Priority": "Medium",
            "DueDate": "29 Sep 2023",
            "Type": "Meeting",
            "Status": "Completed",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "29 Sep 2023, 04:15 pm",
        },
        {
            "TaskName": "Update orginal contentuelysell",
            "AssignedTo": "Adrian Davies",
            "Priority": "High",
            "DueDate": "05 Oct 2023",
            "Type": "Email",
            "Status": "Inprogress",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "04 Oct 2023, 10:18 am",
        },
        {
            "TaskName": "Use only component colours",
            "AssignedTo": "Adrian Davies",
            "Priority": "Medium",
            "DueDate": "14 Oct 2023",
            "Type": "Meeting",
            "Status": "Completed",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "17 Oct 2023, 03:31 pm",
        },
        {
            "TaskName": "Add images to the cards section",
            "AssignedTo": "Adrian Davies",
            "Priority": "Low",
            "DueDate": "15 Nov 2023",
            "Type": "Task",
            "Status": "Inprogress",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "24 Oct 2023, 09:14 pm",
        },
        {
            "TaskName": "Design description banner & landing page",
            "AssignedTo": "Adrian Davies",
            "Priority": "High",
            "DueDate": "25 Nov 2023",
            "Type": "Calls",
            "Status": "Completed",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "08 Nov 2023, 09:56 am",
        },
        {
            "TaskName": "Make sure all the padding should be 24px",
            "AssignedTo": "Adrian Davies",
            "Priority": "Low",
            "DueDate": "08 Dec 2023",
            "Type": "Email",
            "Status": "Completed",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "14 Nov 2023, 04:19 pm",
        },
        {
            "TaskName": "Use border radius as 5px or 10 px",
            "AssignedTo": "Adrian Davies",
            "Priority": "Medium",
            "DueDate": "21 Dec 2023",
            "Type": "Task",
            "Status": "Completed",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "23 Nov 2023, 11:14 pm",
        },
        {
            "TaskName": "Use Grey scale colors as body color",
            "AssignedTo": "Adrian Davies",
            "Priority": "Medium",
            "DueDate": "21 Dec 2023",
            "Type": "Meeting",
            "Status": "Inprogress",
            "Image" : "assets/img/profiles/avatar-14.jpg",
            "CreatedDate": "10 Dec 2023, 06:43 am",
        }
    ]
    return render(request, 'pages/reports/task-reports.html',{'task_reports' : task_reports})

# Content

def pages(request):
    pages = [
        {
			"Pages" :"Home",
			"PageSlug" : "home",
			"Status" : "Active",
		},
		{
			"Pages" :"About Us",
			"PageSlug" : "about-us",
			"Status" : "Inactive",
		},
		{
			"Pages" :"FAQ",
			"PageSlug" : "faq",
			"Status" : "Active",
		},
		{
			"Pages" :"Categories",
			"PageSlug" : "categories",
			"Status" : "Active",
		},
		{
			"Pages" :"Terms & Conditions",
			"PageSlug" : "terms-conditions",
			"Status" : "Active",
		},
		{
			"Pages" :"Privacy Policy",
			"PageSlug" : "privacy policy",
			"Status" : "Active",
		},
		{
			"Pages" :"Contact US",
			"PageSlug" : "contact-us",
			"Status" : "Active",
		}
    ]
    return render(request, 'pages/content/pages.html',{'pages' : pages})

def countries(request):
    countries = [
        {
            "CountryCode": "AS",
            "CountryId": "684",
            "CountryImage":"assets/img/flags/as.png",
            "CountryName": "American Samoa (+684)",
        },
        {
            "CountryCode": "AD",
            "CountryId": "376",
            "CountryImage":"assets/img/flags/ad.png",
            "CountryName": "Andorra (+376)",
        },
        {
            "CountryCode": "AO",
            "CountryId": "244",
            "CountryImage":"assets/img/flags/ao.png",
            "CountryName": "Angalo (+244)",
        },
        {
            "CountryCode": "AI",
            "CountryId": "1264",
            "CountryImage":"assets/img/flags/ai.png",
            "CountryName": "Anguilla (+1264)",
        },
        {
            "CountryCode": "AQ",
            "CountryId": "672",
            "CountryImage":"assets/img/flags/qa.png",
            "CountryName": "Antarctica (+672)",
        },
        {
            "CountryCode": "AG",
            "CountryId": "1268",
            "CountryImage":"assets/img/flags/ag.png",
            "CountryName": "Antigua & Barbuda (+1268)",
        },
        {
            "CountryCode": "AR",
            "CountryId": "54",
            "CountryImage":"assets/img/flags/ar.png",
            "CountryName": "Argentina (+54)",
        },
        {
            "CountryCode": "AU",
            "CountryId": "61",
            "CountryImage":"assets/img/flags/au.png",
            "CountryName": "Australia (+61)",
        },
        {
            "CountryCode": "AT",
            "CountryId": "43",
            "CountryImage":"assets/img/flags/at.png",
            "CountryName": "Austria (+43)",
        },
        {
            "CountryCode": "AZ",
            "CountryId": "994",
            "CountryImage":"assets/img/flags/az.png",
            "CountryName": "Azerbaijan (+994)",
        }
    ]
    return render(request, 'pages/content/location/countries.html', {'countries' : countries})
 
def states(request):
    states = [
        {
            "CountryCode" : "AS",
			"StateName" : "American Samosa(+684)",
			"CountryImage":"assets/img/flags/as.png",
			"State": "Swains Island",
		},
		{
            "CountryCode" : "AD",
			"StateName" : "Andorra(+376)",
			"CountryImage":"assets/img/flags/ad.png",
			"State": "Andorra la Vella",
			
		},
		{
            "CountryCode" : "AO",
			"StateName" : "Angola(+244)",
			"CountryImage":"assets/img/flags/ao.png",
			"State": "Benguella",
		},
		{
            "CountryCode" : "AI",
			"StateName" : "Angulila(+1264)",
			"CountryImage":"assets/img/flags/ai.png",
			"State": "The Valley",
		},
		{
			"CountryCode" : "AQ",
			"StateName" : "Antartica(+672)",
			"CountryImage":"assets/img/flags/qa.png",
			"State": "Victoria Land",
		},
		{
			"CountryCode" : "AG",
			"StateName" : "Antigua & Barbuda(+1268)",
			"CountryImage":"assets/img/flags/ag.png",
			"State": "Saint Paul",
		},
		{
			"CountryCode" : "AR",
			"StateName" : "Argentina(+54)",
			"CountryImage":"assets/img/flags/ar.png",
			"State": "Santa Fe",
		},
		{
			"CountryCode" : "AU",
			"StateName" : "Australia(+61)",
			"CountryImage":"assets/img/flags/au.png",
			"State": "Queensland",
		},
		{
			"CountryCode" : "AT",
			"StateName" : "Austria(+43)",
			"CountryImage":"assets/img/flags/at.png",
			"State": "Tyrol",
		},
		{
			"CountryCode" : "AZ",
			"StateName" : "Azerbaijan(+994)",
			"CountryImage":"assets/img/flags/az.png",
			"State": "Karabakh",
		}
    ]
    return render(request, 'pages/content/location/states.html', {'states' : states})

def cities(request):
    cities = [
        {
            "CityName" : "Gandzasar",
			"CountryName" : "American Samosa(+684)",
			"CountryImage":"assets/img/flags/as.png",
			"StateName": "Swains Island",
		},
		{
            "CityName" : "Escaldes-Engordany",
			"CountryName" : "Andorra(+376)",
			"CountryImage":"assets/img/flags/ad.png",
			"StateName": "Andorra la Vella",
			
		},
		{
            "CityName" : "Chissamba",
			"CountryName" : "Angola(+244)",
			"CountryImage":"assets/img/flags/ao.png",
			"StateName": "Benguella",
		},
		{
            "CityName" : "Illinois",
			"CountryName" : "Angulila(+1264)",
			"CountryImage":"assets/img/flags/ai.png",
			"StateName": "The Valley",
		},
		{
			"CityName" : "Melbourne",
			"CountryName" : "Antartica(+672)",
			"CountryImage":"assets/img/flags/qa.png",
			"StateName": "Victoria Land",
		},
		{
			"CityName" : "Maplewood",
			"CountryName" : "Antigua & Barbuda(+1268)",
			"CountryImage":"assets/img/flags/ag.png",
			"StateName": "Saint Paul",
		},
		{
			"CityName" : "Rosario",
			"CountryName" : "Argentina(+54)",
			"CountryImage":"assets/img/flags/ar.png",
			"StateName": "Santa Fe",
		},
		{
			"CityName" : "Atherton",
			"CountryName" : "Australia(+61)",
			"CountryImage":"assets/img/flags/au.png",
			"StateName": "Queensland",
		},
		{
			"CityName" : "Mayrhofen",
			"CountryName" : "Austria(+43)",
			"CountryImage":"assets/img/flags/at.png",
			"StateName": "Tyrol",
		},
		{
			"CityName" : "Askeran",
			"CountryName" : "Azerbaijan(+994)",
			"CountryImage":"assets/img/flags/az.png",
			"StateName": "Karabakh",
		}
    ]
    return render(request, 'pages/content/location/cities.html', {'cities' : cities})

def testimonials(request):
    testimonials = [
		{
			"CustomerName" : "Darlee Robertson",
			"CustomerImage" : "assets/img/profiles/avatar-19.jpg",
			"CustomerDesignation" : "Facility Manager",
			"Content" : "Project was received ontime without any mistake",
			"Status" : "Inactive",
            "Createdate" : "25 Sep 2023, 01:22pm",
		},
		{
			"CustomerName" : "Sharon Roy",
			"CustomerImage" : "assets/img/profiles/avatar-20.jpg",
			"CustomerDesignation" : "Installer",
			"Content" : "It help us to manage, track & do more business",
            "Status" : "Inactive",
            "Createdate" : "29 Sep 2023, 08:12 am",
		},
		{
			"CustomerName" : "Vaughan",
			"CustomerImage" : "assets/img/profiles/avatar-21.jpg",
			"CustomerDesignation" : "Senior  Manager",
			"Content" : "Brillant tool to manage leads & projects",
			"Status" : "Active",
            "Createdate" : "02 Oct 2023, 10:15 am",
		},
		{
			"CustomerName" : "Jessica",
			"CustomerImage" : "assets/img/profiles/avatar-23.jpg",
			"CustomerDesignation" : "Test Engineer",
			"Content" : "Very responsive and accurate with suggestions",
			"Status" : "Active",
            "Createdate" : "11 Oct 2023, 02:32 pm",
		},
		{
			"CustomerName" : "Carol Thomas",
			"CustomerImage" : "assets/img/profiles/avatar-16.jpg",
			"CustomerDesignation" : "UI /UX Designer",
			"Content" : "Happy with measurable on lead management",
			"Status" : "Inactive",
            "Createdate" : "4 Nov 2023, 04:22 pm",
		},
		{
			"CustomerName" : "Dawn Mercha",
			"CustomerImage" : "assets/img/profiles/avatar-22.jpg",
			"CustomerDesignation" : "Technician",
			"Content" : "Pipeline are great for tracking process",
			"Status" : "Active",
            "Createdate" : "16 Nov 2023, 10:51 pm",
		},
		{
			"CustomerName" : "Rachel Hampton",
			"CustomerImage" : "assets/img/profiles/avatar-24.jpg",
			"CustomerDesignation" : "Software Developer",
			"Content" : "It have complete visiblity of clients & interactions",
			"Status" : "Active",
            "Createdate" : "25 Nov 2023, 3:43 pm",
		},
		{
			"CustomerName" : "Jonelle Curtiss",
			"CustomerImage" : "assets/img/profiles/avatar-25.jpg",
			"CustomerDesignation" : "Supervisor",
			"Content" : "Give customer best possible service & support",
			"Status" : "Active",
            "Createdate" : "07 Dec 2023, 11:22 am",
		},
		{
			"CustomerName" : "Jonathan",
			"CustomerImage" : "assets/img/profiles/avatar-26.jpg",
			"CustomerDesignation" : "Team Lead Dev",
			"Content" : "It give accurate and real time information",
			"Status" : "Active",
            "Createdate" : "15 Dec 2023, 8:17 am",
		},
		{
			"CustomerName" : "Eric Adams",
			"CustomerImage" : "assets/img/profiles/avatar-06.jpg",
			"CustomerDesignation" : "HR Manager",
			"Content" : "Most efficient process, accurate & consistent data",
			"Status" : "Active",
            "Createdate" : "29 Dec 2023, 1:22 pm",
		}
	]
    return render(request, 'pages/content/testimonials.html', {'testimonials' : testimonials})

def faq(request):
    faq = [
         {
            "Questions": "How can I book a service",
            "Category": "Services",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "25 Sep 2023, 01:22 pm",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Advertising",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "29 Sep 2023, 08:12 am",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Services",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "02 Oct 2023, 02:32 pm",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Services",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "11 Oct 2023, 02:32 pm",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Media",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "04 Nov 2023, 04:22 pm",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Content Marketing",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "16 Nov 2023, 10:51 pm",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Health Care",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "25 Nov 2023, 03:43 pm",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Services",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "07 Dec 2023, 11:22 am",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Social Marketing",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "15 Dec 2023, 08:17 am",
            "Status" : "Active",
        },
        {
            "Questions": "How can I book a service",
            "Category": "Media",
            "Answers": "Lorem ipsum dolor amet, adipiscing elit",
            "CreatedAt": "29 Dec 2023, 01:22 pm",
            "Status" : "Active",
        }
    ]
    return render(request, 'pages/content/faq.html', {'faq' : faq})
 
# Membership 

def membership_plans(request):
    return render(request, 'pages/membership/membership-plans.html') 
 
def membership_addons(request):
    return render(request, 'pages/membership/membership-addons.html') 
 
def membership_transactions(request):
    membership_transactions = [
        {
            "Type" : "Wallet Topup",
			"Amount" : "+$650",
			"Date":"25 Sep 2023, 01:22 pm",
            "PaymentType":"Paypal",
			"Status": "Completed"
		},
        {
            "Type" : "Purchase",
			"Amount" : "-350",
			"Date":"27 Sep 2023, 04:18 pm",
            "PaymentType":"Cash",
			"Status": "Cancel"
		},
        {
            "Type" : "Refund",
			"Amount" : "+$100",
			"Date":"29 Sep 2023, 10:08 am",
            "PaymentType":"Paypal",
			"Status": "Completed"
		},
        {
            "Type" : "Wallet Topup",
			"Amount" : "+$650",
			"Date":"05 Oct 2023, 09:43 am",
            "PaymentType":"Cash",
			"Status": "Completed"
		},
        {
            "Type" : "Wallet Topup",
			"Amount" : "+$650",
			"Date":"17 Oct 2023, 01:22 am",
            "PaymentType":"Paypal",
			"Status": "Cancel"
		},
        {
            "Type" : "Wallet Topup",
			"Amount" : "+$650",
			"Date":"22 Oct 2023, 06:32 pm",
            "PaymentType":"Cash",
			"Status": "Completed"
		}
    ]
    return render(request, 'pages/membership/membership-transactions.html', {'membership_transactions' : membership_transactions}) 
 
# User Management 
 
def roles_permissions(request):
    roles_permissions = [
        {
			"RolesName" : "Admin",
			"Created" : "25 Sep 2023, 12:12 pm",
		},
		{
			"RolesName" : "Company Owner",
			"Created" : "27 Sep 2023, 07:40 am",
		},
		{
			"RolesName" : "Deal Owner",
			"Created" : "29 Sep 2023, 08:20 am",
		},
		{
			"RolesName" : "Project Manager",
			"Created" : "25 Sep 2023, 12:12 pm",
		},
		{
			"RolesName" : "Client",
			"Created" : "15 Oct 2023, 06:18 pm",
		},
		{
			"RolesName" : "Lead",
			"Created" : "29 Oct 2023, 03:10 pm",
		}
    ]
    return render(request, 'pages/user-management/roles-permissions.html',{'roles_permissions' : roles_permissions })
 
def permission(request):
    permission = [
        {
			"Module" : "Dashboard",
			"SubModule" : "Dashboard",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Contacts",
			"SubModule" : "Contacts",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Companies",
			"SubModule" : "Companies",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Leads",
			"SubModule" : "Leads",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Deals",
			"SubModule" : "Deals",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Pipelines",
			"SubModule" : "Pipelines",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Compaign",
			"SubModule" : "Compaign",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Projects",
			"SubModule" : "Projects",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Tasks",
			"SubModule" : "Tasks",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		},
		{
			"Module" : "Activity",
			"SubModule" : "Activity",
			"Create" : "",
			"Edit" : "",
			"View" : "",
			"Delete" : "",
			"Allow" : ""
		}
    ]
    return render(request ,'pages/user-management/permission.html', {'permission' : permission}) 
 
def delete_request(request):
    delete_request = [
        {
			"CustomerName" : "Darlee Robertson",
			"CustomerImage" : "assets/img/profiles/avatar-19.jpg",
			"CustomerNo" : "Facility Manager",
			"Created" : "25 Sep 2023, 12:12 pm",
			"DeleteRequest": "25 Sep 2023, 12:12 pm",
		},
		{
			"CustomerName" : "Sharon Roy",
			"CustomerImage" : "assets/img/profiles/avatar-20.jpg",
			"CustomerNo" : "Installer",
			"Created" : "27 Sep 2023, 07:40 am",
			"DeleteRequest" : "27 Sep 2023, 07:40 am",
		},
		{
			"CustomerName" : "Vaughan",
			"CustomerImage" : "assets/img/profiles/avatar-21.jpg",
			"CustomerNo" : "Senior  Manager",
			"Created" : "29 Sep 2023, 08:20 am",
			"DeleteRequest": "29 Sep 2023, 08:20 am",
		},
		{
			"CustomerName" : "Jessica",
			"CustomerImage" : "assets/img/profiles/avatar-23.jpg",
			"CustomerNo" : "Test Engineer",
			"Created" : "25 Sep 2023, 12:12 pm",
			"DeleteRequest": "25 Sep 2023, 12:12 pm",
		},
		{
			"CustomerName" : "Carol Thomas",
			"CustomerImage" : "assets/img/profiles/avatar-16.jpg",
			"CustomerNo" : "UI /UX Designer",
			"Created" : "02 Oct 2023, 10:10 am",
			"DeleteRequest": "02 Oct 2023, 10:10 am",
		},
		{
			"CustomerName" : "Dawn Mercha",
			"CustomerImage" : "assets/img/profiles/avatar-22.jpg",
			"CustomerNo" : "Technician",
			"Created" : "17 Oct 2023, 04:25 pm",
			"DeleteRequest": "17 Oct 2023, 04:25 pm",
		},
		{
			"CustomerName" : "Rachel Hampton",
			"CustomerImage" : "assets/img/profiles/avatar-24.jpg",
			"CustomerNo" : "Software Developer",
			"Created" : "28 Oct 2023, 07:16 am",
			"DeleteRequest": "28 Oct 2023, 07:16 am",
		},
		{
			"CustomerName" : "Jonelle Curtiss",
			"CustomerImage" : "assets/img/profiles/avatar-25.jpg",
			"CustomerNo" : "Supervisor",
			"Created" : "08 Nov 2023, 06:10 am",
			"DeleteRequest": "08 Nov 2023, 06:10 am",
		},
		{
			"CustomerName" : "Jonathan",
			"CustomerImage" : "assets/img/profiles/avatar-26.jpg",
			"CustomerNo" : "Team Lead Dev",
			"Created" : "15 Nov 2023, 11:50 am",
			"DeleteRequest": "15 Nov 2023, 11:50 am",
		},
		{
			"CustomerName" : "Brook",
			"CustomerImage" : "assets/img/profiles/avatar-01.jpg",
			"CustomerNo" : "Team Lead Dev ",
			"Created" : "25 Nov 2023, 06:34 pm",
			"DeleteRequest": "25 Nov 2023, 06:34 pm",
		}
    ]
    return render(request, 'pages/user-management/delete-request.html',{'delete_request' : delete_request })
 
def manage_users(request):
    manage_users = [
        {
			"CustomerName" : "Darlee Robertson",
			"CustomerImage" : "assets/img/profiles/avatar-19.jpg",
			"CustomerNo" : "Facility Manager",
			"Phone" : "1234567890",
			"Email" : "robertson@example.com",
			"Location" : "Germany",
			"Created" : "25 Sep 2023, 12:12 pm",
			"LastActivity": "2 mins ago",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Sharon Roy",
			"CustomerImage" : "assets/img/profiles/avatar-20.jpg",
			"CustomerNo" : "Installer",
			"Phone" : "+1 989757485",
			"Email" : "sharon@example.com",
			"Location" : "USA",
			"Created" : "27 Sep 2023, 07:40 am",
			"LastActivity": "5 mins ago",
			"Status" : "Inactive",
		},
		{
			"CustomerName" : "Vaughan",
			"CustomerImage" : "assets/img/profiles/avatar-21.jpg",
			"CustomerNo" : "Senior  Manager",
			"Phone" : "+1 546555455",
			"Email" : "vaughan12@example.com",
			"Location" : "Canada",
			"Created" : "29 Sep 2023, 08:20 am",
			"LastActivity": "2 days ago",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Jessica",
			"CustomerImage" : "assets/img/profiles/avatar-23.jpg",
			"CustomerNo" : "Test Engineer",
			"Phone" : "+1 454478787",
			"Email" : "jessica13@example.com",
			"Location" : "India",
			"Created" : "25 Sep 2023, 12:12 pm",
			"LastActivity": "2 mins ago",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Carol Thomas",
			"CustomerImage" : "assets/img/profiles/avatar-16.jpg",
			"CustomerNo" : "UI /UX Designer",
			"Phone" : "+1 124547845",
			"Email" : "caroltho3@example.com",
			"Location" : "China",
			"Created" : "02 Oct 2023, 10:10 am",
			"LastActivity": "Online",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Dawn Mercha",
			"CustomerImage" : "assets/img/profiles/avatar-22.jpg",
			"CustomerNo" : "Technician",
			"Phone" : "+1 478845447",
			"Email" : "dawnmercha@example.com",
			"Location" : "Japan",
			"Created" : "17 Oct 2023, 04:25 pm",
			"LastActivity": "3 days ago",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Rachel Hampton",
			"CustomerImage" : "assets/img/profiles/avatar-24.jpg",
			"CustomerNo" : "Software Developer",
			"Phone" : "+1 215544845",
			"Email" : "rachel@example.com",
			"Location" : "Indonesia",
			"Created" : "28 Oct 2023, 07:16 am",
			"LastActivity": "10 days ago",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Jonelle Curtiss",
			"CustomerImage" : "assets/img/profiles/avatar-25.jpg",
			"CustomerNo" : "Supervisor",
			"Phone" : "+1 121145471",
			"Email" : "jonelle@example.com",
			"Location" : "Cuba",
			"Created" : "08 Nov 2023, 06:10 am",
			"LastActivity": "1 week go",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Jonathan",
			"CustomerImage" : "assets/img/profiles/avatar-26.jpg",
			"CustomerNo" : "Team Lead Dev",
			"Phone" : "+1 321454789",
			"Email" : "jonathan@example.com",
			"Location" : "Isreal",
			"Created" : "15 Nov 2023, 11:50 am",
			"LastActivity": "1 day ago",
			"Status" : "Active",
		},
		{
			"CustomerName" : "Brook",
			"CustomerImage" : "assets/img/profiles/avatar-01.jpg",
			"CustomerNo" : "Team Lead Dev ",
			"Phone" : "+1 278907145",
			"Email" : "brook@example.com",
			"Location" : "Colombia",
			"Created" : "25 Nov 2023, 06:34 pm",
			"LastActivity": "8 mins ago",
			"Status" : "Active",
		}
    ]
    return render(request, 'pages/user-management/manage-users.html', {'manage_users' : manage_users})
 

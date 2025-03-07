from django.shortcuts import render

# Create your views here.

def index(request):
    deals_dashboard = [
        {
            "id" : 1,
            "deal_name" : "Collins",
            "stage" : "Conversation",
            "deal_value" : "$04,51,000",
            "probability" : "85%",
            "status" : "Lost"
        },
        {
            "id" : 2,
            "deal_name" : "Konopelski",
            "stage" : "Pipeline",
            "deal_value" : "$14,51,000",
            "probability" : "56%",
            "status" : "Won"
        },
        {
            "id" : 3,
            "deal_name" : "Adams",
            "stage" : "Won",
            "deal_value" : "$12,51,000",
            "probability" : "15%",
            "status" : "Won"
        },
        {
            "id" : 4,
            "deal_name" : "Schumm",
            "stage" : "Lost",
            "deal_value" : "$51,000",
            "probability" : "45%",
            "status" : "Lost"
        },
        {
            "id" : 5,
            "deal_name" : "Wisozk",
            "stage" : "Follow Up",
            "deal_value" : "$67,000",
            "probability" : "5%",
            "status" : "Won"
        }
    ]
    return render(request, 'pages/dashboard/index.html', {'deals_dashboard': deals_dashboard})

def leads_dashboard(request):
    leads_dashboard = [
        {
            "LeadName": "Collins",
            "CompanyName": "NovaWave LLC",
            "Location": "Newyork, USA",
            "Phone": "+1 875455453",
            "Image": "assets/img/icons/company-icon-01.svg",
            "LeadStatus": "Not Contacted"
        },
        {
            "LeadName": "Konopelski",
            "CompanyName": "BlueSky Industries",
            "Location": "Winchester, KY",
            "Phone": "+1 989757485",
            "Image": "assets/img/icons/company-icon-02.svg",
            "LeadStatus": "Contacted"
        },
        {
            "LeadName": "Adams",
            "CompanyName": "SilverHawk",
            "Location": "Jametown, NY",
            "Phone": "+1 546555455",
            "Image": "assets/img/icons/company-icon-03.svg",
            "LeadStatus": "Contacted"
        },
        {
            "LeadName": "Schumm",
            "CompanyName": "SummitPeak",
            "Location": "Compton, RI",
            "Phone": "+1 454478787",
            "Image": "assets/img/icons/company-icon-04.svg",
            "LeadStatus": "Not Contacted"
        }
    ] 
    return render(request, 'pages/dashboard/leads-dashboard.html', {'leads_dashboard': leads_dashboard})

def project_dashboard(request):
    project_dashboard = [
        {
            "Priority": "Truelysell",
            "PriorityImage": "assets/img/priority/truellysel.svg",
            "Name": "NovaWave LLC",
            "Image": "assets/img/icons/company-icon-01.svg",
            "Client": "High",
            "DueDate": "15 Oct 2023"
        },
        {
            "Priority": "Dreamschat",
            "PriorityImage": "assets/img/priority/dreamchat.svg",
            "Name": "BlueSky Industries",
            "Image": "assets/img/icons/company-icon-02.svg",
            "Client": "Medium",
            "DueDate": "22 Oct 2023"
        },
        {
            "Priority": "Truelysell",
            "PriorityImage": "assets/img/priority/truellysell.svg",
            "Name": "SilverHawk",
            "Image": "assets/img/icons/company-icon-03.svg",
            "Client": "High",
            "DueDate": "27 Oct 2023"
        },
        {
            "Priority": "Servbook",
            "PriorityImage": "assets/img/priority/servbook.svg",
            "Name": "SummitPeak",
            "Image": "assets/img/icons/company-icon-04.svg",
            "Client": "High",
            "DueDate": "01 Oct 2023"
        },
        {
            "Priority": "DreamPOS",
            "PriorityImage": "assets/img/priority/dream-pos.svg",
            "Name": "RiverStone Ventur",
            "Image": "assets/img/icons/company-icon-05.svg",
            "Client": "Medium",
            "DueDate": "06 Oct 2023"
        }
    ]
    return render(request, 'pages/dashboard/project-dashboard.html', {'project_dashboard' : project_dashboard })
from django.shortcuts import render
from app.models import PTeam
from app.models import WTB
from app.models import Movie
from app.models import Speaker
from app.models import ClownCanard
from app.models import CodeOClock
# Create your views here.
def home(request):
    return render(request,"home.html")
def pixel(request):
    if request.method == "POST":

        teamName = request.POST.get("teamname")

        leaderName = request.POST.get("leadername")
        leaderRollNo = request.POST.get("leaderrollno")
        leaderEmail = request.POST.get("leaderemail")
        leaderPhoneNumber = request.POST.get("leaderpno")

        teammate1Name = request.POST.get("teammate1name")
        teammate1RollNo = request.POST.get("teammate1rollno")
        teammate1Email = request.POST.get("teammate1email")
        teammate1PhoneNumber = request.POST.get("teammate1pno")

        teammate2Name = request.POST.get("teammate2name")
        teammate2RollNo = request.POST.get("teammate2rollno")
        teammate2Email = request.POST.get("teammate2email")
        teammate2PhoneNumber = request.POST.get("teammate2pno")

        team = PTeam(team_name=teamName, leader_name=leaderName, leader_roll_no=leaderRollNo, leader_thapar_email=leaderEmail,leader_phone_no=leaderPhoneNumber, teammate1_name=teammate1Name, teammate1_roll_no=teammate1RollNo, teammate1_thapar_email=teammate1Email,teammate1_phone_no=teammate1PhoneNumber, teammate2_name=teammate2Name,
                             teammate2_roll_no=teammate2RollNo, teammate2_thapar_email=teammate2Email,teammate2_phone_no=teammate2PhoneNumber)
        team.save()
    return render(request, "pixel.html") 

def sucess(request):

    return render(request,"success.html")

def mn(request):
    if request.method == "POST":


        leaderName = request.POST.get("leadername")
        leaderRollNo = request.POST.get("leaderrollno")
        leaderEmail = request.POST.get("leaderemail")
        leaderPhoneNumber = request.POST.get("leaderpno")


        team = Movie( leader_name=leaderName, leader_roll_no=leaderRollNo, leader_thapar_email=leaderEmail,leader_phone_no=leaderPhoneNumber)
        team.save()
    return render(request,"mn.html")

def speaker(request):
    if request.method == "POST":

        leaderName = request.POST.get("leadername")
        leaderRollNo = request.POST.get("leaderrollno")
        leaderEmail = request.POST.get("leaderemail")
        leaderPhoneNumber = request.POST.get("leaderpno")


        team = Speaker( leader_name=leaderName, leader_roll_no=leaderRollNo, leader_thapar_email=leaderEmail,leader_phone_no=leaderPhoneNumber)
        team.save()


    return render(request,"speaker.html")

def wtb(request):
    if request.method == "POST":

        teamName = request.POST.get("teamname")

        leaderName = request.POST.get("leadername")
        leaderRollNo = request.POST.get("leaderrollno")
        leaderEmail = request.POST.get("leaderemail")
        leaderPhoneNumber = request.POST.get("leaderpno")

        teammate1Name = request.POST.get("teammate1name")
        teammate1RollNo = request.POST.get("teammate1rollno")
        teammate1Email = request.POST.get("teammate1email")
        teammate1PhoneNumber = request.POST.get("teammate1pno")

        teammate2Name = request.POST.get("teammate2name")
        teammate2RollNo = request.POST.get("teammate2rollno")
        teammate2Email = request.POST.get("teammate2email")
        teammate2PhoneNumber = request.POST.get("teammate2pno")

        team = WTB(team_name=teamName, leader_name=leaderName, leader_roll_no=leaderRollNo, leader_thapar_email=leaderEmail,leader_phone_no=leaderPhoneNumber, teammate1_name=teammate1Name, teammate1_roll_no=teammate1RollNo, teammate1_thapar_email=teammate1Email,teammate1_phone_no=teammate1PhoneNumber, teammate2_name=teammate2Name,
                             teammate2_roll_no=teammate2RollNo, teammate2_thapar_email=teammate2Email,teammate2_phone_no=teammate2PhoneNumber)
        team.save()

    return render(request,"wtb.html")

def code(request):
    if request.method == "POST":

        teamName = request.POST.get("teamname")

        leaderName = request.POST.get("leadername")
        leaderRollNo = request.POST.get("leaderrollno")
        leaderEmail = request.POST.get("leaderemail")
        leaderPhoneNumber = request.POST.get("leaderpno")

        teammate1Name = request.POST.get("teammate1name")
        teammate1RollNo = request.POST.get("teammate1rollno")
        teammate1Email = request.POST.get("teammate1email")
        teammate1PhoneNumber = request.POST.get("teammate1pno")


        team = CodeOClock(team_name=teamName, leader_name=leaderName, leader_roll_no=leaderRollNo, leader_thapar_email=leaderEmail,leader_phone_no=leaderPhoneNumber, teammate1_name=teammate1Name, teammate1_roll_no=teammate1RollNo, teammate1_thapar_email=teammate1Email,teammate1_phone_no=teammate1PhoneNumber)
        team.save()

    return render(request,"codeoclock.html")

def cc(request):
    if request.method == "POST":

        teamName = request.POST.get("teamname")

        leaderName = request.POST.get("leadername")
        leaderRollNo = request.POST.get("leaderrollno")
        leaderEmail = request.POST.get("leaderemail")
        leaderPhoneNumber = request.POST.get("leaderpno")

        teammate1Name = request.POST.get("teammate1name")
        teammate1RollNo = request.POST.get("teammate1rollno")
        teammate1Email = request.POST.get("teammate1email")
        teammate1PhoneNumber = request.POST.get("teammate1pno")

        teammate2Name = request.POST.get("teammate2name")
        teammate2RollNo = request.POST.get("teammate2rollno")
        teammate2Email = request.POST.get("teammate2email")
        teammate2PhoneNumber = request.POST.get("teammate2pno")

        team = ClownCanard(team_name=teamName, leader_name=leaderName, leader_roll_no=leaderRollNo, leader_thapar_email=leaderEmail,leader_phone_no=leaderPhoneNumber, teammate1_name=teammate1Name, teammate1_roll_no=teammate1RollNo, teammate1_thapar_email=teammate1Email,teammate1_phone_no=teammate1PhoneNumber, teammate2_name=teammate2Name,
                             teammate2_roll_no=teammate2RollNo, teammate2_thapar_email=teammate2Email,teammate2_phone_no=teammate2PhoneNumber)
        team.save()


    return render(request,"theclowncanard.html")
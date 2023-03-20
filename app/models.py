from django.db import models

# Create your models here.
class WTB(models.Model):
    team_name=models.CharField(max_length=50,default="",null=True, blank=True)
    # Team Leader
    leader_name= models.CharField(max_length=22, blank=False)
    leader_roll_no=models.CharField(max_length=9, blank=False)
    leader_thapar_email=models.CharField(max_length=50, blank=False)
    leader_phone_no=models.CharField(max_length=50, blank=False)

    # Teammate 1
    teammate1_name= models.CharField(max_length=22, default="",null=True, blank=True)
    teammate1_roll_no=models.CharField(max_length=9, default="",null=True, blank=True)
    teammate1_thapar_email=models.CharField(max_length=50,  default="",null=True, blank=True)
    teammate1_phone_no=models.CharField(max_length=50, default="",null=True, blank=True)

    # Teammate 2
    teammate2_name= models.CharField(max_length=22, default="",null=True, blank=True)
    teammate2_roll_no=models.CharField(max_length=9, default="",null=True, blank=True)
    teammate2_thapar_email=models.CharField(max_length=50, default="",null=True, blank=True)
    teammate2_phone_no=models.CharField(max_length=50, default="",null=True, blank=True)


class PTeam(models.Model):
    team_name=models.CharField(max_length=50,default="",null=True, blank=True)
    # Team Leader
    leader_name= models.CharField(max_length=22, blank=False)
    leader_roll_no=models.CharField(max_length=9, blank=False)
    leader_thapar_email=models.CharField(max_length=50, blank=False)
    leader_phone_no=models.CharField(max_length=50, blank=False)

    # Teammate 1
    teammate1_name= models.CharField(max_length=22, default="",null=True, blank=True)
    teammate1_roll_no=models.CharField(max_length=9, default="",null=True, blank=True)
    teammate1_thapar_email=models.CharField(max_length=50,  default="",null=True, blank=True)
    teammate1_phone_no=models.CharField(max_length=50, default="",null=True, blank=True)

    # Teammate 2
    teammate2_name= models.CharField(max_length=22, default="",null=True, blank=True)
    teammate2_roll_no=models.CharField(max_length=9, default="",null=True, blank=True)
    teammate2_thapar_email=models.CharField(max_length=50, default="",null=True, blank=True)
    teammate2_phone_no=models.CharField(max_length=50, default="",null=True, blank=True)

class Movie(models.Model):
    # Person
    leader_name= models.CharField(max_length=22, blank=False)
    leader_roll_no=models.CharField(max_length=9, blank=False)
    leader_thapar_email=models.CharField(max_length=50, blank=False)
    leader_phone_no=models.CharField(max_length=50, blank=False)

class Speaker(models.Model):
    # Person
    leader_name= models.CharField(max_length=22, blank=False)
    leader_roll_no=models.CharField(max_length=9, blank=False)
    leader_thapar_email=models.CharField(max_length=50, blank=False)
    leader_phone_no=models.CharField(max_length=50, blank=False)


class CodeOClock(models.Model):
    team_name=models.CharField(max_length=50,default="",null=True, blank=True)
    # Team Leader
    leader_name= models.CharField(max_length=22, blank=False)
    leader_roll_no=models.CharField(max_length=9, blank=False)
    leader_thapar_email=models.CharField(max_length=50, blank=False)
    leader_phone_no=models.CharField(max_length=50, blank=False)

    # Teammate 1
    teammate1_name= models.CharField(max_length=22, default="",blank=True, null=True)
    teammate1_roll_no=models.CharField(max_length=9, default="",blank=True, null=True)
    teammate1_thapar_email=models.CharField(max_length=50,  default="",blank=True, null=True)
    teammate1_phone_no=models.CharField(max_length=50, default="",blank=True,null=True)

class ClownCanard(models.Model):
    team_name=models.CharField(max_length=50,default="",null=True, blank=True)
    # Team Leader
    leader_name= models.CharField(max_length=22, blank=False)
    leader_roll_no=models.CharField(max_length=9, blank=False)
    leader_thapar_email=models.CharField(max_length=50, blank=False)
    leader_phone_no=models.CharField(max_length=50, blank=False)

    # Teammate 1
    teammate1_name= models.CharField(max_length=22, default="",blank=True, null=True)
    teammate1_roll_no=models.CharField(max_length=9, default="",blank=True, null=True)
    teammate1_thapar_email=models.CharField(max_length=50,  default="",blank=True, null=True)
    teammate1_phone_no=models.CharField(max_length=50,default="", blank=True,null=True)

    # Teammate 2
    teammate2_name= models.CharField(max_length=22, default="",blank=True, null=True)
    teammate2_roll_no=models.CharField(max_length=9, default="",blank=True, null=True)
    teammate2_thapar_email=models.CharField(max_length=50, default="",blank=True, null=True)
    teammate2_phone_no=models.CharField(max_length=50,default="", blank=True,null=True)

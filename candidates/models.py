from django.db import models
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField



Role_choices=(('','None'),('Embedded Software Engineer','Embedded Software Engineer'),
    ('Front End Developer','Front End Developer'),('Full Stack Developer','Full Stack Developer'))
Location_choices=(('','--'),('Montreal','Montreal'),
    ('Toronto','Toronto'),('Vancouver','Vancouver'))

class Role(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


def file_size(value): # add this to some file where you can import it from
    limit = 0.1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 0.5 MB.')

"""
2.5MB - 2621440
5MB - 5242880
10MB - 10485760
20MB - 20971520
50MB - 5242880
100MB - 104857600
250MB - 214958080
500MB - 429916160
"""

"""
Name
Email
Years of Experience
Linked In profile link
Desired incorporated hourly rate
Resume
"""

STATUS_PENDING='Pending'
STATUS_ACCEPTED='Accepted'
STATUS_REJECTED='Rejected'
STATUS_CHOICES=(
    (STATUS_PENDING,'Pending'),
    (STATUS_ACCEPTED,'Accepted'),
    (STATUS_REJECTED,'Rejected'),
)
class Job(models.Model):
    """
Req Id
Job Title
Role
Start Date
End Date
Submission deadline
Location
# Candidates open
Apply Button
    
    """
    

    Req_Id = models.IntegerField()
    Job_title = models.CharField (max_length=255)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    
    Start_date= models.DateField()
    End_date= models.DateField()
    Submission_deadline= models.DateTimeField()
    
    No_Openings= models.IntegerField() 
    Description= RichTextUploadingField(default='') 
    
    def __str__(self):
        return self.Job_title

        
class Candidate(models.Model):
    Name = models.CharField(max_length=100,)
    Email_id = models.CharField(max_length=100,null = True,blank=True)
    Years_of_Experience = models.IntegerField(null = True, blank=True, default=None)
    Linkedin_Profile = models.CharField(max_length=100,null = True)
    Expected_hourly_rate = models.IntegerField(null = True,blank=True,default=None)
    Resume = models.FileField(upload_to='doc', validators=[file_size])
    job=models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    req=models.ForeignKey(Job, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Name
    def Req_Id(self):
        return self.req.Req_Id

class CandidateJobMap(models.Model):
    candidate=models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    status=models.CharField(
        max_length=30,choices=STATUS_CHOICES,default=STATUS_PENDING)
    feedback=models.TextField(blank=True,null=True)

    def Name(self):
        return self.candidate.Name

    def Years_of_Experience(self):
        return self.candidate.Years_of_Experience
    def Email_id(self):
        return self.candidate.Email_id
    
    def Req_Id(self):
        return self.job.Req_Id
    
    def Expected_hourly_rate(self):
        return self.candidate.Expected_hourly_rate


    def __str__(self):
        return "{} - {}".format(self.candidate.Name,self.job.Role)
    class Meta:
        verbose_name_plural = 'All_Candidates'



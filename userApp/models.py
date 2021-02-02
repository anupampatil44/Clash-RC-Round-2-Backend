from django.db import models
from django.contrib.auth.models import User

NO_OF_QUESTIONS = 6


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totalScore = models.IntegerField(default=0)
    email1 = models.EmailField(default='example@gmail.com')
    phone1 = models.CharField(max_length=10)
    name1 = models.CharField(max_length=100)
    junior = models.BooleanField(default=True)       # True if Junior(FE) else False if Senior(SE,TE,BE)
    latestSubTime = models.TimeField(default='00:00')
    timer = models.TimeField(default='00:00')
    choice = models.CharField(max_length=5, default='cpp')       # for the extension the code C or CPP or python
    qid = models.IntegerField(default=0)                         # will store the current question id
    flag = models.BooleanField(default=False)                    # Flag for instruction Page
    lang = models.CharField(max_length=3,default='cpp')
    correctly_solved = models.IntegerField(default=0) # will store the current question lang
    attempted=models.IntegerField(default=0)
    cheatcounter=models.IntegerField(default=3)
    def __str__(self):
        return self.user.username


class Question(models.Model):
    titleQue = models.CharField(max_length=50)
    question = models.CharField(max_length=5000)
    totalSub = models.IntegerField(default=0)
    totalSuccessfulSub = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    constraints = models.TextField(default="NA")
    explanation = models.TextField(default="NA")
    iformat = models.TextField(default="NA")
    oformat = models.TextField(default="NA")
    sampleInput = models.TextField(default="NA")
    sampleOutput = models.TextField(default="NA")

    # accuracy = total Successful submission / total Submission

    def __str__(self):
            return self.titleQue + '-' + self.question

    def IDNumber(self):
        return self.pk


class MultipleQues(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    que = models.ForeignKey(Question, on_delete=models.CASCADE)
    scoreQuestion = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    que = models.ForeignKey(Question, on_delete=models.CASCADE)
    qid=models.IntegerField(default=1)
    code = models.CharField(max_length=1000)
    attempt = models.IntegerField(default=0)                       # Current Attempt
    out = models.IntegerField(default=0)
    subStatus = models.CharField(default='NA', max_length=5)     # four type of submission status(WA, PASS, TLE, CTE)
    subTime = models.CharField(default='', max_length=50)
    subScore = models.IntegerField(default=0)
    correctTestCases = models.IntegerField(default=0)
    TestCasesPercentage = models.IntegerField(default=0)
    # (TestCasesPercentage = correctTestCases / NO_OF_QUESTIONS) * 100

    def __str__(self):
            return self.user.username + ' - ' + self.que.titleQue

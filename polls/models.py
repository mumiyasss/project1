from django.db import models

class polls(models.Model):
    question = models.CharField(max_length=300)
    def publish(self):
        self.save()

    def __str__(self):
        return self.question


class answers(models.Model):
    currentPoll = models.ForeignKey(polls, on_delete=models.CASCADE, null=True)
    answer      = models.CharField(max_length=200)
    rate        = models.IntegerField(default=0)

    def rateInc(self):
        self.rate = rate + 1;

    def rateDec(self):
        self.rate = self.rate - 1;

    def publish(self):
        if self.currentPoll:
            self.save()

    def __str__(self):
        return self.answer
from django.db import models

class polls(models.Model):
    question = models.CharField(max_length=300)
    variantsOfAnswer = {}
    answerPolls = {}
    ids = 0;

    def edit_quetion(self, text):
        self.question = text

    def add_new_variant(self, question):
        self.ids = ids + 1
        self.variantsOfAnswer[ids] = question;

    def vote(self, forWhat):
        self.answerPolls[forWhat] = self.answerPolls[forWhat] + 1

    def publish(self):
        for position in ids:
            self.answerPolls[position] = 0

        self.save()




from django.db import models
import random

class Pet(models.Model):
    objects = None
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=1)
    fullness = models.IntegerField(default=40)
    happiness = models.IntegerField(default=40)
    is_resting = models.BooleanField(default=False)

    def feed(self):
        if not self.is_resting:
            self.fullness += 15
            self.happiness += 5
            if self.fullness > 100:
                self.happiness -= 30
        self.save()

    def play(self):
        if self.is_resting:
            self.is_resting = False
            self.happiness -= 5
        else:
            self.happiness += 15
            self.fullness -= 10
            if random.randint(1, 3) == 1:
                self.happiness = 0
        self.save()

    def rest(self):
        self.is_resting = True
        self.save()

    def get_image(self):
        if self.happiness > 70:
            return 'images/happy_cat.jpg'
        elif self.happiness > 30:
            return 'images/neutral_cat.jpeg'
        else:
            return 'images/sad_cat.jpg'

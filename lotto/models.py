from django.db import models
from django.utils import timezone
import random

# Create your models here.
# http://j.mp/2NBbpWU (ModelFields)
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) #로또 번호 리스트 이름
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = "" #빈 str 만들기
        origin = list(range(1, 46))

        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self): # Admin page에서 display 되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) #pk는 자동생성

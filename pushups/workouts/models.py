from django.db import models


#Each workout will hold a datetime field, user name, and number of pushups
class Workout(models.Model):
    user_name = models.CharField(max_length=100)
    workout_date = models.DateTimeField('Time and date of workout')
    pushup_count = models.IntegerField('Number of pushups completed')
    def __unicode__(self):
        return self.user_name + "-"+str(self.pushup_count)
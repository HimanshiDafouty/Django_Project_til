from django.db import models

# Create your models here.

  # Post(models.Model): Creates a database table named Post.
class Post(models.Model): 
  
    # Adds a column text to the table, storing short text up to 240 characters.
    text = models.CharField(max_length=240)
    
    # Adds a column 'date' that automatically updates to the current datetime every time the model is saved.
    date = models.DateTimeField(auto_now = True)
    
    # __str__: This is used to define how your object will appear in the Django admin and shell. It'll show the actual post text instead of something like Post object (1).
    def __str__(self):
        return self.text

from django.db.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver  

class Base(Model):
    """Base model for all of the models in the app. """
    class Meta:
            abstract = True
                    
    created     = DateTimeField(auto_now_add=True, editable=False)
    updated     = DateTimeField(auto_now=True, editable=False)
    is_active   = BooleanField(default=1)        
        
    def __unicode__ (self):
        if hasattr(self, "title") and self.title:
            return self.title
        else:
            return "%s" % (type(self))


class Response(Base):
    """Stores values of a single response to the question posted on the site """

    dream   = FloatField(default= 2.0)
    make    = FloatField(default= 2.0)
    learn   = FloatField(default= 2.0)
    teach   = FloatField(default= 2.0)
    rest    = FloatField(default= 2.0)
    taste   = FloatField(default= 2.0)
    play    = FloatField(default= 2.0)
    earn    = FloatField(default= 2.0)
    spend   = FloatField(default= 2.0)
    connect = FloatField(default= 2.0)
    move    = FloatField(default= 2.0)
    help    = FloatField(default= 2.0)
    sent_by = IPAddressField(null=True, blank=True)

    def __unicode__(self):
        return "%s response" % self.sent_by


@receiver(post_save, sender=Response)
def email_response(sender, **kwargs):
    # format values in an email and send to the knitters
    pass
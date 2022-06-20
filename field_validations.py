from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import pytz
import datetime

utc = pytz.UTC

def validate_bookingfrom(value):
    now = datetime.datetime.now()
    if value + datetime.timedelta(seconds=60) < utc.localize(now):
        raise ValidationError(_("You can't book for dates in the past. \nKindly check your date."))
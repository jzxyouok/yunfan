from django import template
from django.db import models

from info.models import Information 
register = template.Library()


# Expose RelationshipManager functionality as template filters.




# Comparing two users.

@register.filter
def viewed(from_user, info_id):
    """Returns ``True`` if the first user follows the second, ``False`` otherwise.  Example: {% if user|follows:person %}{% endif %}"""
    try:
        info = Information.objects.get(id=int(info_id))
        user_viewed = from_user.viewers.all()
        #nice!!
        if info in user_viewed:
            return True
        else:
            return False
    except AttributeError:
        return False

@register.filter
def get_relationship(from_user, to_user):
    """Get relationship between two users."""
    try:
        return Relationship.objects.get_relationship(from_user, to_user)
    except AttributeError:
        return None

# get_relationship templatetag.

class GetRelationship(template.Node):
    def __init__(self, from_user, to_user, varname='relationship'):
        self.from_user = from_user
        self.to_user = to_user
        self.varname = varname

    def render(self, context):
        from_user = template.resolve_variable(self.from_user, context)
        to_user = template.resolve_variable(self.to_user, context)

        relationship = Relationship.objects.get_relationship(from_user, to_user)
        context[self.varname] = relationship

        return ''


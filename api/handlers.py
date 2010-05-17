from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from blogserver.blog.models import Blogpost

class BlogpostHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    model = Blogpost
    
    def read(self, request): # title=None):
        print "read ", attrs
        base = Blogpost.objects
        
        if title:
            return base.get(title=title)
        else:
            return base.all()
    
    def create(self, request):
        """ Creates a new blogpost.  """
        attrs = self.flatten_dict(request.POST)
        print "CREATE ", attrs, request.user
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            post = Blogpost(title=attrs['title'], content=attrs['content'], author=request.user)
            post.save()
        return post
 

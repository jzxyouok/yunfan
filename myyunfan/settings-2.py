



#use for static and media
import os
HERE = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join( HERE, "../media").replace('\\', '/')
MEDIA_URL = "/site_media/"

STATIC_ROOT = os.path.join(HERE, "../static").replace('\\', '/')
STATIC_URL = "/static/"

STATICFILES_DIRS = ( os.path.join(HERE, "../app名字/static/").replace('\\', '/'), )  #和STATIC_ROOT最好路径不要重叠
#建议将静态文件保存在app的static目录中

#urls.py中加入：

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#这样使用
<link  type="text/css"  rel="stylesheet" href="/static/css/bootstrap.min.css"/> 
        <link  type="text/css"  rel="stylesheet" href="/static/css/bootstrap-responsive.css"/> 
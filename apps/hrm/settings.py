app_name="hrm"
rel_login_url="login"
import os
host_dir= ""
def on_authenticate(sender):
    from django.contrib.auth import get_user_model
    model = get_user_model().objects
    if model.filter(username="root").count() == 0:
        rootUser=model.create_superuser("root","123456","root@xjd.com")
        rootUser.is_active =True
        rootUser.save()


    user = sender.request.user

    if sender.request.user.is_anonymous.value:
        return False
    return True
def on_get_language_resource_item(language,appname,view,key,value):
    return value
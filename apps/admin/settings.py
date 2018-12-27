app_name="admin"
host_dir="admin"
def on_authenticate(sender):
    return False
def on_get_language_resource_item(language,appname,view,key,value):
    return value
rel_login_url="login"
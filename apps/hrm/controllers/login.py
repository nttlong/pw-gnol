"""
The controller serve for Login
"""
import xdj
@xdj.Controller(
    url="login",
    template="login.html"
)
class LoginController(xdj.BaseController):
    def on_get(self,model):
        if isinstance(model,xdj.Model):
            return self.render(model)

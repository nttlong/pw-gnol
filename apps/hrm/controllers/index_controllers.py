#!/usr/bin/python
# -*- coding: utf-8 -*
import xdj
@xdj.Controller(
    url="",
    template="index.html"
)
class IndexController(xdj.BaseController):
    def on_get(self,sender):
        return self.render(sender)
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import jinja2
import webapp2

# Set up jinja environment

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("Home.html", items = items)

class Stage_0_Handler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("Stage_0_Notes.html", items = items)

class Stage_1_Handler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("Stage_1_Notes.html", items = items)

class Stage_2_Handler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("Stage_2_Notes.html", items = items)

class Stage_3_Handler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("Stage_3_Notes.html", items = items)

class Stage_4_Handler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("Stage_4_Notes.html", items = items)

class About_Handler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("About.html", items = items)        

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/Stage0', Stage_0_Handler),
                               ('/Stage1', Stage_1_Handler),
                               ('/Stage2', Stage_2_Handler),
                               ('/Stage3', Stage_3_Handler),
                               ('/Stage4', Stage_4_Handler),
                               ('/about', About_Handler),
                               ],
                               debug=True)

# -*- coding: utf-8 -*-
"""
    My First Pastebin
    
    My First Pastebin is a simple pastebin for the
    Google App Engine, running on the Webapp framework.
    
    Copyright 2010 Bjørn Tore Håvie
"""
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name

from models import Paste
import b64

langs = sorted([{'name': l[0], 'id': l[1][0]} for l in get_all_lexers()], key=lambda x: x['name'])

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template.render("index.html",
                                                {'langs': langs}))
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        content = self.request.POST.get('content', '')
        lang = self.request.POST.get('type', 'None')
        paste = Paste(content=content, type=lang)
        paste.put()
        self.redirect('/' + b64.num_encode(paste.key().id()))

class PastePage(webapp.RequestHandler):
    def get(self, paste_id):
        try:
            aid = b64.num_decode(paste_id)
            paste = Paste.get_by_id(aid)
            content, lang = paste.content, paste.type
            formatter = HtmlFormatter()
            self.response.out.write(template.render("paste.html", {'css': formatter.get_style_defs('.highlight'),
                                                                   'paste': highlight(content, get_lexer_by_name(lang), formatter)}))
        except Exception:
            self.response.set_status(404)
            self.response.out.write(template.render("404.html", {}))

application = webapp.WSGIApplication([('/', MainPage), ('/(.+)', PastePage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class CapitalOf():
    def __init__(self, country, capital, img_url):
        self.country = country
        self.capital = capital
        self.img_url = img_url

    def return_data(self):
        dict = {'country': self.country, 'capital' : self.capital, 'img_url': self.img_url}
        return dict

country0 = CapitalOf('Slovenija', 'ljubljana', 'assets/img/ljubljana.jpg')
country1 = CapitalOf('Avstrija', 'dunaj', 'assets/img/dunaj.jpg')
country2 = CapitalOf('Nizozemska', 'amsterdam', 'assets/img/amsterdam.jpg')
country3 = CapitalOf('Grcija', 'atene', 'assets/img/atene.jpg')

country_list = [country0, country1, country2, country3]

class CapitalHandler(BaseHandler):
    def get(self):
        selected = random.randint(0, (len(country_list) - 1))
        params = country_list[selected].return_data()
        return self.render_template("first.html", params=params)
    def post(self):
        capital = self.request.get('odgovor')
        country = self.request.get('country')
        params = {'rezultat' : 'Ni podatka'}
        for c in country_list:
            if country == c.return_data()['country']:
                if capital.lower() == c.return_data()['capital']:
                    params = {'rezultat': 'Bravo! ' + capital.title() + ' je glavno mesto drzave: ' + country}
                else:
                    params = {'rezultat': 'A-a. Nimas prav. Poizkusi ponovno...'}
        return self.render_template("first.html", params=params)


def init_dna():
    hair_list = [('Black', 'CCAGCAATCGC'), ('Brown', 'GCCAGTGCCG'), ('Blonde', 'TTAGCTATCGC')]
    face_list = [('Square', 'GCCACGG'), ('Round', 'ACCACAA'), ('Oval', 'AGGCCTCA')]
    eye_list = [('Blue', 'TTGTGGTGGC'), ('Green', 'GGGAGGTGGC'), ('Brown', 'AAGTAGTGAC')]
    gender_list = [('Female', 'TGAAGGACCTTC'), ('Male', 'TGCAGGAACTTC')]
    race_list = [('White', 'AAAACCTCA'), ('Black', 'CGACTACAG'), ('Asian', 'CGCGGGCCG')]

    return [hair_list, face_list, eye_list, gender_list, race_list]


def search_suspect(dna):
    dna_record = init_dna()
    dna_suspect = []
    for dna_part in dna_record:
        for prop in dna_part:
            if prop[1] in dna:
                dna_suspect.append(prop[0])
    return dna_suspect

class ForensicsHandler(BaseHandler):
    def get(self):
        return self.render_template("forensics.html")
    def post(self):
        dna = self.request.get('dna')
        dna_test = search_suspect(dna)

        params = {'result': dna_test}
        return self.render_template("forensics.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/guess_capital', CapitalHandler),
    webapp2.Route('/forensics', ForensicsHandler),
], debug=True)


import webapp2
import jinja2
import os
import datetime

jinja_environment = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('/templates/index.html')
        self.response.out.write(template.render(template_values))
		
class OutputHandler1(webapp2.RequestHandler):
    def post(self):
        date1 = self.request.get("date1")
        date1 = date1.split("-")
        date1[0] = int(date1[0])
        date1[1] = int(date1[1])
        date1[2] = int(date1[2])
        date1 = datetime.date(year=date1[0], month=date1[1], day=date1[2])

        date2 = self.request.get("date2")
        date2 = date2.split("-")
        date2[0] = int(date2[0])
        date2[1] = int(date2[1])
        date2[2] = int(date2[2])
        date2 = datetime.date(year=date2[0], month=date2[1], day=date2[2])

        diffd = date2 - date1
        diff1 = abs(diffd.days)

        time1 = self.request.get("time1")
        t1 = time1.split(":")
        t1[0] = int(t1[0])
        t1[1] = int(t1[1])
        t1 = datetime.timedelta(hours=t1[0], minutes=t1[1])

        time2 = self.request.get("time2")
        t2 = time2.split(":")
        t2[0] = int(t2[0])
        t2[1] = int(t2[1])
        t2 = datetime.timedelta(hours=t2[0], minutes=t2[1])

        if t2 > t1:
            difft = t2 - t1
        else:
            difft = t1 - t2

        diff2 = abs(difft.seconds / 60)

        template_values2 = {'date1': date1, 'date2': date2, 'diff2': diff1, 'time1': time1, 'time2': time2, 't1': t1, 't2': t2, 'diff1': diff2}
        template = jinja_environment.get_template('/templates/output.html')
        self.response.out.write(template.render(template_values2))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/output2', OutputHandler1)
], debug=True)

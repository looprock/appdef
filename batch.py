"""This is where the magic happens."""
import jinja2
import helpers

templateloader = jinja2.FileSystemLoader(searchpath="./templates")
templateenv = jinja2.Environment(loader=templateloader)


def testfunc(appdef):
    """A test."""
    # config 1
    template = templateenv.get_template("test.tmpl")
    helpers.writeconf('./test1.conf', template.render(appdef))
    # config 2
    template = templateenv.get_template("test2.tmpl")
    helpers.writeconf('./test2.conf', template.render(appdef))

from bottle import *
import urllib.request, json

@route("/")
def index():
    return  """
    <h2>verkefni 3</h2>
    <p><a href="/a">Json local</a></p>
    <p><a href="/b">Json af Api.is</a></p>
"""
@route("/a")
def index():
    return template("index.tpl")


with urllib.request.urlopen("http://api.is/currency/") as url:
    data = json.loads(url.read().decode())

@route("/b")
def index():
    return template("index2.tpl", data=data)

#####################################################
@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root='./static')

@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða fannst ekki</h2>"

run(host='localhost',port=8080, reloader=True, debug=True)



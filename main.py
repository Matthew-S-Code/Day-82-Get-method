from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  return "type '/language' in the url then a '?' then 'lang=eng' or 'lang=ger'"

@app.route("/language")
def language():
  get = request.args
  if get == {}:
    return "No Data"
  if get["lang"].lower() == "eng":
    return "Hello this website is displaying in english"
  elif get["lang"].lower()=="ger":
    return "Hallo, diese Website wird auf Englisch angezeigt."
  

app.run(host='0.0.0.0', port=81)

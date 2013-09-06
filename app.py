from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
 return render_template("index.html")

if __name__ == "__main__":
  app.debug = True
  app.run()


# GOOGLE MAPS API KEY (goes in the url): key=AIzaSyAQpM8R-OLTmRM30bkfm1NOYyFiFSvn7kY
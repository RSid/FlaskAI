from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

@app.route('/')
def index():
    template = env.get_template('index.html')
    return template.render(username='Alla')

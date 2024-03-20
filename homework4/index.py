from flask import render_template
from flask.views import MethodView
import gbmodel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = model.select()
        return render_template('index.html', entries=entries)

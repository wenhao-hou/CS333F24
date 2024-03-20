from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['description'], request.form['street_address'], 
                     request.form['type_of_service'], request.form['phone_number'], 
                     request.form['hours_of_operation'], request.form['reviews'])
        return redirect(url_for('index'))

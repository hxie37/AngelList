"""
    :author: Hanjie Xie
    :date: 3/38/2021
    :description: This project is a take home assignment from AngelList
"""
from datetime import datetime
import json
import os
from flask import Flask, render_template, request, jsonify
import json
import os
app = Flask(__name__)

from allocation_proration.models import Investor, Proration
from allocation_proration import app

@app.route('/', methods = ['GET', 'POST'])
def index():
    """
    process request from web app
    :return:
    """
    if request.method == 'POST':
        investors = []
        js_in = {}
        if request.form.get('name1') and request.form.get('req1') and request.form.get('avg1'):
            investor1 = Investor(request.form.get('name1'), float(request.form.get('req1')), float(request.form.get('avg1')))
            investors.append(investor1)
        if request.form.get('name2') and request.form.get('req2') and request.form.get('avg2'):
            investor2 = Investor(request.form.get('name2'), float(request.form.get('req2')), float(request.form.get('avg2')))
            investors.append(investor2)
        if request.form.get('name3') and request.form.get('req3') and request.form.get('avg3'):
            investor3 = Investor(request.form.get('name3'), float(request.form.get('req3')), float(request.form.get('avg3')))
            investors.append(investor3)
        if request.form.get('allocation_amount') and investors:
            proration = Proration(investors, float(request.form.get('allocation_amount')))
            res = proration.real_allocation()
            js_in['investor_amounts'] = proration.get_list()
            js_in['allocation_amount'] = float(request.form.get('allocation_amount'))
            log(js_in, 1)
            log(res, 0)
            return render_template('index.html', res = res)
    return render_template('index.html')


def log(js : dict, input):
    """
    store log json file
    :param js:
    :param input:
    :return:
    """
    now = datetime.now()
    if input:
        fn = 'input_' + str(now) + '.json'
    else:
        fn = 'output_' + str(now) + '.json'
    completeFn = os.path.join(os.getcwd(), 'allocation_proration', 'log', fn)
    with open(completeFn, 'w') as of:
        json.dump(js, of, indent = 2)
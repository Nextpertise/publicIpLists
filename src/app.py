#!/usr/bin/python3

import requests
import flask
from flask import request, jsonify, abort

app = flask.Flask(__name__)
app.config["DEBUG"] = False

class providers:
    def provider_atlassian(self, ipv):
        cidr_ipv4 = []
        cidr_ipv6 = []

        url = 'https://ip-ranges.atlassian.com/'
        resp = requests.get(url=url)
        data = resp.json()
        for i in data['items']:
            if(':' in i['cidr']):
                cidr_ipv6.append(i['cidr'])
            else:
                cidr_ipv4.append(i['cidr'])

        if(ipv == 'ipv4'):
            return cidr_ipv4 
        if(ipv == 'ipv6'):
            return cidr_ipv6 
        abort(404)

def format(cidr_list):
    if('json' in request.headers.get('accept')):
        return jsonify(cidr_list)
    return '\n'.join(cidr_list)

@app.route('/<provider>/<ipv>', methods=['GET'])
def provider(provider, ipv):
    providerObj = providers()
    provider_name = 'provider_{}'.format(provider)
    if provider_name in dir(providerObj):
        provider_method = getattr(providerObj, provider_name)
        return format(provider_method(ipv))
    else:
        abort(404)

app.run(host='0.0.0.0')

from flask import request

@app.route('/landingpage')
def landing_page():
    id = request.args['id']
    ...

# /landingpage?id=A
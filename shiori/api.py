"""
API


GET /links
    Return the list of links

POST /links
    Insert new link(s)

GET /link/<id>
    Get a specific link

PUT /link/<id>
    Change data about a specific link


"""


from flask import Flask, jsonify, request
from shiori.config import DB

api = Flask(__name__)


@api.route("/links", methods=["GET", "POST"])
def api_links():
    """
    Create or list links
    """
    if request.method == "GET":
        links = DB["links"].find()
        return jsonify(list(links))
    else:
        # Todo: Take this request handling out of the api main loop
        req = request.get_json()
        links = req["links"]
        for link in links:
            DB["links"].insert_one({
                "url":link,
                "_id": hash(link)
                })
        return jsonify({'success':True}), 200


@api.route("/link/<lid>")
def api_link(lid):
    """
    Operate on a single link
    
    :param str lid: Link id
    """
    pass

def run_api():
    api.run(debug=True)
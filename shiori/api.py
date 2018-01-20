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


from flask import Flask, jsonify
from shiori.config import DB

api = Flask(__name__)


@api.route("/links", methods=["GET", "POST"])
def api_links():
    """
    Create or list links
    """
    links = DB["links"].find()
    return jsonify(list(links))

@api.route("/link/<lid>")
def api_link(lid):
    """
    Operate on a single link
    
    :param str lid: Link id
    """
    pass

def run_api():
    api.run(debug=True)
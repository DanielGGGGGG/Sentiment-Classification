import falcon

# from .images import Resource
from .sentiment import Resource


api = application = falcon.API()

sentiment = Resource()
api.add_route('/sentiment', sentiment)

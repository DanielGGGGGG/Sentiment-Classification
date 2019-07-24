import falcon

# from .images import Resource
from .sentiment import SentimentPredict

api = application = falcon.API()

sentimentPredictResource = SentimentPredict()

api.add_route('/sentiment', sentimentPredictResource) 
from flask import Blueprint , request

from schema.apartments import Apartments

from services.model_inference import ModelInferenceService

bp  = Blueprint('prediction', __name__ , url_prefix = '/pred')



@bp.get('/')
def get_predictions():
    # get and check input params of apartment 
    apartment_features = Apartments(**request.args)

    # load an existing model
    Model_inference = ModelInferenceService()
    Model_inference.load_model()

    # feed the model with input params 

    prediction = Model_inference.predict(list(apartment_features.model_dump().values()))

    # return a prediction score 
    return {'prediction': prediction}


@bp.post('/')
def get_predictions_post():
    # get and check input params of apartment 
    apartment_features = Apartments(**request.json)

    # load an existing model
    Model_inference = ModelInferenceService()
    Model_inference.load_model()

    # feed the model with input params 

    prediction = Model_inference.predict(list(apartment_features.model_dump().values()))

    # return a prediction score 
    return {'prediction': prediction}
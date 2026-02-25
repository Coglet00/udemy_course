"""
This module provides functionality for managing a ML model.

It contains the ModelService class, which handles loading and using
a pre-trained ML model. The class offers methods to load a model
from a file, building it if it doesn't exist, and to make predictions
using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings



class ModelInferenceService:
    """
    A service class for managing the ML model.

    This class provides functionalities to load a ML model from
    a specified path, build it if it doesn't exist, and make
    predictions using the loaded model.

    Attributes:
        model: ML model inference managed by this service. Initially set to None.

    Methods:
        __init__: Constructor that initializes the ModelService.
        load_model: Loads the model from file or builds it if it doesn't exist.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelService with no model loaded."""
        self.model = None
        self.model_path = model_settings.model_path
        self.model_name = model_settings.ml_model

    def load_model(self) -> None:
        """Load the model from a specified path, or builds it if not exist."""
        logger.info(
            f'checking the existance of model config file at '
            f'{self.model_path}/{self.model_name}',
        )

        model_path = Path(
            f'{self.model_path}/{self.model_name}'
        )

        if not model_path.exists():
            raise FileNotFoundError("Model file does not exist")
            

        logger.info(
            f'model {self.model_path} exists! -> '
            'loading model configuration file',
        )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using the loaded model.

        Takes input parameters and passes it to the model, which
        was loaded using a pickle file.

        Args:
            input_parameters (list): The input data for making a prediction.

        Returns:
            list: The prediction result from the model.
        """
        logger.info('making prediction!')
        return self.model.predict([input_parameters])


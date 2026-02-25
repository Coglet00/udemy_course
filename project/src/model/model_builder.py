"""
This module provides functionality for managing a ML model.

It contains the Model builder service which trains and saves the model. 
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelBuilderService:
    """
    A service class for building and saving the ML model.

    This class provides functionalities to load a ML model from
    a specified path, build it if it doesn't exist, and make
    predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.

    Methods:
        __init__: Constructor that initializes the ModelService.
        load_model: Loads the model from file or builds it if it doesn't exist.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelBuilderService with no model loaded."""
        self.model_path = model_settings.model_path
        self.ml_model =  model_settings.ml_model

    def train_model(self) -> None:
        """Load the model from a specified path, or builds it if not exist."""
        logger.info(
            f'checking the existance of model config file at '
            f'{self.model_path}/{self.ml_model}',
        )

       
        build_model()



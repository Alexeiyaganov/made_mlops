from dataclasses import dataclass

from .mlflow_params import MlFlowParams
from .data_params import SplittingParams
from .feature_params import FeatureParams
from .model_params import TrainingParams
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class TrainingPipelineParams:
    input_data_path: str
    output_model_path: str
    metric_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams
    ml_flow_params: MlFlowParams


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    with open(path, "r") as file:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(file))
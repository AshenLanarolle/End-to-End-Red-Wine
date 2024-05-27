from Wineproject import logger
from Wineproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wineproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Wineproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    Data_ingestion = DataIngestionTrainingPipeline()
    Data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_Transformation = DataTransformationTrainingPipeline()
    data_Transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
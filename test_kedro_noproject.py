from kedro.io import DataCatalog, MemoryDataSet
from kedro.runner import ThreadRunner

from src.test_kedro_mp.pipelines.test_pipe.pipeline import create_pipeline

# Prepare a data catalog
data_catalog = DataCatalog({"mock_input": MemoryDataSet()})


def run():
    pipeline = create_pipeline()
    runner = ThreadRunner()
    runner.run(pipeline, data_catalog)
    pass


if __name__ == "__main__":
    run()

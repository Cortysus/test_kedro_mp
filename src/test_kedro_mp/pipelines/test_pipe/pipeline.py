from kedro.pipeline import Pipeline, node
from .nodes import test_mp


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=test_mp,
                inputs=None,
                outputs="my_test",
            ),
        ]
    )

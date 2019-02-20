from wordcounter.core.pipeline.utils import pipeline_composer


def test_pipeline_composer():
    fnx = pipeline_composer(*[lambda x: x * 2, lambda x: x - 1])
    assert fnx([1, 2, 3] == [1, 3, 5])

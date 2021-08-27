from dagster import ModeDefinition, pipeline

from iris.solids.cluster import create_df, normalize_df, pca_df, sse_plot

# Mode definitions allow you to configure the behavior of your pipelines and solids at execution
# time. For hints on creating modes in Dagster, see our documentation overview on Modes and
# Resources: https://docs.dagster.io/overview/modes-resources-presets/modes-resources
MODE_PROD = ModeDefinition(name="prod", resource_defs={})
MODE_TEST = ModeDefinition(name="test", resource_defs={})


@pipeline(mode_defs=[MODE_PROD, MODE_TEST])
def my_pipeline():
    sse_plot(pca_df(normalize_df(create_df())))

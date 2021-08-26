from dagster import repository

from iris.pipelines.my_pipeline import my_pipeline
from iris.schedules.my_hourly_schedule import my_hourly_schedule
from iris.sensors.my_sensor import my_sensor


@repository
def iris():
    """
    The repository definition for this iris Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [my_pipeline]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return pipelines + schedules + sensors

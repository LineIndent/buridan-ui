from ...wrappers.base import base
from ...charts.exports import exports_config


def get_exports(directory):
    return [export() for export in exports_config[directory]]


@base("/charts/bar-charts", "Bar Charts", title="Bar Charts - buridan/ui")
def bar_charts():
    return get_exports("bar")


@base("/charts/area-charts", "Area Charts", title="Area Charts - buridan/ui")
def area_charts():
    return get_exports("area")

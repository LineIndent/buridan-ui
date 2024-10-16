from ...wrappers.base import base
from ...charts.exports import exports_config


def get_exports(directory):
    return [export() for export in exports_config[directory]]


@base("/charts/bar-charts", "Bar Charts", title="Bar Charts - buridan/ui")
def subscribe():
    return get_exports("bar")

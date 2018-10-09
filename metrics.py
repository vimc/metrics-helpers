from flask import Response
from dateutil import parser
from datetime import datetime

def render_value(value):
    if value is True:
        return 1
    elif value is False:
        return 0
    else:
        return value


def render_metrics(metrics):
    output = ""
    for k, v in metrics.items():
        output += "{k} {v}\n".format(k=k, v=render_value(v))
    return Response(output, mimetype='text/plain')


def label_metrics(metrics, labels):
    label_items = ",".join('{k}="{v}"'.format(k=k, v=v) for k, v in labels.items())
    label = "{" + label_items + "}"

    labelled = {}
    for k, v in metrics.items():
        labelled[k + label] = v
    return labelled


def seconds_elapsed_since(timestamp):
    if timestamp:
        now = datetime.now().timestamp()
        return (now - timestamp).total_seconds()
    else:
        return None


def parse_timestamp(raw):
    if raw and raw != "None":
        return parser.parse(raw)
    else:
        return None

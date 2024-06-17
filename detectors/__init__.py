import inspect
from slither.detectors.abstract_detector import AbstractDetector
from .all_detectors import *


def make_plugin():

    detectors = [getattr(all_detectors, name) for name in dir(all_detectors)]
    detectors = [d for d in detectors if inspect.isclass(d) and issubclass(d, AbstractDetector)]

    printers = []

    return detectors, printers
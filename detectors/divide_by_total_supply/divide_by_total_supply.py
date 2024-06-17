from typing import List

from slither.detectors.abstract_detector import (
    AbstractDetector,
    DetectorClassification,
    DETECTOR_INFO,
)
from slither.utils.output import Output


class DivideByTotalSupply(AbstractDetector):
    """
    <Documentation>
    """

    ARGUMENT = "divide-by-total-supply" 
    HELP = "Divide by total suppy"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = "https://github.com/crytic/slither/wiki/Adding-a-new-detector"
    WIKI_TITLE = "Example"
    WIKI_DESCRIPTION = "Plugin example"
    WIKI_EXPLOIT_SCENARIO = ".."
    WIKI_RECOMMENDATION = ".."

    def _detect(self) -> List[Output]:
        results: List[Output] = []

        # implement logic
        for contract in self.compilation_unit.contracts_derived:
            pass

        return results
# Add your detectors here
from .copy_propagation.copy_propagation import CopyPropagation
from .divide_by_total_supply.divide_by_total_supply import DivideByTotalSupply
from .iscontract.iscontract import IsContract
from .mul_reduction.mul_reduction import MulReduction
from .read_only_reentrancy.read_only_reentrancy import ReadOnlyReentrancy
from .storage_read_elimiation.storage_read import StorageRead
from .unused_event.unused_event import UnusedEvent

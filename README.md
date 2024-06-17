# Slither secureum workshop

The goals of this workshop are to:
- Learn about Slither's API
- Write your first detectors
- Experiment with writing new detectors rules
- Experiment with how to evaluate static analyzers

## Detector list

For each detector:
- Use the `example.sol` file in the `evaluation/NAME` directory
- Create more test cases, and try your detector on various codebases
- Highlight any edge-case that is properly detected by your detector in its documentation

| ID  | Name                 | What it detects                             | Examples                                                |
|-----|----------------------|---------------------------------------------|---------------------------------------------------------|
| 0   | [unused-event](./detectors/unused_event/unused_event.py)         | Events that are not used                    | [example.sol](./evaluation/unused_event/example.sol)     |
| 1   | [isContract](./detectors/iscontract/iscontract.py)           | Incorrect isContract function/modifier      | [example.sol](./evaluation/iscontract/example.sol)       |
| 2   | [divide-by-total-supply](./detectors/divide_by_total_supply/divide_by_total_supply.py) | Division by the total supply                | [example.sol](./evaluation/divide_by_total_supply/example.sol) |
| 3   | [storage-read](./detectors/storage_read_elimiation/storage_read.py)         | Unnecessary storage read                    | [example.sol](./evaluation/storage_read_eliminination/example.sol) |
| 4   | [mul-reduction](./detectors/mul_reduction/mul_reduction.py)        | Mul can be replaced by add                  | [example.sol](./evaluation/mul_reduction/example.sol)    |
| 5   | [copy-propagation](./detectors/copy_propagation/copy_propagation.py)     | Costly operations can be replaced           | [example.sol](./evaluation/copy_propagation/example.sol) |
| 6   | [read-only-reentrancy](./detectors/read_only_reentrancy/read_only_reentrancy.py) | Read only vulnerability                     | No example provided                                            |
| 7   | NAME1                | Your own detector :)                        | N/A                                                     |
| 8   | NAME2                | Your own detector :)                        | N/A                                                     |
| 9  | NAME3                | Your own detector :)                        | N/A                                                     |

The list does not follow a particular order. 
The `read-only-reentrancy` is considered as the most challenging detector to write (you might take inspiration from the [existing detectors](https://github.com/crytic/slither/tree/master/slither/detectors/reentrancy)).
We would recommend trying to write your own detector's idea after writing 2-3 of the provided ones. 

# Judging criteria
- Novelty and complexity handling
- False alarms rate
- Code quality
- Test quality

# Setup 
- Fork this repo
- Update the detectors in `detectors/NAME/detector_name.py`
  - For a new detector, update `detectors/all_detectors.py` to import the class
- Add more tests in `evaluation/NAME/`. Ensure the code compile with solc 0.8.20 (if another version is needed, precise it)

## Python tips
- Use a python virtual environement.
  - For example: https://virtualenvwrapper.readthedocs.io/en/latest/
  - `mkvirtualenv secureum` - generate a python virtual env
  - `workon secureum` - open the virtual env
- From the virtual env, run `pip install -e .`. This will add the detectors in slither.
- You can then run you new detector with `slither path/to/file.sol --detect NAME`

Ask in discord if you have problems 

# Submission

Send your fork of this repo to `josselin@trailofbits.com` by Sunday 23th end of day (no timezone requirement):
- Either with a zipfile
- Or if you use a private github repo, add `montyly` to the repo

You can provide a readme with any relevant details (ex: highligting specific edge case handled, showing the different tests)

# References
- [Tutorials](https://secure-contracts.com/program-analysis/slither/index.html)
- [Adding a new detector](https://github.com/crytic/slither/wiki/Adding-a-new-detector)
- [Slides](./slides.pdf)

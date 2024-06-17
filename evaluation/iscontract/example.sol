
// Using extcodesize to detect if the caller is a contract is flawed, as a contract mid-deployment will not yet have its code set, and can trick the vulnerable contract.

contract A {
    modifier isContract {
        uint32 size;
        address a = msg.sender;
        assembly {
            size := extcodesize(a)
        }
        require(size > 0);
        _;
    }
}

contract Divide{

    uint total_supply;

    function totalSupply() public returns(uint){
        return total_supply;
    }

    function divideTotalSupply() public returns (uint) {
        return 420 / totalSupply();
    }
}
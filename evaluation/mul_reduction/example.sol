contract test{

    function mulby2(uint a) public returns(uint)    {
        return a * 2; // can be replaced by  a+a
    }


    uint a;
    function mulby2() public returns(uint)    {
        return a * a; // can be replaced by  a+a. However this is better only if the optimization is enabled
    }

}

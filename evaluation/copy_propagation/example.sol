contract Test3{
    function f(uint x) public returns(uint){
        uint y;
        uint z;
        // This can be replace dby z = 3 + x;
        y = x;
        z = 3 + y;
        return z;
    }
}
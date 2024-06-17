contract A{
    event EventEmited();
    event OmmitedEmited();

    function test() public{
        emit EventEmited();
    }
}

contract B{
    event MyEvent(uint a);
    event MyEvent();

    function test() public{
        emit MyEvent(10);
    }
}

contract C{

    event EventEmited();
    event OmmitedEmited();

}

contract D is C{
    function test() public{
        emit EventEmited();
    }
}

contract Simple{
    uint v;

    function test() public returns(uint){
        uint result = v + v;
        return result;
    }

}

contract Complex1{

    uint v;

    function increase_v() public{
        v++;
    }

    function read_v() public returns(uint){
        return v;
    }

    function test(bool b) public{
        uint a;
        a = read_v();
        // because of the condition write, we can't remve the first read
        if(b){
            increase_v();
        }
        a += read_v();
        a += read_v();
    }

}

contract Complex2{

    uint v;

    function test(uint counter) public {
        uint res;
        
        // because of the loop, which writes into v, the read on v can't be removed
        for(uint i=0; i<counter;i++){
            res = v + 1;

            v = counter+1;
        }

    }

}
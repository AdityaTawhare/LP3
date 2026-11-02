// practical 2
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract SimpleBank{
    uint public balance;
    function deposit(uint amount) public{
        require( amount>0,"invalid amount");
        balance+=amount;
    }
    function withdraw(uint amount) public{
        require(amount>0,"invalid amount");
        require(amount<=balance, "Insufficuet balance ");
        balance-=amount;
    }
    function ShowBalance()public view returns (uint){
        return balance;        
    }
}



//Practical 3
pragma solidity ^0.8.20;
contract studentdata{
    struct student{
        uint rollNo;
        string name;
        uint age;
    }
    student[] public students;
    function addstudent(uint r,string memory n,uint a)public {
        students.push(student(r,n,a));
    }
    fallback() external payable { }
}


// SPDX-License-Identifier: MIT

pragma solidity ^0.8.3 <0.9.0;

// Array - dynamic or fixed size
// Initialization
// Insert(push) and remove(pop), update, delete, length
// Creating an array in memory
// Returning array from function

contract Array {
    uint[] public nums = [1,2,3];       // dynamic size
    uint[3] public numsFixed = [4,5,6]; // fixed size

    function examples() external {
        nums.push(4);           // add(push) to end of array
        uint x = nums[1];       // get 2nd element
        nums.pop();             // remove last element and return it
        nums[1] = 666;          // set 2nd element to 666
        uint y = nums.length;   // get length of array
        delete nums[1];         // delete element at index 1

        // create an array in memory
        uint[] memory nums2 = new uint[](3); // note: has to be fixed size for memory, no pop or push
        nums2[0] = 1; // update element of memory array

    }

    // not recommended to return an array, because arrays take up a lot of gas
    function returnArray() external view returns (uint[] memory) {
        return nums;
    }

}


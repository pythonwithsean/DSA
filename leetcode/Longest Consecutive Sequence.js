//Solution with Queue
const nums = [100, 4, 200, 1, 3, 2];
const setNums = new Set(nums);
let maxLength = 0;
let queue = [];
for (const num of nums) {
  //Means this is begining of the sequence
  if (!setNums.has(num - 1)) {
    queue.push(num);
    let currentLength = 1;
    //Begin Bfs algorithm
    while (queue.length > 0) {
      let currentNumber = queue.shift();
      let NextNumber = currentNumber + 1;
      if (setNums.has(NextNumber)) {
        currentLength++;
        queue.push(NextNumber);
      }
    }
    maxLength = Math.max(currentLength, maxLength);
  }
}

console.log(maxLength);

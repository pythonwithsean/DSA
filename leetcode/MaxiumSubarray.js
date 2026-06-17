const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

//Brute Force Solution
let Max = 0;
for (let i = 0; i < nums.length; i++) {
  let sum = 0;
  for (let j = 0; j < nums.length; j++) {
    let elm = nums[j];
    sum += elm;
    Max = Math.max(sum, Max);
  }
}

console.log(Max);

// let left = 0 
// let right = nums.length
// let res = []
// let rounds = 0 
// let num = 1
// while (rounds < nums.length){
	// 	if(left !== right){
		// 	 num *= nums[left]
		// 	}
		// 	left += 1 % nums.length
		// 	if( left % nums.length === 0){
			// 		res.push(num)
			// 		rounds +=1
			// 		left = 0
			// 		right -= 1
			// 		num = 1
			// 	}
			// }
			// console.log(res)

			
// Second Solution
// let leftArr = new Array(nums.length).fill(1) 
// leftArr[0] =  1
// let rightArr = new Array(nums.length).fill(1)
// rightArr[rightArr.length - 1] = 1
// for (i = 1; i < leftArr.length; i++){
	// 	leftArr[i] = nums[i - 1] * leftArr[i -1]
	// }
	
	// for(i = nums.length - 1; i > 0; i--){
		// 	rightArr[i-1] = rightArr[i] * nums[i]
		// }
		// let result = new Array(nums.length).fill(1)
		// for (let v = 0; v < result.length; v++){
			// 	result[v] = leftArr[v] * rightArr[v]
			// }
			
			// console.log(result)
			
			
let nums = [1,2,3,4]
const length = nums.length
let result = new Array(length).fill(1)

// Result = [1,1,1,1]
// Add Left Side of Array
let LeftProduct = 1
for (let i = 0; i < length; i++){
	result[i] = LeftProduct
	LeftProduct *= nums[i]
}
console.log(result)
let right_product = 1
for(let i = length -1; i > -1; i--){
	result[i] *= right_product
	right_product *= nums[i]
}

console.log(result)

//Container With Most Water
// For the height we use the smaller bound 
// the width is i max - i min
// 2 Pointer Solution
const height = [1,8,6,2,5,4,8,3,7]
let bounds  = height.length
// let left = 0 
// let right = height.length
// let max = 0
// while (left < right){
// 	if(height[left] < height[right]){
// 		left +=1 
// 	}else{
// 		right -=1
// 	}
	
// 	let amount = Math.abs(right - left) * Math.min(height[left],height[right])
// 	if(max < amount){
// 		max = amount
// 	}

// }
// console.log(max)

// O(N^2) BruteForce Solution
let max= 0 
for(let i = 0; i < bounds; i++){
	for(y = i + 1; y < bounds; y++){
		let amount = Math.min(height[i], height[y]) * Math.abs(y - i)
		if(max < amount) max = amount
	}
}
console.log(max)


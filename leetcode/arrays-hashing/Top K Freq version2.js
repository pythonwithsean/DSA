let m = new Map()
let nums = [ 3,0,1,0], k = 1
// rank 1 -> 0: 2
// rank 2 -> 3 : 1
// rank 3 -> 1: 1

for(let i = 0; i < nums.length; i++){
  if(!m.has(nums[i])){
    m.set(nums[i],[nums[i]])
  }else{
    m.get(nums[i]).push(nums[i])
  }
}

let res = []
let count = [...m.values()].sort((a,b) => b.length - a.length)

for(let r = 0; r < k; r++) { 
  res.push(count[r][0])  
}
console.log(res)
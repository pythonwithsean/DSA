let prices = [7,1,5,3,6,4]
let length = prices.length	
let left = 0;
let right = 1
let maxProfit = 0

while(right < length){
	if(prices[left] < prices[right]){
		let profit = Math.abs(prices[left] - prices[right])
		if(profit > maxProfit){
			maxProfit = profit
		}
	}else{
		left = right
	}
	right += 1
}


console.log(maxProfit)
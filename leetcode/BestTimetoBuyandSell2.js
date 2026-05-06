let prices = [7,6,4,3,1] 
let maxProfit = 0;
let left = 0;
let right = 1


while(right < prices.length){
	if(prices[left] > prices[right]){
		left = right
	}
	else{
			let profit = prices[right] - prices[left]
				maxProfit += profit	
				left = right
	}
	right += 1
}

console.log(maxProfit)
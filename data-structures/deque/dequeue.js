class Deque{ 
	/**
	 * 
	 * @param {*} size 
	 */
	constructor(size){ 
		this.bucket = new Array(size).fill(null)
		this.front = size - 1
		this.rear = size - 1 
	}
					
	//  r   
	// f
	// [null, null, null]   		
	// so for the front we go backward to add and foward after remove 
	// and for the read we go forward to add and backward after remove 
	append_rear = (num) => {
		this.rear = (this.rear + 1) % this.bucket.length // move rear forward
		this.bucket[this.rear] = num
	}

	pop_rear = () => { 
		this.bucket[this.rear] = null  
		this.rear = (this.rear - 1) % this.bucket.length 
	}

	append_front = (num) => { 
		this.front = (this.front - 1) % this.bucket.length
		this.bucket[this.front] = num
	}

	pop_front = () => { 
		this.bucket[this.front] = null 
		this.front = (this.front + 1 ) % this.bucket.length
	}	

	// Get the front element
    peek_front = () => {
        return this.bucket[this.front] !== null ? this.bucket[this.front] : 'Queue is empty';
    }

    // Get the rear element
    peek_rear = () => {
        return this.bucket[(this.rear - 1 + this.bucket.length) % this.bucket.length] !== null
            ? this.bucket[(this.rear - 1 + this.bucket.length) % this.bucket.length]
            : 'Queue is empty';
    }
}

deque = new Deque(3)
deque.append_front(1)
console.log(deque.peek_rear())
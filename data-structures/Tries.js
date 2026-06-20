class TrieNode{
	constructor(){ 
		this.children = {}
		this.endOfWord = false 
	}
} 


class Tries { 
	constructor(){ 
		this.root = new TrieNode()
	}

	insertWord = (word) => {
		let current = this.root
		for(const char of word){ 
			if (!(current.children[char])){ 
				current.children[char] = new TrieNode()
			}
			current = current.children[char]
		}
		current.endOfWord = true 
	}

	search = (word) => { 
		let current = this.root
		for (const char of word){ 
			if(!(current.children[char])){ 
				return false 
			}
			current = current.children[char]
		
		}
		return current.endOfWord
	}

	startsWith = (pref) => { 
		let current = this.root
		for(const char of pref){ 
			if(!(current.children[char])) { 
				return false
			}else{ 
				current = current.children[char]
			}
		}
		return current.endOfWord === false
	}
}


const TrieTree = new Tries()
TrieTree.insertWord("apple")
console.log(TrieTree.search("apple")) // True
console.log(TrieTree.search("app")) // False
console.log(TrieTree.startsWith("app")) // True


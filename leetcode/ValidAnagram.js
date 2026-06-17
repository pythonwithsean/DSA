let s = "anagram", t = "nagaram"
let sortedWordA = t.split("").sort((a,b) => a.localeCompare(b)).join(), sortedWordB =  s.split("").sort((a,b) => a.localeCompare(b)).join()
console.log(sortedWordA === sortedWordB)
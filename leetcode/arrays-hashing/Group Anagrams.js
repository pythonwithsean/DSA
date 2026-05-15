strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
out = [];
let map = new Map();

for (let i = 0; i < strs.length; i++) {
  let word = strs[i]
    .split("")
    .sort((a, b) => a.localeCompare(b))
    .join("");
  if (!map.has(word)) {
    map.set(word, [strs[i]]);
  } else {
    map.get(word).push(strs[i]);
  }
}
out = [...map.values()];
console.log(out);

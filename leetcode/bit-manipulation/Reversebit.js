n = 0b00000010100101000001111010011100;
bin = n.toString(2);
result = bin.split("").reverse().join("");
bin_curr = parseInt(result, 2);
console.log(bin_curr * 2 ** (32 - result.length));

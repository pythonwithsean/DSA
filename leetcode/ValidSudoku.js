let board = [
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
];

let length = board.length;
//Row
for (let row = 0; row < length; row++) {
  let s = new Set();
  for (let col = 0; col < length; col++) {
    let item = board[row][col];
    if (item !== ".") {
      if (s.has(item)) {
        console.log("False");
        // return false;
      }
      s.add(item);
    }
  }
}

//Col
for (let row = 0; row < length; row++) {
  let s = new Set();
  for (let col = 0; col < length; col++) {
    //So i check the row ith element for every column iteration
    let item = board[col][row];
    if (item !== ".") {
      if (s.has(item)) {
        console.log("False");
        // return false;
      }
      s.add(item);
    }
  }
}

//3x3
const pos = [
  [0, 0],
  [0, 3],
  [0, 6],
  [3, 0],
  [3, 3],
  [3, 6],
  [6, 0],
  [6, 3],
  [6, 6],
];

for (const [x, y] of pos) {
  const seen = new Set();
  for (let row = x; row < x + 3; row++) {
    for (let col = y; col < y + 3; col++) {
      let item = board[x][y];
      if (item !== ".") {
        if (seen.has(item)) {
          console.log("Found");
          return false;
        }
        seen.add(item);
      }
    }
  }
}

console.log("true");

for (let x = 0; x < board.length; x++) {
	for (let y = 0; y < board.length; y++) {
		let rowMsg = `Value ${board[x][y]} found at row ${x}`;
		let colMsg = `Value ${board[x][y]} found at row ${y}`;
		if (!s.has(rowMsg)) {
			if (!s.has(colMsg))
				s.add(colMsg);
			else {
				console.log("Duplicate Found", board[x][y]);
				break;
			}

			s.add(rowMsg);
		} else {
			console.log("Duplicate Found", board[x][y]);
			break;

		}
	}
}

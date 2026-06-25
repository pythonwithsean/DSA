// package main

// import (
// 	"bufio"
// 	"container/heap"
// 	"container/list"
// 	"fmt"
// 	"math"
// 	"os"
// 	"sort"
// 	"strconv"
// 	"strings"
// )

// func main() {
// 	// ======================== FAST I/O ========================
// 	reader := bufio.NewReader(os.Stdin)
// 	writer := bufio.NewWriter(os.Stdin)
// 	scanner := bufio.NewScanner(os.Stdin)
// 	defer writer.Flush()

// 	// ======================== READING INPUT ========================

// 	// Read a single int
// 	var n int
// 	fmt.Scan(&n)

// 	// Read int with bufio (faster)
// 	line, _ := reader.ReadString('\n')
// 	line = strings.TrimSpace(line)
// 	n, _ = strconv.Atoi(line)

// 	// Read multiple ints from one line
// 	scanner.Scan()
// 	parts := strings.Fields(scanner.Text())
// 	a, _ := strconv.Atoi(parts[0])
// 	b, _ := strconv.Atoi(parts[1])

// 	// Read slice of ints
// 	scanner.Scan()
// 	fields := strings.Fields(scanner.Text())
// 	nums := make([]int, len(fields))
// 	for i, f := range fields {
// 		nums[i], _ = strconv.Atoi(f)
// 	}

// 	// Read until EOF
// 	for scanner.Scan() {
// 		line := scanner.Text()
// 		// process line
// 		_ = line
// 	}

// 	// Read all lines into slice
// 	var lines []string
// 	for scanner.Scan() {
// 		lines = append(lines, scanner.Text())
// 	}

// 	// ======================== WRITING OUTPUT ========================
// 	fmt.Println("hello")                             // simple print
// 	fmt.Fprintln(writer, "hello")                    // buffered print (faster)
// 	fmt.Fprintf(writer, "%d %s\n", 42, "answer")     // formatted

// 	// ======================== STRINGS ========================

// 	// Strings are immutable in Go
// 	s := "hello world"

// 	// Length
// 	len(s) // bytes, not runes

// 	// Substring (slice of bytes)
// 	sub := s[0:5] // "hello"

// 	// Iterate over runes
// 	for i, r := range s {
// 		_, _ = i, r
// 	}

// 	// Builder (like StringBuilder)
// 	var sb strings.Builder
// 	sb.WriteString("hello")
// 	sb.WriteByte(' ')
// 	sb.WriteString("world")
// 	sb.String() // "hello world"

// 	// Split / Join
// 	parts = strings.Split("a,b,c", ",")
// 	joined := strings.Join(parts, ",")

// 	// Trim
// 	strings.TrimSpace(s)
// 	strings.Trim(s, " \n\t")
// 	strings.TrimPrefix(s, "hello")

// 	// Contains / Count / Replace
// 	strings.Contains(s, "world")
// 	strings.Count(s, "l")
// 	strings.ReplaceAll(s, "l", "L")

// 	// ToUpper / ToLower
// 	strings.ToUpper(s)
// 	strings.ToLower(s)

// 	// Rune array (for Unicode/mutable string manipulation)
// 	runes := []rune(s)
// 	runes[0] = 'H'
// 	s = string(runes)

// 	// int <-> string
// 	s = strconv.Itoa(42)
// 	n, _ = strconv.Atoi("42")

// 	// ======================== SLICES ========================

// 	// Declare and initialize
// 	arr := make([]int, 0, 10)        // len=0, cap=10
// 	slice := []int{1, 2, 3}          // literal
// 	dp := make([][]int, n)           // 2D slice
// 	for i := range dp {
// 		dp[i] = make([]int, m)
// 	}

// 	// Append
// 	slice = append(slice, 4)         // [1,2,3,4]
// 	slice = append(slice, 5, 6)      // [1,2,3,4,5,6]
// 	slice = append(slice, nums...)   // append another slice

// 	// Copy
// 	dst := make([]int, len(src))
// 	copy(dst, src)

// 	// Slice tricks
// 	slice = slice[:0]                // clear (keep capacity)
// 	slice = append([]int{n}, slice...) // prepend

// 	// Subslice (no copy, shares backing array)
// 	sub = slice[1:3]

// 	// ======================== MAPS ========================

// 	// Hash map
// 	m := make(map[string]int)
// 	m["key"] = 42
// 	val, ok := m["key"] // ok is true if key exists
// 	delete(m, "key")

// 	// Iterate
// 	for k, v := range m {
// 		_, _ = k, v
// 	}

// 	// Set (using map)
// 	set := make(map[int]bool)
// 	set[1] = true
// 	if set[1] {
// 		// exists
// 	}
// 	delete(set, 1)

// 	// ======================== SORTING ========================

// 	sort.Ints(nums)                          // ascending
// 	sort.Sort(sort.Reverse(sort.IntSlice(nums))) // descending

// 	// Sort strings
// 	sort.Strings(strs)

// 	// Custom sort
// 	sort.Slice(slice, func(i, j int) bool {
// 		return slice[i] < slice[j] // ascending
// 	})

// 	// ======================== HEAP (Priority Queue) ========================

// 	// Min-heap example
// 	h := &MinHeap{}
// 	heap.Init(h)
// 	heap.Push(h, 3)
// 	heap.Push(h, 1)
// 	heap.Push(h, 2)
// 	smallest := heap.Pop(h).(int)

// 	// Max-heap: negate values, or define Less as reversed
// 	mh := &MaxHeap{}
// 	heap.Init(mh)

// 	// ======================== LIST (Doubly Linked List / Deque) ========================

// 	l := list.New()
// 	l.PushBack(1)
// 	l.PushFront(2)
// 	front := l.Front().Value.(int)
// 	back := l.Back().Value.(int)
// 	l.Remove(l.Front())

// 	// ======================== MATH ========================

// 	math.Max(float64(a), float64(b))
// 	math.Min(float64(a), float64(b))
// 	math.Abs(float64(a))
// 	math.Pow(2.0, 10.0)
// 	int(math.Sqrt(float64(81))) // 9
// 	int(math.Pow10(3))          // 1000

// 	// Min/Max for ints (not in stdlib, write your own)
// 	// min := func(a, b int) int { if a < b { return a }; return b }
// 	// max := func(a, b int) int { if a > b { return a }; return b }

// 	// ======================== STRUCTS ========================

// 	type ListNode struct {
// 		Val  int
// 		Next *ListNode
// 	}

// 	type TreeNode struct {
// 		Val   int
// 		Left  *TreeNode
// 		Right *TreeNode
// 	}

// 	type Pair struct {
// 		first, second int
// 	}

// 	// ======================== COMMON PATTERNS ========================

// 	// Reading pairs into slice
// 	// scanner.Scan()
// 	// t, _ := strconv.Atoi(scanner.Text())
// 	// pairs := make([][2]int, t)
// 	// for i := 0; i < t; i++ {
// 	//     scanner.Scan()
// 	//     fs := strings.Fields(scanner.Text())
// 	//     a, _ := strconv.Atoi(fs[0])
// 	//     b, _ := strconv.Atoi(fs[1])
// 	//     pairs[i] = [2]int{a, b}
// 	// }

// 	// Sliding window / two pointers
// 	// left, right := 0, 0
// 	// for right < n {
// 	//     // expand window
// 	//     right++
// 	//     for /* condition */ {
// 	//         // shrink window
// 	//         left++
// 	//     }
// 	// }
// }

// // ======================== HEAP IMPLEMENTATIONS ========================

// type MinHeap []int

// func (h MinHeap) Len() int            { return len(h) }
// func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] }
// func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
// func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
// func (h *MinHeap) Pop() interface{} {
// 	old := *h
// 	n := len(old)
// 	x := old[n-1]
// 	*h = old[:n-1]
// 	return x
// }

// type MaxHeap []int

// func (h MaxHeap) Len() int            { return len(h) }
// func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] } // reversed
// func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
// func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
// func (h *MaxHeap) Pop() interface{} {
// 	old := *h
// 	n := len(old)
// 	x := old[n-1]
// 	*h = old[:n-1]
// 	return x
// }

// // ======================== UTILITY HELPERS ========================

// func minInt(a, b int) int {
// 	if a < b {
// 		return a
// 	}
// 	return b
// }

// func maxInt(a, b int) int {
// 	if a > b {
// 		return a
// 	}
// 	return b
// }

// func absInt(x int) int {
// 	if x < 0 {
// 		return -x
// 	}
// 	return x
// }

// func gcd(a, b int) int {
// 	for b != 0 {
// 		a, b = b, a%b
// 	}
// 	return a
// }

// func lcm(a, b int) int {
// 	return a / gcd(a, b) * b
// }

package main

import "fmt"

func toInt(s string) (int, error) {
	res := 0
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c < 0x30 || c > 0x39 {
			return -1, fmt.Errorf("can not turn \"%c\" to int", c)
		}
		res *= 10
		res += int((c - byte('0')))
	}
	return res, nil
}

func main() {
	x := "200"
	fmt.Printf("%T %v\n", x, x)
	p, err := toInt(x)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%T %v\n", p, p)
}

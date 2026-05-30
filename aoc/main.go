package main

import "fmt"

func main() {

	var i any = 22

	if s, ok := i.(string); ok {
		fmt.Println(s)
	}

}

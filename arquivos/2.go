package exercicio2

import (
	"fmt"
)

func main() {
	var t1, t2 int
	fmt.Scan(&t1)
	fmt.Scan(&t2)
	if t1 > t2 {
		fmt.Println(1)
	} else if t1 < t2 {
		fmt.Println(2)
	} else {
		fmt.Println(0)
	}
}

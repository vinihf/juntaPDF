package exercicio1

import (
	"fmt"
)

func main() {
	var v1 int
	var v2 int
	fmt.Scan(&v1)
	fmt.Scan(&v2)
	if v2 > 0 {
		fmt.Println(v1 % v2)
	} else {
		fmt.Println("Erro")
	}
}

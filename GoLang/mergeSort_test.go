package main
import (
	"testing"
	"math/rand"
	"fmt"
)

func TestMergeSort(t *testing.T) {
	var testArr = []PokemonProduct {
		{Name:"Test", Price:"10.00"},
		{Name:"Test", Price:"100.00"},
		{Name:"Test", Price:"1000.00"},
		{Name:"Test", Price:"1000.00"},
		{Name:"Test", Price:"10000.00"},
		{Name:"Test", Price:"10000.00"},
		{Name:"Test", Price:"10001.00"},
		{Name:"Test", Price:"100011.00"},
		{Name:"Test", Price:"100011.00"},
		{Name:"Test", Price:"1000111.00"},
	}
	var shuffleArr = make([]PokemonProduct, len(testArr))
	copy(shuffleArr, testArr)
	rand.Shuffle(len(shuffleArr), func(i, j int) {
		shuffleArr[i], shuffleArr[j] = shuffleArr[j], shuffleArr[i]
	})
	fmt.Print(shuffleArr)
	sort(shuffleArr, 0, len(shuffleArr) - 1)
	for i := 0; i < len(testArr); i++{
		want := testArr[i].Price
		if want != shuffleArr[i].Price {
			t.Errorf("Got %q, wanted %q", shuffleArr[i].Price, want)
		}
	}


}

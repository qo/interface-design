package main

import (
  "fmt"
  "sync"
  "time"
)

var wg sync.WaitGroup

func repeat(s string, n int) {
  for i := 0; i < n; i++ {
    fmt.Println(s)
    time.Sleep(time.Millisecond)
  }
  wg.Done()
}

func main() {
  go repeat("0", 10)
  go repeat("1", 10)
  wg.Add(2)
  wg.Wait()
}

# Explanation

In order to showcase multithreading 2 goroutines are used: the first to print zeroes, and the second to print ones. Since goroutines are running concurrently, zeroes and ones are mixed in the output. The WaitGroup is used in order to ensure all of goroutines have finished before program terminates.

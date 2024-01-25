package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

func lineToSublines(line string) []string {
	sublines := strings.Split(line, " | ")
	return sublines
}

func sublineToPathAndArgs(subline string) (string, []string) {
	parts := strings.Split(subline, " ")
	path, args := parts[0], parts[1:]
	return path, args
}

func lineToCmds(line string) []*exec.Cmd {
	var cmds []*exec.Cmd
	sublines := lineToSublines(line)
	for _, subline := range sublines {
		path, args := sublineToPathAndArgs(subline)
		cmd := exec.Command(path, args...)
		cmds = append(cmds, cmd)
	}
	return cmds
}

func run(line string) (string, error) {
	var mid strings.Builder
	cmds := lineToCmds(line)
	for _, cmd := range cmds {
		cmd.Stdin = strings.NewReader(mid.String())
		mid.Reset()
		cmd.Stdout = &mid
		err := cmd.Run()
		if err != nil {
			return "", err
		}
	}
	return mid.String(), nil
}

func read() (string, error) {
	in := bufio.NewReader(os.Stdin)
	line, err := in.ReadString('\n')
	if err != nil {
		return "", err
	}
	line = strings.Trim(line, "\n")
	return line, err
}

func main() {
	line, err := read()
	if err != nil {
		log.Fatal(err)
	}
	out, err := run(line)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Print(out)
}

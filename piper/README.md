# Explanation

The task is to implement Linux pipe operator with using stdin and stdout streams. In order to do that the program parses the command that user inputs. More specifically it splits the command by pipe ("|") operator into individual commands. Then it runs each individual command and makes it so the next command takes previous' command output as an input.

# Example

## Input

`ls -la | grep M | grep file`

## Output

`-rw-r--r--. 1 null null 147 Jan 25 20:15 Makefile`

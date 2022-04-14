package main

import "fmt"

func main() {
	info, err := GetReleaseInfo()
	if err != nil {
		panic(err)
	}
	fmt.Println(info.RepoUrl)
}

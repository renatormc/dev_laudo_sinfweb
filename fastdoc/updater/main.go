package main

import (
	"os"
	"path/filepath"
)

func updateLibs() {
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exPath := filepath.Dir(ex)
	pythonExe := filepath.Join(exPath, "extras", "Python", "python.exe")
	requirementsPath := filepath.Join(exPath, "requirements.txt")
	CmdExec2(pythonExe, "-m", "pip", "install", "-r", requirementsPath)
}

func gitPull() {
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exPath := filepath.Dir(ex)
	gitExe := filepath.Join(exPath, "extras", "git", "git.exe")
	CmdExec2(gitExe, "reset", "--hard")
	CmdExec2(gitExe, "pull", "origin", "master")
}

func main() {
	gitPull()
	updateLibs()
}

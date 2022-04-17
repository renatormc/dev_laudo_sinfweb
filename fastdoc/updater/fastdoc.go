package main

import (
	"log"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exPath := filepath.Dir(ex)
	pythonExe := filepath.Join(exPath, ".venv", "Scripts", "pythonw.exe")
	script := filepath.Join(exPath, "main.py")

	cmd := exec.Command(pythonExe, script, "gui")
	err = cmd.Start()

	if err != nil {
		log.Fatal(err)
		return
	}
}

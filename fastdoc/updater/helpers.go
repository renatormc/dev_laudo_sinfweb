package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"regexp"
	"strings"
	"time"
)

func FileExists(path string) bool {
	info, err := os.Stat(path)
	if os.IsNotExist(err) {
		return false
	}
	return !info.IsDir()
}

func DirectoryExists(path string) bool {
	info, err := os.Stat(path)
	if os.IsNotExist(err) {
		return false
	}
	return info.IsDir()
}

func SaveJson(data interface{}, filepath string) error {
	file, err := json.MarshalIndent(data, "", " ")
	if err != nil {
		return err
	}

	err = ioutil.WriteFile(filepath, file, 0644)
	if err != nil {
		return err
	}
	return nil
}

func WriteTextFile(text string, path string) error {
	f, err := os.Create(path)

	if err != nil {
		return err
	}

	defer f.Close()
	_, err = f.WriteString(text)
	if err != nil {
		return err
	}
	return nil
}

func SliceStrContains(s []string, str string) bool {
	for _, v := range s {
		if v == str {
			return true
		}
	}

	return false
}

func CmdExec(args ...string) (*bytes.Buffer, error) {
	baseCmd := args[0]
	cmdArgs := args[1:]

	cmd := exec.Command(baseCmd, cmdArgs...)

	cmdOutput := &bytes.Buffer{}
	cmd.Stdout = cmdOutput
	cmdErr := &bytes.Buffer{}
	cmd.Stderr = cmdErr
	err := cmd.Run()
	if err != nil {
		return cmdErr, err
	}
	return cmdOutput, nil
}

func CmdExecStrOutput(args ...string) (string, error) {
	res, err := CmdExec(args...)
	return res.String(), err
}

func SanitizeString(value string) string {
	return strings.ReplaceAll(value, "\x00", "")
}

func GetFileSize(filepath string) (int64, error) {
	fi, err := os.Stat(filepath)
	if err != nil {
		return 0, err
	}
	return fi.Size(), nil
}

func StrToDuration(text string) (*time.Duration, error) {
	reg := regexp.MustCompile(text)
	res := reg.FindAllString(text, 1)
	if len(res) != 1 {
		return nil, fmt.Errorf("format unknown")
	}
	parts := strings.Split(res[0], ":")
	duration, err := time.ParseDuration(fmt.Sprintf("%sh%sm%ss", parts[0], parts[1], parts[2]))
	if err != nil {
		return nil, err
	}
	return &duration, nil
}

type ReleaseInfo struct {
	RepoUrl string `json:"repo_url"`
	Version string `json:"version"`
}

func GetReleaseInfo() (*ReleaseInfo, error) {
	var info ReleaseInfo
	resp, err := http.Get("https://raw.githubusercontent.com/renatormc/fastdoc/master/fastdoc/current_release.json")
	if err != nil {
		return nil, err
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	err = json.Unmarshal(body, &info)
	if err != nil {
		return nil, err
	}

	return &info, nil
}

func SyncDown() {
	info, err := GetReleaseInfo()
	if err != nil {
		panic(err)
	}
}

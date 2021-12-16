package main

import (
	"context"
	goHttp "net/http"
	"os"
	"os/signal"
	"syscall"

	dockerContainer "github.com/docker/docker/api/types/container"

	golog "log"

	"github.com/containerssh/auth"
	"github.com/containerssh/configuration/v2"
	"github.com/containerssh/http"
	"github.com/containerssh/log"
	"github.com/containerssh/service"
)

var imageName string = os.Getenv("TASK_IMAGE")

type authHandler struct {
}

var ctx = context.Background()

func (a *authHandler) OnPassword(Username string, Password []byte, RemoteAddress string, ConnectionID string) (
	bool,
	error,
) {
	if string(Password) == "plznohackme" && Username == "user" {
		golog.Printf("Successful login by user %s\n", Username)
		return true, nil
	}

	golog.Printf("Auth failed by IP %s\n", RemoteAddress)

	return false, nil
}

func (a *authHandler) OnPubKey(_ string, _ string, _ string, _ string) (
	bool,
	error,
) {
	return false, nil
}

type configHandler struct {
}

func (c *configHandler) OnConfig(request configuration.ConfigRequest) (configuration.AppConfig, error) {
	containerConfig := dockerContainer.Config{}
	config := configuration.AppConfig{}

	config.Backend = "docker"
	config.Docker.Connection.Host = "unix:///var/run/docker.sock"
	config.Docker.Execution.Launch.ContainerConfig = &containerConfig

	containerConfig.Image = imageName

	golog.Printf("config.Docker.Execution.Launch.ContainerConfig.Image: %s\n", config.Docker.Execution.Launch.ContainerConfig.Image)
	return config, nil
}

type handler struct {
	auth   goHttp.Handler
	config goHttp.Handler
}

func (h *handler) ServeHTTP(writer goHttp.ResponseWriter, request *goHttp.Request) {
	switch request.URL.Path {
	case "/password":
		fallthrough
	case "/pubkey":
		h.auth.ServeHTTP(writer, request)
	case "/config":
		h.config.ServeHTTP(writer, request)
	default:
		writer.WriteHeader(404)
	}
}

func main() {
	logger, err := log.NewLogger(log.Config{
		Level:       log.LevelDebug,
		Format:      log.FormatLJSON,
		Destination: log.DestinationStdout,
	})

	if err != nil {
		panic(err)
	}

	authHTTPHandler := auth.NewHandler(&authHandler{}, logger)
	configHTTPHandler, err := configuration.NewHandler(&configHandler{}, logger)
	if err != nil {
		panic(err)
	}

	srv, err := http.NewServer(
		"authConfig",
		http.ServerConfiguration{
			Listen: "0.0.0.0:6823",
		},
		&handler{
			auth:   authHTTPHandler,
			config: configHTTPHandler,
		},
		logger,
		func(s string) {

		},
	)
	if err != nil {
		panic(err)
	}

	running := make(chan struct{})
	stopped := make(chan struct{})
	lifecycle := service.NewLifecycle(srv)
	lifecycle.OnRunning(
		func(s service.Service, l service.Lifecycle) {
			println("Auth-Config Server is now running...")
			close(running)
		}).OnStopped(
		func(s service.Service, l service.Lifecycle) {
			close(stopped)
		})
	exitSignalList := []os.Signal{os.Interrupt, os.Kill, syscall.SIGINT, syscall.SIGTERM}
	exitSignals := make(chan os.Signal, 1)
	signal.Notify(exitSignals, exitSignalList...)
	go func() {
		if err := lifecycle.Run(); err != nil {
			panic(err)
		}
	}()
	select {
	case <-running:
		if _, ok := <-exitSignals; ok {
			println("Stopping Test Auth-Config Server...")
			lifecycle.Stop(context.Background())
		}
	case <-stopped:
	}
}

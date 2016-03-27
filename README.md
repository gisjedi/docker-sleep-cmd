# docker-sleep-cmd
Docker container to run any command endlessly on a sleep-wait cycle.

## Usage

Run a shell command every 10 seconds following container launch:

```
docker run -e SLEEP_SECONDS 10 gisjedi/sleep-cmd echo Running
```

All commands will be launched in a subprocess and called again in 10 seconds regardless of the completion of previous command.

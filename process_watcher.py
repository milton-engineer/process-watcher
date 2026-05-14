import subprocess


def get_top_processes():
    try:
        result = subprocess.run(
            [
                "ps",
                "-eo",
                "pid,ppid,cmd,%mem,%cpu",
                "--sort=-%cpu"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.splitlines()

        print("Process Watcher")
        print("-" * 60)

        for line in output[:10]:
            print(line)

    except Exception as error:
        print(f"[ERROR] Failed to inspect processes: {error}")


if __name__ == "__main__":
    get_top_processes()

import subprocess

def run_command_with_logging(logfile_name, command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    try:
        with open(logfile_name, 'w') as logfile:
            while True:
                output = process.stdout.readline()
                if output == b'' and process.poll() is not None:
                    break
                if output:
                    line = output.decode().strip()
                    print(line)
                    logfile.write(line + '\n')
                    logfile.flush()
    except KeyboardInterrupt:
        print("Process killed")
    finally:
        process.terminate()  # ensure subprocess is terminated
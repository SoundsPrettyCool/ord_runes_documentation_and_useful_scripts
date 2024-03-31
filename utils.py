import subprocess

def run_command_with_logging(logfile_name, command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    with open(logfile_name, 'w') as logfile:
        try:
            while True:
                output = process.stdout.readline()
                if output == b'' and process.poll() is not None:
                    break
                if output:
                    line = output.decode().strip()
                    print(line)
                    logfile.write(line + '\n')
                    logfile.flush()
            process.poll()
        except KeyboardInterrupt:
            process.kill()
            print("Process killed")
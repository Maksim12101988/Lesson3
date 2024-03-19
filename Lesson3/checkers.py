import subprocess
def checkout(cmd: str, text: str) -> bool:

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    print(result.stdout)  # Print the command's output
    if text in result.stdout and result.returncode == 0:  # Check if the text is in the output and the command returns with code 0
        return True
    else:
        return False

def checkout_negative(cmd, text):

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def get_output_from_command(cmd):

    completed_process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return completed_process.stdout


def getout():
    return None
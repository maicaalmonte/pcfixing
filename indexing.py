import subprocess

def run_indexing_troubleshooter():
    # Launch the Windows Troubleshooter for Indexing
    subprocess.run("msdt.exe /id PerformanceDiagnostic", shell=True)

run_indexing_troubleshooter()

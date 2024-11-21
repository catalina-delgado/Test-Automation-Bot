import subprocess
import sys

browser = "chrome"

result = subprocess.run(
    [sys.executable, '-m', 'pytest', '--browser', browser],  # Cambié el formato de argumentos
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)
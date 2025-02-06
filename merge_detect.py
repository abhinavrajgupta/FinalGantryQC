import subprocess

module_name = input("Enter the module name (e.g., 'M35'): ")
source_path = f"Modules/{module_name}/"

command_arrowplot = [
    "python", "detect_arrowplot.py",
    "--weights", "bestarrowplot.pt",
    "--img", "640",
    "--conf", "0.6",
    "--source", source_path,
    "--project", source_path,
    "--name", "ResultsArrowPlots",
    "--save-txt"
]

command_wirebond = [
    "python", "detect_wirebond.py",
    "--weights", "bestwirebond.pt",
    "--img", "640",
    "--conf", "0.5",
    "--source", source_path,
    "--project", source_path,
    "--name", "Resultswirebond",
    "--save-txt"
]

try:
    subprocess.run(command_wirebond, check=True)
    print("Detection for Wirebond completed successfully!")
    subprocess.run(command_arrowplot, check=True)
    print("Detection for arrowplot completed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error during detection: {e}")


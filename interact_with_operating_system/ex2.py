import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if not os.path.isdir(directory):
    os.mkdir(directory)
  # Create the new file inside of the new directory
  os.chdir(directory)

  with open (filename,"w") as file:
    file.write("")

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))
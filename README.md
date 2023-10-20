# IntuneConverter
Python GUI Software that convert installation files into Intune files

This script provides a simple GUI for converting application installers into the .intunewin format using the IntuneWinAppUtil.exe tool.

**Features:**

Select source and output directories through a GUI.
Convert .exe or .msi installers to .intunewin format.
Intuitive feedback with success and error messages.

**Prerequisites:**

tkinter module for the GUI.
IntuneWinAppUtil.exe should be in the same directory as this script.

**Usage:**

Run the script. A GUI window titled "IntuneWin Converter" will appear.
Click on "Select Source Folder" to select the directory containing the installer you wish to convert.
Click on "Select Output Folder" to select the directory where the converted .intunewin file should be saved.
Click on "Convert to IntuneWin" to start the conversion process.
Choose the installer file (.exe or .msi) from the source folder.
Upon successful conversion, a success message will be displayed. If there's an error during the conversion, an error message will pop up showing the reason for the failure.

**Notes:**

The script assumes that the IntuneWinAppUtil.exe is present in the same directory as the script. Ensure that it is available before running the script.
Ensure you have necessary permissions to read from the source folder and write to the output folder.
The script is built using the tkinter library, and it might require additional installations if tkinter is not already installed in your Python environment.


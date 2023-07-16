import os
import configparser

# Read the configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Check if Thunderbird has been installed using this script before
if os.path.exists(f"{config['paths']['opt_path']}/thunderbird"):
    # Move the current installation to a backup folder
    os.system(f"mv {config['paths']['opt_path']}/thunderbird {os.path.expanduser('~')}/Thunderbird_backup")

# Download Thunderbird
os.system(f"wget -O {config['paths']['download_path']}/thunderbird.tar.bz2 '{config['links']['thunderbird_latest']}'")

# Extract the contents of the downloaded file
os.system(f"tar xjf {config['paths']['download_path']}/thunderbird.tar.bz2 -C {config['paths']['download_path']}")

# Move the uncompressed Thunderbird folder to /opt
os.system(f"sudo mv {config['paths']['download_path']}/thunderbird {config['paths']['opt_path']}")

# Create a symlink to the Thunderbird executable
os.system(
    f"sudo ln -sf {config['paths']['opt_path']}/thunderbird/thunderbird {config['paths']['bin_path']}/thunderbird")

# Check if the desktop file has been installed using this script before
if os.path.exists(f"{config['paths']['applications_path']}/thunderbird.desktop"):
    # Move the current desktop file to a backup folder
    os.system(
        f"mv {config['paths']['applications_path']}/thunderbird.desktop {os.path.expanduser('~')}/Thunderbird_backup")

# Download a copy of the desktop file
os.system(f"sudo wget {config['links']['desktop_file']} -P {config['paths']['applications_path']}")

print("Thunderbird has been installed successfully!")

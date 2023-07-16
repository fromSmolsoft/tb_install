import os

# Download Thunderbird
os.system("wget -O ~/Downloads/thunderbird.tar.bz2 'https://download.mozilla.org/?product=thunderbird-latest&os=linux64&lang=en-US'")

# Extract the contents of the downloaded file
os.system("tar xjf ~/Downloads/thunderbird.tar.bz2 -C ~/Downloads")

# Move the uncompressed Thunderbird folder to /opt
os.system("sudo mv ~/Downloads/thunderbird /opt")

# Create a symlink to the Thunderbird executable
os.system("sudo ln -s /opt/thunderbird/thunderbird /usr/local/bin/thunderbird")

# Download a copy of the desktop file
os.system("sudo wget https://raw.githubusercontent.com/mozilla/sumo-kb/main/installing-thunderbird-linux/thunderbird.desktop -P /usr/local/share/applications")

print("Thunderbird has been installed successfully!")

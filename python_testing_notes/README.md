Python includes a tool called pip that’s used to install third-party packages.
Because pip helps install packages from external resources, it’s updated
often to address potential security issues. So, we’ll start by updating pip.
Open a new terminal window and issue the following command:
python3 -m pip install --upgrade pip

You can use this command to update any third-party package installed
on your system:
python3 -m pip install --upgrade package_name

Now that pip is up to date, we can install pytest:
pip3 install pytest

You can use this command to install many third-party packages:
python3 -m pip install --user package_name

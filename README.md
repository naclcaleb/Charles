# Charles
To get your Charles up and running, download the zip file and extract it in a folder of your choice. 
Open up a terminal in the directory, and run:

sudo chmod +x install_dependencies.sh && sudo ./install_dependencies.sh

This will install all the Python libraries and other Linux packages you need to run the Python script.


To get the email system running, you will have to edit a couple of the files. First, open Email.py and replace all occurrences of "example@gmail.com" with your gmail address (has to be Gmail), and "example_password" with your password. Do the same in the mailsys.py file.

To get the SMS messaging system running you will have to sign up for an account with Twilio, and paste information such as your Account SID and Auth Token into their proper variables in the SMS.py file.

You also need to set up your contacts in the contacts.list file. For each contact, make a new line with format:

Name,Email,Phone Number

NOTE: Do not put any spaces between the information and the commas!

That's all! Your Charles should be up and running at this point. 

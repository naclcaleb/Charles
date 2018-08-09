# Charles
To get your Charles up and running, download the zip file and extract it in a folder of your choice. 
Open up a terminal in the directory, and run:

sudo chmod +x install_dependencies.sh && sudo ./install_dependencies.sh

This will install all the Python libraries and other Linux packages you need to run the Python script.

Next you will have to obtain a WolframAlpha app ID for your agent. WolframAlpha (wolframalpha.com) is a Computational Knowledge base that you can search and get answers from. You can read more about it on the website, but we're using it to make our assistant be able to answer random trivia-like questions, offer statistics, and even give real-time data.

To obtain an app ID, you need to create a Wolfram ID. Click on this link to create one: https://account.wolfram.com/auth/create

 Once this is done, go to http://developer.wolframalpha.com/portal/myapps/ and click "Get an AppID"
 Follow the instructions, and once it gives you the AppID, copy it and paste it into the "appID" variable in the "main.py" file. It may take a while for the appID to register, so if you get errors the first few times you try to use it, you may just have to wait a bit.

You will also have to set up the Charles Dialogflow agent. Go to dialogflow.com and sign in with your Google account. Create a new agent and name it Charles. On the panel to the left, click the gear icon next to your agent's name. In the subsequent page, go to the "Import and Export" tab and click "Import from zip". Select the "Charles.zip" file, and all my intents should be imported into your agent. 

The last thing you'll have to do is go back to the "General" tab and scroll until you see "API Keys". Copy the "Client Access token", and paste it into the "access_token" variable in the file "main.py".

That's it for the backend, but there are a few things you might want to set up on the frontend, such as the email system and the SMS messaging system. 


To get the email system running, you will have to edit a couple of the files. First, open Email.py and replace all occurrences of "example@gmail.com" with your gmail address (has to be Gmail), and "example_password" with your password. Do the same in the mailsys.py file.

To get the SMS messaging system running you will have to sign up for an account with Twilio, and paste information such as your Account SID and Auth Token into their proper variables in the SMS.py file.

You also need to set up your contacts in the contacts.list file. For each contact, make a new line with format:

Name,Email,Phone Number

NOTE: Do not put any spaces between the information and the commas!

That's all! Your Charles should be up and running at this point. 

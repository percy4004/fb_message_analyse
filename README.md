# fb_message_analyse

This Python script is for analysing Facebook Messenger data. The outputs are:

  1. A CSV containing the date, week (week commencing date), month, year, time, and sender name)
  2. Individual text files containing the message content of each message participant
  
These outputs can be used for creating graphs showing message volume over time and wordclouds

Here's how to use it:

  1. Download your Facebook Messenger data in JSON format
  2. Create a directory tree like this -
  
      Messenger_Analyse (parent folder)
          message_analyse.py
          Messenger_Group_1 (child folder)
              data (child folder)
              message_1.json
              message_2.json
     
  3. Amend the folder name in the script to the name of your folder
  4. Run the script and use the output to create visualisations

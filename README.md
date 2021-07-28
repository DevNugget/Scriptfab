# Scriptfab - What is it?
A python script to prefab your scripts/text files, and re create them with ease and not have to open your browser to copy code or write code yourself.
You can copy paste or write a script into the python file and re instance it easily. You don't have to wait for your browser to load, you don't have to re-watch a tutorial to write code.
Example of practical use:
You start a new Godot or Unity project and you need to write a Player script (player controller) and you need to look up the code or watch a tutorial, instead of doing that you can copy and paste that code into the python script once and re-instance it as many times you want in the future by running the python file.

# Scriptfab - How to use it?
Download the python file and place it in your project folder, open it using a text editor (preferably Visual Studio Code/Sublime Text/Notepad++/Pycharm) then take a look at the comments, I have tried to explain as much as I can. I will also go through how to use it here.

![image](https://user-images.githubusercontent.com/84568105/127273493-c97641af-e909-4606-ba80-64cd267236fb.png)

Look at the variable called "script_content", this is where your script that you want to re-use goes. Start off by deleting "# Delete this comment and copy paste/write the script you want to re-use here" inside of the triple quotes.

Then copy/paste or write the script there,
example:
![image](https://user-images.githubusercontent.com/84568105/127274074-858de992-0ae2-48d4-80c0-c47d8ea5e560.png)

Now to configure the command
Scroll down to find this,
![image](https://user-images.githubusercontent.com/84568105/127275198-0d276489-4a8e-40f3-a683-faebcbb1a7c7.png)
Then un-comment the elif statement.
Write the name of command that you want to type when running the python file inside the "" ![image](https://user-images.githubusercontent.com/84568105/127275448-ef7d5c1b-f807-40e1-9748-4f8113f63f84.png) ![image](https://user-images.githubusercontent.com/84568105/127275702-3a238e41-408a-4068-af11-f2d8e7efbf23.png) (MAKE SURE IT IS LOWERCASE)

Scroll up to find this, ![image](https://user-images.githubusercontent.com/84568105/127275551-16a307a7-4c65-4d9a-bd32-afe1767dcd9d.png)
Then create a new list value as a string and add the name of the command you used ![image](https://user-images.githubusercontent.com/84568105/127275864-c7b73a17-3303-4f3c-b9b6-269b30f8f874.png)

To add more script prefabs, just re create a similar function and elif statement.

# Scriptfab - End result/Running the py file
Requirements: Python
Go to where you have the python file using file explorer.
![image](https://user-images.githubusercontent.com/84568105/127276788-3870e511-fbef-4905-8311-57017e190572.png)

Right click on dead space while holding your Shift key.
![image](https://user-images.githubusercontent.com/84568105/127276983-889b6be3-c4f7-428b-9b9d-4875d3ba0ebd.png)

Then simply click 'Open PowerShell window here' (This could say CommandPrompt for you depending on your windows version).
After you see the powershell window.
![image](https://user-images.githubusercontent.com/84568105/127277206-51c6afcf-9dfe-4c70-a793-a8b7d739cf51.png)

Type in ![image](https://user-images.githubusercontent.com/84568105/127277283-1fcc1902-10fe-48d3-b4d6-e4c94785adce.png)

You should see this.
![image](https://user-images.githubusercontent.com/84568105/127277376-5133b33a-132f-4d79-b878-55f7c0296f7b.png)

Type in 'scripts' to see the list of scripts you added.
![image](https://user-images.githubusercontent.com/84568105/127277697-4452fc73-01c0-4574-919e-0c3b948f7444.png)

Then type in the command you defined before.
![image](https://user-images.githubusercontent.com/84568105/127277792-1f91a7e6-4b9e-4148-a99e-629de80237f1.png)

Then type the filename and file extentsion.
![image](https://user-images.githubusercontent.com/84568105/127281656-f4574440-09c1-4775-a8ec-99ecbdd5dfee.png)

Check again in the folder to see the script you defined before magically appeared!
![image](https://user-images.githubusercontent.com/84568105/127277920-42617822-e14f-4527-80bd-1999cdb77c18.png)

Enjoy saving time!

# Permission to change the script
Do what ever you want with it :D



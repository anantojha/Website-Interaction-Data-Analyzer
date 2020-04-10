Dependencies
Make sure you have Node.js installed (https://nodejs.org/en/download/)

Set up on a localhost
- Navigate to project directory using command line
- enter "npm install" this will install all other dependencies
- enter "node server.js"
- a message "Server has started" should pop up
- go to http://localhost:8000/ to use the program

Set up on openstack

The process of setting up the programon oepnstack via webserver is as following:
    1.ask SCS to proxy the webserver to port 80 on the dev server instance
    2.change the parts of code that when inqurey files, it would instead inqurey them in directory "comp3008_28/"
    3.run the program locally on port 80

The program would run locally on the port 80, which is being proxy to the webserver. The apache webserver will then utilize the program that is running on port 80 to make it avaliable on the url:https://comp3008-w20.scs.carleton.ca/comp3008_28/

Other files and what they do

package.json - stores dependency information used for npm install
package-lock.json - stores dependency information used for npm install
database.csv - holds all user inputted information
server.js - The file used to start the server

Views
    DirectPass.ejs - The homepage for the website
    Practice.ejs - A pop-up window to practice passwords
    Testing.ejs -  A pop-up window to test passwords

public
    Image.png - an image that was used in Testing.ejs and Password.ejs

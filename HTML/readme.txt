Dependencies
Make sure you have Node.js installed (https://nodejs.org/en/download/)

Set up on a localhost
- Navigate to project directory using command line
- enter "npm install" this will install all other dependencies
- enter "node server.js"
- a message "Server has started" should pop up
- go to http://localhost:8000/ to use the program

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

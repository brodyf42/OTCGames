# OTCGames

This Django web application was created as part of my Computer Science undergraduate capstone. 

### Purpose
The owners of a local tabletop game shop in my town hold board game nights twice weekly in which people are encouraged to play games from the in-store demo library or games brought from home.  Over the past several years, the store owners have maintained paper records of games played during the events.  This method of record keeping has proven inefficient and suffers from a poor ability to scale.  Extracting meaningful information from these records has become increasingly difficult.

This application solves this problem by providing interfaces for entering and reviewing game night event data efficiently and by dynamically generating metrics and graphical trend data for games played during game night events. 

### High-level Description
The Application represents data using two primary entities, the game night event, and the game.  Each event will have several games played, and each game will be played at several different events.  The relationship between these two primary entities is represented by a secondary entity called a played game instance.  The played game instance provides a means to specify data for the unique combination of any given event and game.  For example, the application can track how many people played a given game on a given game night.  The set of unique game play instances also provides the data structure necessary to calculate and report game play trends over time.

The real utility of the application is found through the dynamically generated trend data.  By simply entering which games were played during each event, the application uses that data to create graphical representations of game play trends over time.

Since the application was intended for only a small number of users and will not be available to access by any public means, no considerations for user authentication or other security concerns related to publicly accessible software have been implemented.  This also creates a better experience for the end users by removing unnecessary actions. 

### Screenshots

#### Event List

![Event List](https://brodyf42.github.io/images/OTCGames/OTCGames_event_list.png)

#### Event Details

![Event Details](https://brodyf42.github.io/images/OTCGames/OTCGames_event_details.png)

#### Game List

![Game List](https://brodyf42.github.io/images/OTCGames/OTCGames_game_list.png)

#### Game Details

![Game Details](https://brodyf42.github.io/images/OTCGames/OTCGames_game_details.png)

### Development Environment
Django 1.10  
Python 3.6

### Third Party Libraries Used
jQuery v3.4.1 (https://jquery.org)  
Bootstrap v3.3.7 (http://getbootstrap.com)  
Chart.js v2.8.0 (https://www.chartjs.org)


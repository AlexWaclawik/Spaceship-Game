## Spaceship Shoot Em' Up

This game is a 2D arcade shooter in which you control a multidirectional spaceship and shoot enemy UFOs, 
all while obtaining an ever-increasing score. It has been madein *Python*, using the *Pygame* library.

<p align="right"></p>

### Installation

1. [Download the latest release](https://github.com/AlexWaclawik/Spaceship-Game/releases/tag/final).
2. Unzip the contents.
3. Run *main.py* to start the game.

<p align="right"></p>

### Design

The game is made up of several parts, the main of which being the engine. This file is used for managing the sprites,
timings, and everything else during gameplay. There are four sub-components: the player ship, player laser, enemy ship, and enemy laser.
These components are broken up into their own classes, each with it's own specific functionality.

**Player Ship**
The player ship is based off one of the class demos, with some modifications. It can thrust forwards, 
as well as yaw left and right. Each movement input has it's own sprite, so it creates a pleasent animation. 
The ship controls are surprisingly intuitive, and actually have a bit of a skill curve to them.

**Player Laser**
The player laser is activated by pressing the *spacebar*, and is a sprite. It moves in the direction of the player
when it was called, and has a constant speed. Once the laser is fired, a boolean variable called *canShoot* is set to
**False**. Once the sprite is off the screen, the variable is to **True**.

**Enemy Ship**
The enemy ship is spawned with an x-position of *0* or *1200*, and a random y-position between *50* and *750*. Then based on the spawned
it either moves to the left or to the right. Once the ship is off screen, it gets respawned.

**Enemy Laser**
The enemy ship's laser works independently from the ship. When the ship is on screen, the engine will check the enemy laser's timer,
which is set to a value of *60*. If the timer is at *0*, it spawn at the ship's position and move across the screen with a random direction
that is based on the enemy ship's y-position. This allows it to fire above or below the ship into the majority of the screen. After firing,
the timer decreases by *1* every cycle which gives it a firerate of once every *60* frames, or every second. After firing, the timer resets to *60*. 
I originally created the enemy laser to function in the same way as the player's laser (with a boolean sentry variable). However I was getting
some strange behavior with this approach. Rather than try to force the issue, I went ahead and designed it the other way and it worked flawlessly.
Not wanting to fix something that isn't broken, I kept the player laser and enemy laser's logic different.

**Engine**
The engine acts as the controller of the entire game. It initializes the classes, controls the main loop, displays and updates the 
score, checks for sprite collosion, and overall manages most of the game logic.

**State Transition Diagram**

![statetransition.py](https://i.imgur.com/HzbVXbP.png)

<p align="right"></p>

### Credits

All sound effects and sprites are obtained from https://opengameart.org, and are considered public domain under the
Creative Commons 1.0 License found here: https://creativecommons.org/publicdomain/zero/1.0/.

The splash screen theme music is composed by the artist *Stellardrone* and is obtained from https://freemusicarchive.org/music/Stellardrone.
His work is available for use under the Creative Commons 3.0 License found here: https://creativecommons.org/licenses/by/3.0/.

Individual Credits:
1. [Spaceship Sprite](https://opengameart.org/content/spaceship-9)
2. [UFO Sprite](https://opengameart.org/content/gunship)
3. [Explosion Sprites](https://opengameart.org/content/bubble-explosion)
4. [Backgrounds](https://www.nasa.gov/mission_pages/hubble/multimedia/index.html)
5. [Laser Sprites](https://opengameart.org/content/lasers-and-beams)
6. [Player Gun](https://opengameart.org/content/synthesized-explosion)
7. [Enemy Laser](https://opengameart.org/content/laser-fire-0)
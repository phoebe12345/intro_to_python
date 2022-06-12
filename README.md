# Maze Game

When the game is started, the user has the option to select 1 out of 3 maps. Then the user can press up, down, left right to walk around until they are at the exit. You can use a 2D array to represent the map. In the example below, * represents wall. o represents user's current position. X == exit.

```
****o****
**     **
*      **
***** ***
***   ***
***    **
****** **
***     *
**   ****
**X******
```

This is just one example of the map. You solution should work for all maps (for example the one below). Start with this, then you can design 2 other maps. Let's create a file called `map_1.txt`. Once the user selects the map, then we read the file to load the map. This way is more scalabe when we have 1 million maps.

```
**************************************************
o  ** **  * *    *  * ***  * *** * *  * * * * *  *
       *    **** *     ** * * *  * ***  * *   ****
*****    * **  *  * * * ** **      ** ** *  * ****
** ** *  *       ***  ***  ***   ***** * *  *  ***
** ***  ***             ** ***** ***  *  *** *   *
* * ** **  *   *  ****     ***      * ** *   ** **
* * **  ** *   ***   **  * *   *  *   ****     * *
* ****      **** ** * *    *   **  **    **  *  **
**     ***  ***   * * **   * *    * ****  ** * ***
* ****  *  ** ****   *****    * **   **  ** ** * *
** * *   *     *       *   * * ** ** **  ****** **
**  * * * * **  * ****   * *  *** * * *  **  * * *
**   ** * *** *  * * ****  ***   *   * *  * *** **
*  *   * * ***** *     * *  * ****  *   *   *  * *
* * ***   * * **  ** * *   *****    ***   * *  * *
* *** *    *  * * ***  **         *  ** ***    * *
* ** *   *   *   ***  * **  *   ** * * * * *  ****
*  **** **  *  **           ** *  * * *        ***
**********************************************X***
```

The code must not be a bunch of lines of lose scripts. At a bare minimum, we should have a `class Maze` that handles all maze related logic and a `class Player`. There may be other functions if they don't fall into either classes.

using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Timescript : MonoBehaviour {

    /// <summary>
    /// Variables which can be altered from Unity editor. setroundcountdown is here for for testing purposes. 
    /// </summary>

    public string winscene;
    public float setroundcountdown;
    static float roundcountdown = 10;
    public static float round = 1;

    IEnumerator Start () {

        /// <summary>
        /// On start up, difficulty in global control script asset is checked and the time limit for each round is altered depending on the difficult level. 
        /// </summary> 

        int diff = (int)GlobalControl.difficulty;
        switch (diff)
        {
            case 1:
                setroundcountdown = 20;
                break;
            case 2:
                setroundcountdown = 10;
                break;
            case 3:
                setroundcountdown = 5;
                break;
            case 4:
                setroundcountdown = 2;
                break;
            default:
                break;
        }

        /// <summary>
        /// Sets up values for start of game. Round and score is reset to 0 whenever a new game is initiated.
        /// </summary>

        roundcountdown = setroundcountdown;
        GlobalControl.score = 0;
        round = 1;
        GlobalControl.modifierx = 0;
        GlobalControl.modifiery = 0;

        /// <summary>
        /// When countdown for each round is above 0, timer decreases by 1 per second. 
        /// The text asset that represents the countdown timer is also updated every second to show the current countdown value.
        /// </summary>

        while (roundcountdown > -5)
        {
            yield return new WaitForSeconds(1);
            roundcountdown--;
            GameObject.Find("Texttime").GetComponent<Text>().text = "" + roundcountdown;
        }
    }

     void Update () {

        /// <summary>
        /// Whenever the timer hits 0, the round counter is increased by 1 and the countdown timer is reset. 
        /// Text asset representing round is increased by 1. Depending on what round it is, the modifiers in Global Control are altered.
        /// This is because the input text file representing the neural network have a mamimum x and y values of 30. However, each round, the grid is only 10 by 10. 
        /// So when a round changes, a multiple of 10 (0, 10, or 20) must be added to the clicked coordinate for it to register with the input text file.
        /// </summary>

        if (round < 9 && roundcountdown == 0)
        {
            round++;
            roundcountdown = setroundcountdown;
            GameObject.Find("Textround").GetComponent<Text>().text = "Round" + round;

            int intround = (int)round;
            switch (intround)
            {
                case 1:
                    GlobalControl.modifierx = 0;
                    GlobalControl.modifiery = 0;
                    break;
                case 2:
                    GlobalControl.modifierx = 10;
                    GlobalControl.modifiery = 0;
                    break;
                case 3:
                    GlobalControl.modifierx = 20;
                    GlobalControl.modifiery = 0;
                    break;
                case 4:
                    GlobalControl.modifierx = 0;
                    GlobalControl.modifiery = 10;
                    break;
                case 5:
                    GlobalControl.modifierx = 10;
                    GlobalControl.modifiery = 10;
                    break;
                case 6:
                    GlobalControl.modifierx = 20;
                    GlobalControl.modifiery = 10;
                    break;
                case 7:
                    GlobalControl.modifierx = 0;
                    GlobalControl.modifiery = 20;
                    break;
                case 8:
                    GlobalControl.modifierx = 10;
                    GlobalControl.modifiery = 20;
                    break;
                case 9:
                    GlobalControl.modifierx = 20;
                    GlobalControl.modifiery = 20;
                    break;
                default:
                    break;
            }
        }

        /// <summary>
        /// High scores are stored on an external text file, at the end of the final round, the score is published to this text file.
        /// Then the scene is changed to the game over screen.
        /// </summary>

        else if (round >= 9 && roundcountdown <= 0)
        {
            string path = "./highscore.txt";

            StreamWriter writer = new StreamWriter(path, true);
            writer.Write(GlobalControl.score+",");
            writer.Close();

            SceneManager.LoadScene(winscene);
        }
    }
}

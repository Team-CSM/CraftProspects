using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Timescript : MonoBehaviour {
    public string winscene;
    public float setroundcountdown;
    static float roundcountdown = 10;
    public static float round = 1;

    IEnumerator Start () {
        roundcountdown = setroundcountdown;
        GlobalControl.score = 0;
        round = 1;

        while (roundcountdown > -5)
        {
            yield return new WaitForSeconds(1);
            roundcountdown--;
            GameObject.Find("Texttime").GetComponent<Text>().text = "" + roundcountdown;
            //Debug.Log("TIME" + roundcountdown);
        }
    }

     void Update () {
        

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

        else if (round >= 9 && roundcountdown <= 0)
        {
            string path = "C://Users//Adrian//Desktop//results//highscore.txt";

            //Write some text to the test.txt file
            StreamWriter writer = new StreamWriter(path, true);
            writer.Write(GlobalControl.score+",");
            writer.Close();

            SceneManager.LoadScene(winscene);
        }
    }
}

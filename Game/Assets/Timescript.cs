using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Timescript : MonoBehaviour {
    public string winscene;
    public string losescene;
    public static int countdown = 60;
    // Use this for initialization
    IEnumerator Start () {

        countdown = 10;
        while (countdown > 0)
        {
            yield return new WaitForSeconds(1);
            countdown--;
            GameObject.Find("Texttime").GetComponent<Text>().text = "" + countdown;
        }



        if (countdown == 0)
        {
            if (GlobalControl.coins >= GlobalControl.aicoins)
            {
                SceneManager.LoadScene(winscene);
            }
            if (GlobalControl.aicoins > GlobalControl.coins)
            {
                SceneManager.LoadScene(losescene);
            }
        }

    }
	
	// Update is called once per frame
	void Update () {
		
	}
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Aiscorescript : MonoBehaviour {

    // Use this for initialization
    IEnumerator Start () {
        yield return new WaitForSeconds(1);
        GlobalControl.aicoins = 0;
        while (Timescript.countdown > 0)
        {
            yield return new WaitForSeconds(GlobalControl.difficulty);
            GlobalControl.aicoins += 1;
            GameObject.Find("Textai").GetComponent<Text>().text = "Computer Score = " + GlobalControl.aicoins;
        }

    }
	
	// Update is called once per frame
	void Update () {
		
	}
}

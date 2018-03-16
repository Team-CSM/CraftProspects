using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FinalScore : MonoBehaviour {

    /// <summary>
    /// In the end game screen, the final score is retrieved from Global Control and showed in the text asset.
    /// </summary>

    void Start () {
        GameObject.Find("Text").GetComponent<Text>().text = "Final score: " + GlobalControl.score;
    }
	
	void Update () {
		
	}
}

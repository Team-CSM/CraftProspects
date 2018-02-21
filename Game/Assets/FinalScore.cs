using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FinalScore : MonoBehaviour {

	// Use this for initialization
	void Start () {
        GameObject.Find("Text").GetComponent<Text>().text = "Final score: " + GlobalControl.score;
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Mutescript : MonoBehaviour {

    // Use this for initialization
    public int mute;

    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

    void OnMouseDown()
    {
        GlobalControl.mute = mute;
        Debug.Log(GlobalControl.mute);
    }
}

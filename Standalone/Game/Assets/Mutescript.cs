using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Mutescript : MonoBehaviour {

    public int mute;

    void Start () {
		
	}

	void Update () {
		
	}

    /// <summary>
    /// In development. Please ignore.
    /// </summary>

    void OnMouseDown()
    {
        GlobalControl.mute = mute;
        Debug.Log(GlobalControl.mute);
    }
}

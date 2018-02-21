using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Easy : MonoBehaviour
{
    public string sceneLocate;

    void Start () {
	}
	
	void Update () {
	}

    void OnMouseDown()
    {
        GlobalControl.difficulty = 1;
        SceneManager.LoadScene((sceneLocate));
    }
}

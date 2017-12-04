using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Hard : MonoBehaviour {

    public string sceneLocate;
    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }
    void OnMouseDown()
    {
        GlobalControl.difficulty = 1;
        SceneManager.LoadScene((sceneLocate));
    }
}

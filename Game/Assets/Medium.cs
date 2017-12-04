using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Medium : MonoBehaviour {

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
        GlobalControl.difficulty = 3;
        SceneManager.LoadScene((sceneLocate));
    }
}

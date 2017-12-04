using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Impossible : MonoBehaviour {
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
        GlobalControl.difficulty = 0.5f;
        SceneManager.LoadScene((sceneLocate));
    }
}

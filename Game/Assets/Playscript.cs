using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Playscript : MonoBehaviour {

    public string sceneLocate;
    public GameObject play;
    // Use this for initialization
    void Start()
    {
        //At the start of the game, the zombies will find the gameobject called wayPoint.
        //play = GameObject.Find("Play");
        //SceneManager.LoadScene((sceneLocate));
    }
    // Update is called once per frame
    void Update()
    {

    }

    void OnMouseDown()
    {

        SceneManager.LoadScene((sceneLocate));
        Debug.Log("CLICKED");
    }

}
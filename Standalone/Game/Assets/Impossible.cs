using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Impossible : MonoBehaviour
{
    public string sceneLocate;

    void Start()
    {
    }

    void Update()
    {
    }

    void OnMouseDown()
    {
        GlobalControl.difficulty = 4;
        SceneManager.LoadScene((sceneLocate));
    }
}
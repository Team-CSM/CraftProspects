﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Quitscript : MonoBehaviour
{

    //public string sceneLocate;
    public GameObject button;

    void Start()
    {
    }

    void Update()
    {
    }

    void OnMouseDown()
    {
        Application.Quit();
        Debug.Log("CLICKED");
    }

}